username = input("enter your firstname:")
password= input("enter your lastname:")

def access(usr,pwd):
    if usr == "amankhadse" and pwd == 123456:
        return True
    else:
        return False\
 
verified  = access(username,password)            

if verified == True:
    print("welcome")
else:
    print("enter again")    