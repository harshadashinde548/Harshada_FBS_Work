def odd_number(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input("Enter the number"))
res=odd_number(n)
print(res)    