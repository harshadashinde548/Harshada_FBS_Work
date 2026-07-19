#write a program to input all sides of a triangle and check Whether triangle is valid or not
FA=int(input("Enter the first angle:"))
SA=int(input("Enter the second angle:"))
TA=int(input("Enter the third angle:"))
if(FA+SA>TA and SA+TA>FA and TA+SA>FA):
    print("Triangle is valid")
else:
    print("Triangle is not valid")