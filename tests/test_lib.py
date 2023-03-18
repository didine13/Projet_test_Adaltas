from project import lib

def test_create_user():
    print("Create 5 users and profiles")
    rows = [
            {
                'email': 'tesut1@test1.fr',
                'password': "password",
                'first_name': 'Alex',
                'last_name': "Dupont",
                'job': 'dev'
            },
            {
                'email': 'remyui@example.fr',
                'password': "password1",
                'first_name': 'Remy',
                'last_name': "Teit",
                'job': 'dev'
            },
            {
                'email': 'diantge@example2.fr',
                'password': "password3",
                'first_name': 'Diane',
                'last_name': "Durand",
                'job': 'front'
            },
            {
                'email': 'marjfie@test1.fr',
                'password': "mdpass",
                'first_name': 'Marie',
                'last_name': "Mars",
                'job': 'r&d'
            },
            {
                'email': 'ladffure@test1.fr',
                'password': "motdepasse",
                'first_name': 'Laure',
                'last_name': "ziot",
                'job': 'acquisition'
            }]
    print("Create ended")
    uuid_tab = lib.create_user(users=rows)
    assert(len(rows) == len(uuid_tab))

def test_create_friends():
    user1 = 'd9064bb5-1501-4ec9-bfee-21ab74d645b8'
    user2 = 'f76629c5-a070-4bbc-9918-64beaea48848'
    data = lib.save_friends(user1_uuid=user1, user2_uuid=user2)
    assert(len(data.data) > 0)

def test_getProfiles():
    user = {"email": "ok@elodine.com", "password": "secret"}
    lib.getProfiles(user)
