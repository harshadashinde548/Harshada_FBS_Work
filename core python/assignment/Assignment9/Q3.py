def reverseNumber(n,rev):
    if(n>0):
        d=n%10
        rev=rev*10+d
        return reverseNumber(n//10,rev)
    else:
        return rev
n=int(input("Enter the number"))
res=reverseNumber(n,0)
print("Reverse number",res)