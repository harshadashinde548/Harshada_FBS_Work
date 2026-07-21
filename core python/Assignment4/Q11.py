# WAP to check if given nunber storong Nubmber 
n=int(input("Enter the number:"))
temp=n
sum=0
while(n>0):
    d=n%10==0
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(temp==sum):
   print("Strong Number")
else:
   print("Not Strong Number")        

