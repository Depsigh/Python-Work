# Administrator accounts list
adminlist = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
def getCreds ():
    user_name = input ("What is your username? ")
    password = input ("What is your password? ")

    userInfo = [
        {
            "username" : user_name,
            "password" : password
        }
    ]
    return userInfo

user_info =getCreds()
def checkLogin (userInfo, adminlist):
        if userInfo in adminlist:
            loggedIn = True

        else:
            loggedIn = False

            while loggedIn == False:
                print ("Login Failed. ")
                retry = getCreds()
                return retry

getCreds ()

checkLogin (user_info, adminlist)
