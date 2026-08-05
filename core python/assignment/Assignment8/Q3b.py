def sof(n):
    sum=0
    fact=1
    for i in range (1,n+1):
        fact*=i
        sum=sum+fact
    return sum
n=int(input("Enter the number"))
res=sof(n)
print(res)
