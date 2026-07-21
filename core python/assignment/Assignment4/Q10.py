#WAP to check if given number is perfect Number
n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("Perfect Number")
else:
    print("Not perfect Number")      