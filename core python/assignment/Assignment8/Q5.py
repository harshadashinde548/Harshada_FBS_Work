#sum of all prime numbers bet'n 1 to n
def prime_number(n):
    sum=0
    for num in range(1,n+1):
        if(num>1):
            for i in range(2,num):
                if(num%i==0):
                      break
            else:
                sum=sum+num
    return sum 
n=int(input("Enter the number"))
print('sum=',prime_number(n))            