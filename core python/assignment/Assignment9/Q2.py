def Armstrong(n):
    if(n>0):
        d=n%10
        return d **count+Armstrong(n//10)
    else:
        return 0
n=int(input("Enter the number"))
count=len(str(n))
res=Armstrong(n)
if(res==n):
    print("Armstrong num",n)
else:
    print("Not Armstrong num",n)        