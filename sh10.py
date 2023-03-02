users={"user1": "pass","user2":"pass2"}




username=input("enter username:")
if username in users:
    password=input("enter your password:")
    correctpassword=users[username]

    if password !=correctpassword:
        print("incorrect password")
    else:
        print("login successfull")
else:
    print("no such users")


#a=[1,3,4,5]
#a[0]

a=(4,6,7)
a[0]

a={"key":"value","key2":"value2"}

a["key"]
