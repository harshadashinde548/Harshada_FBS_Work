def Prime(num,i):
    if(num==i):
        return True
    if(num%i==0):
        return False
    return Prime(num,i+1)
num=int(input("Enter number:"))
if(num>1):
    res=Prime(num,2)
    if(res):
        print("Number is Prime")
    else:
        print("Number is not Prime")
else:
    print("Number is not Prime")            