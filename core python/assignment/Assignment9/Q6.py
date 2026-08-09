def Fibonacci(n,a,b):
    if(n>0):
        c=a+b
        print(c,end='  ')
        return Fibonacci(n-1,b,c)
n=int(input("Enter number:"))
print("Fibonacci Series")
Fibonacci(n,-1,1)