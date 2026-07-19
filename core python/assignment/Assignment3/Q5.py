#write  a program to check whether the triangle is equilateral ,isosceles,scalene
FS=int(input("Enter the First side:"))
SS=int(input("Enter the Second side:"))
TS=int(input("Enter the Third side:"))
if(FS==SS==TS):
    print("Equilateral")
elif(FS==SS or SS==TS or TS==FS ):
    print("Isosceles")
else:
    print("Scalene")        