#....Q5WAP to find factorial using recursion
def Factorial(n):
    if(n>0):
        return  n*Factorial(n-1)
    else:
        return 1
n=int(input("Enter the number"))
res=Factorial(n)
print("Factorial num",res)    