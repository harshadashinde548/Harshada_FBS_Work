#6. Write a program to print first n prime numbers.  
n=int(input("Enter the number:"))
count=0
num=2
print("First the {n} Prime numbers:")
while(count<n):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)
        count=count+1
    num=num+1        
