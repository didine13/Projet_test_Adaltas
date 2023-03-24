from utils import supabaseAdmin, supabaseClient
from utils.createClient import initializeClient
from utils.params import SUPABASE_KEY, API_URL, API_KEY

def test_createProfile():
    supabase = initializeClient(API_URL, SUPABASE_KEY)
    print("Creation test of 5 users and profiles")
    rows = [
        {
            "email": "test84512create1@test1.fr",
            "password": "password",
            "first_name": "Alex",
            "last_name": "Dupont",
            "job": "dev",
        },
        {
            "email": "remyui84512create@example.fr",
            "password": "password1",
            "first_name": "Remy",
            "last_name": "Teit",
            "job": "dev",
        },
        {
            "email": "diant84512gcreae@example2.fr",
            "password": "password3",
            "first_name": "Diane",
            "last_name": "Durand",
            "job": "front",
        },
        {
            "email": "mar895623jficreae@test1.fr",
            "password": "mdpass",
            "first_name": "Marie",
            "last_name": "Mars",
            "job": "r&d",
        },
        {
            "email": "ladff84512creaure@test1.fr",
            "password": "motdepasse",
            "first_name": "Laure",
            "last_name": "ziot",
            "job": "acquisition",
        },
    ]

    cpt = 0
    for user in rows:
        print("------------------------ Create profile", user)
        profile = supabaseAdmin.createProfile(supabase, user)
        assert profile != False and len(profile) == 1
        # user_uuid = profile.split(",")[0].split("{")[-1].split(":")[-1].strip('"')
        user_uuid = profile[0]["id"]

        # verify if profile created well
        data = supabaseAdmin.showUserProfile(supabase, user_uuid)
        assert len(data) == 1
        for_comparison = data[0]
        for key, value in user.items():
            if key != "password":
                print(
                    key,
                    " : user_key = ",
                    value,
                    " - from database = ",
                    for_comparison[key],
                )
                assert key in for_comparison.keys() and value == for_comparison[key]

        cpt = cpt + 1
        print("------------------------ Create profile completed", user[key])

        # Clear table by deleting of newly created profile
        print("------------------------ Clear database by deleting of newly created profile")
        assert supabaseAdmin.deleteProfile(user_uuid) != False

    assert cpt == len(rows)
    print("End Creation of 5 profiles")


def test_create_friends():
    print("Test create friends")
    supabase = initializeClient(API_URL, SUPABASE_KEY)
    rows = [
        {
            "email": "tes84521t1@testcrea1.fr",
            "password": "password",
            "first_name": "Alex",
            "last_name": "Dupont",
            "job": "dev",
            "town": "paris"
        },
        {
            "email": "remyu412i@exacreample.fr",
            "password": "password1",
            "first_name": "Remy",
            "last_name": "Teit",
            "job": "dev",
        }]
    print("------------------------ Create 2 profiles")
    user_uuid1 = supabaseAdmin.createProfile(supabase, rows[0])[0]["id"]
    user_uuid2 = supabaseAdmin.createProfile(supabase, rows[1])[0]["id"]

    print("------------------------ Create friends")
    data = supabaseAdmin.save_friends(supabase, user1_uuid=user_uuid1, user2_uuid=user_uuid2)
    assert data != False
    assert user_uuid1 == data[0]['user1'] and user_uuid2 == data[0]['user2']

    print("------------------------ Clear database")
    assert supabaseAdmin.deleteProfile(user_uuid1) != False
    assert supabaseAdmin.deleteProfile(user_uuid2) != False
    print("End test create friends")

def test_getProfiles():
    print("Test list profiles")
    # create superbase client
    supabase_admin = initializeClient(API_URL, SUPABASE_KEY)
    rows = [
            {
                'email': 'rep45pst1@test1.fr',
                'password': "password",
                'first_name': 'Alex',
                'last_name': "Dupont",
                'job': 'dev'
            },
            {
                'email': 're85omy@example.fr',
                'password': "password1",
                'first_name': 'Remy',
                'last_name': "Teit",
                'job': 'dev'
            },
            {
                'email': 'dian841fe@example2.fr',
                'password': "password3",
                'first_name': 'Diane',
                'last_name': "Durand",
                'job': 'front'
            }]

    print("------------------------ Create 3 profiles")
    authentified_user = rows[0].copy()
    for user in rows:
        profile = supabaseAdmin.createProfile(supabase_admin, user)
        user["uuid"] = profile[0]["id"]

    print("------------------------ Create 1 friend relation between 2 profiles")
    supabaseAdmin.save_friends(supabase_admin, user1_uuid=rows[0]['uuid'], user2_uuid=rows[1]['uuid'])

    print("------------------------ List profiles")
    supabase = initializeClient(API_URL, API_KEY)
    profiles = supabaseClient.getProfiles(supabase, authentified_user["email"], authentified_user["password"])
    friends = supabaseAdmin.getFriends(supabase_admin, rows[0]['uuid'])

    print("------------------------ Clear database")
    for user in rows:
        assert supabaseAdmin.deleteProfile(user["uuid"]) != False

    # Comparison of content of friend list and profile list returned by policy
    assert len(profiles) != 0 and len(friends) != 0 and len(profiles) == len(friends)
    isSameUuid = 0
    for friend in friends:
        for profile in profiles:
            if friend['user2'] == profile['id']:
                isSameUuid = isSameUuid + 1
    assert len(profiles) == isSameUuid

    print("End test list profiles")
