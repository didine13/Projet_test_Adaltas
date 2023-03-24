from supabase import create_client, Client

def initializeClient(supabase_url, supabase_key):
    """
    This function initialize new admin supabase client

    Returns supabase client
    """
    supabase: Client = create_client(supabase_url, supabase_key)
    return supabase
