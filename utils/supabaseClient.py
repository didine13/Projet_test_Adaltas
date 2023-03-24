def getProfiles(supabase, email, password):
    """
    This function Returns the profiles list of firends of authentified user

    Returns a list of dictionnaries
    """
    try:
        credentials = {"email": email, "passwdord": password}
        supabase.auth.sign_in_with_password(credentials)
        profiles = supabase.table("profiles").select("*").execute().data
        supabase.auth.sign_out()
        return profiles
    except Exception as e:
        print("Error : ",e)

    return False
