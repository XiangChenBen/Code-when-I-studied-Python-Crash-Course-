users = {
    "jj":{
        "first":"Jack",
        "last":"Jhon",
        "sex":"male"
    },

    "aa":{
        "first":"Anna",
        "last":"Aron",
        "sex":"female"
    }
}

for username,userinfo in users.items():
    print(f"\nUsername:{username.upper()}")
    fullname = f"{userinfo['first']} {userinfo['last']}"
    sex = userinfo["sex"]

    print(f"\tFull Name:{fullname}")
    print(f"\tSex:{sex}")