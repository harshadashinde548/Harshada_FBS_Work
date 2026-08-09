#....Q7WAP to find sum of digits using recursion
def SOD(n):
    if(n>0):
        d=n%10
        n=n//10
        return d+SOD(n)
    else:
        return 0
n=int(input("Enter the number:"))
res=SOD(n)
print("Sum of digits",res)