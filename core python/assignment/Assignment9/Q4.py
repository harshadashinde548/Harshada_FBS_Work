def SON(n):
    if(n>0):
        return n+SON(n-1)
    else:
        return 0
n=int(input("Enter the number:"))
res=SON(n)
print("sum of Number",res)    