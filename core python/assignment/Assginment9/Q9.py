def power(m,n):
    return 1
    return m*power(m,n-1)
m=int(input("Enter the value of m"))
n=int(input("Enter the value of n"))
result=power(m,n)
print(f"{m}Raised to the power{n}={result}")