X=int(input("Enter the number:"))
n=int(input("Enter the ending value:"))
dem=1
sign=1
sum=0
for i in range(1,n+1):
    sum+=sign*(X**i)/dem
    dem+=2
    sign*=-1
print("Sum of the series",sum)    