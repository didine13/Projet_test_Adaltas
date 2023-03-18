import os
from supabase import create_client
import subprocess

API_URL = os.environ.get("API_URL")
API_KEY = os.environ.get("API_KEY")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# supabase = create_client(API_URL, API_KEY)
supabase = create_client(API_URL, SUPABASE_KEY)


def create_user(users):
    """
    This function create new user and his profile

    Arguments :
    users
        *   email           -- email address of user
        *   password        -- password of user
        *   profile_data    -- contains user's data
        *   first_name      -- user first name
        *   last_name       -- user last name
        *   job             -- user job (activity)

    Returns boolean
    """

    user_uuid_tab = []
    if len(users) > 0:
        for user in users:
            # Create user un auth.users
            command = (
                'curl -X POST ${API_URL} -H "apikey: ${API_KEY}" -H "Authorization: Bearer ${SUPABASE_KEY}" -H "Content-Type: application/json" -d \'{"email": "'
                + user["email"]
                + '","password": "'
                + user["password"]
                + '","email_confirm": true,"user_metadata": { "first_name": "'
                + user["first_name"]
                + '","last_name": "'
                + user["last_name"]
                + '", "job":"'
                + user["job"]
                + "\"}}'"
            )

            # print("\nAppel de la  commande '{}'".format(command), flush=True)
            (status, output) = subprocess.getstatusoutput(command)
            # print("status: {}\nsortie : '{}'".format(status, output))
            user_uuid = output.split(",")[0].split("{")[-1].split(":")[-1].strip('"')
            if status == 0 and user_uuid.isdigit():
                print(
                    user["email"],
                    ":",
                    output.split(",")[1].split("}")[0].split(":")[-1],
                )
            else:
                user_uuid_tab.append(user_uuid)
    return user_uuid_tab


def getProfiles(user):
    """
    This function Returns the profiles list of firends of authentified user

    Argument :
    user    -- json which contains login an password to authenticate user

    Returns a list of dictionnaries
    """
    user_signin = supabase.auth.sign_in_with_password(user)
    data = supabase.table("profiles").select("*").execute()
    return data


def save_friends(user1_uuid, user2_uuid):
    """
    This function create friends relation

    Arguments :
    user1_uuid  -- correspond to uuid from auth.users of one user
    user2_uuid  -- correspond to uuid from auth.users of another user

    Returns boolean
    """
    return (
        supabase.table("friends")
        .insert({"user1": user1_uuid, "user2": user2_uuid})
        .execute()
    )
