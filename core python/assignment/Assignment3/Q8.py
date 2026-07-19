import random 
Userid=input("Enter the userid:")
Password=input("Enter the Password:")
if(Userid=='Harshada' and Password=='123'):
    Capcha=random.randint(1000,9999)
    print('Capcha:',Capcha)
    Chuser=int(input("Enter the Capcha:"))
    if(Chuser==Capcha):
        print("Login Sussecfully!")
    else:
        print("invalid Capcha")
else:
    print("Invalid userid and password")        
    