#write a program to find print the following fibonacci series using function
def fibonacii_series(n):
    a=-1
    b=1
    for i in range(n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
n=int(input("Enter the number"))   
res=fibonacii_series(n)
print(res)     