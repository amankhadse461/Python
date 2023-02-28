username = input("enter your username:")
password= input("enter your password:")

def access(usr,pwd):
    if usr == "aman" and pwd == "1234":
        return True
    else:
        return False
 
verified  = access(username,password)            

if verified == True:
    print("welcome")
else:
    print("enter again") 