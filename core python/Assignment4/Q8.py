#WAP  to find which num are divisible by 7 and multiple of in a given range
start=int(input("Enter starting the number: "))
end=int(input("Enter ending the number:"))
for i in range(start,end+1):
    if(i%7==0 and i%5==0):
        print(i)