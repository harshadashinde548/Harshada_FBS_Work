def sod(n):
    sum=0
    while(n>0):
        digit=n%10
        n=n//10
        sum=sum+digit
    return sum
n=int(input("Enter number"))
res=sod(n)
print(res)    