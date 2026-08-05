def sos(n):
    if(n>0):
        return n+sos(n-1)
    else:
        return 0
n=int(input("Enter number"))
res=sos(n)
print(res)    