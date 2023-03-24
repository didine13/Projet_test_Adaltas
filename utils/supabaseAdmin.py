
import subprocess
from utils.params import SUPABASE_KEY, API_URL

def createProfile(supabase, user):
    """
    This function create new user and his profile

    Parameters :
    supabase                string -- supabase client
    user
        *   email           string -- email address of user
        *   password        string -- password of user
        *   first_name      string -- user first name
        *   last_name       string -- user last name
        *   job             string -- user job or activity (could be empty)
        *   address         string -- user address (could be empty)
        *   town            string -- user town (could be empty)

    Returns user data or boolean (False) if error
    """

    if len(user) > 0:
        # Create user un auth.users
        command = (
            'curl -X POST "${API_URL}/auth/v1/admin/users" -H "apikey: ${API_KEY}" -H "Authorization: Bearer ${SUPABASE_KEY}" -H "Content-Type: application/json" -d \'{"email": "'
            + user["email"]
            + '","password": "'
            + user["password"]
            + '","email_confirm": true}\''
        )

        (status, output) = subprocess.getstatusoutput(command)
        # print("status: {}\nsortie : '{}'".format(status, output))
        user_uuid = output.split(",")[0].split("{")[-1].split(":")[-1].strip('"')
        if status == 0 and user_uuid.isdigit():
            print(
                user["email"],
                ":",
                output.split(",")[1].split("}")[0].split(":")[-1],
            )
            return False
        else:
            user.pop("email")
            user.pop("password")
            output = updateProfile(supabase, user, user_uuid)
            return output

def updateProfile(supabase, user_details, user_uuid):
    """
    This function create new user and his profile

    Parameters :
    usser_details
        *   first_name      string -- user first name
        *   last_name       string -- user last name
        *   job             string -- user job or activity (could be empty)
        *   date_of_birth   srting -- user birthday
        *   address         string -- user address (could be empty)
        *   town            string -- user town (could be empty)
    user_uuid               string -- user uuid

    Returns user data from public.profiles tableor boolean (False) if error
    """
    try:
        data = supabase.table("profiles").update(user_details).eq("id", user_uuid).execute()
        return data.data
    except Exception as e:
        print('Erreur :', e)

    return False

def deleteProfile(user_uuid):
    """
        This function deletes user (from the auth.users table and all other related tables)

        Parameters :
        user_uuid       string -- user uuid

        Returns status as integer, and output as sting
    """
    command = 'curl -X DELETE "${API_URL}/auth/v1/admin/users/'+user_uuid+'" -H "apikey: ${API_KEY}" -H "Authorization: Bearer ${SUPABASE_KEY}"'
    status, output = subprocess.getstatusoutput(command)
    if status == 0 and output.split(",")[0].split("{")[-1].split(":")[-1].strip('"').isdigit() == False:
        return output

    if output.split(",")[0].split("{")[-1].split(":")[-1].strip('"').isdigit():
        print("Error :", output.split("\n")[-1])
    return False

def showUserProfile(supabase, user_uuid):
    """
        This function get user profile

        Parameters :
        user_uuid       string -- user uuid

        Returns profile details as dictionnary
    """
    return supabase.table("profiles").select("*").eq("id", user_uuid).execute().data

def save_friends(supabase, user1_uuid, user2_uuid):
    """
    This function create friends relation

    Parameters :
    supabase    -- supabase client
    user1_uuid  -- correspond to uuid from auth.users of one user
    user2_uuid  -- correspond to uuid from auth.users of another user

    Returns boolean
    """
    try:
        data = supabase.table("friends") \
                    .insert({"user1": user1_uuid, "user2": user2_uuid})  \
                    .execute().data
        return data
    except Exception as e:
        print("Error :", e)
        return False

def getFriends(supabase, user_uuid):
    """
        This function get user profile

        Parameters :
        user_uuid       string -- user uuid

        Returns profile details as dictionnary
    """
    return supabase.table("friends").select("user2").eq("user1", user_uuid).execute().data
