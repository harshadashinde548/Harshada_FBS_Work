#Write a program to input angles of a triangle and check Whether triangle is valid or not
FA=int(input("Enter the first Angle:")) 
SA=int(input("Enter the Second Angle:")) 
TA=int(input("Enter the Third Angle:")) 
if(FA+SA+TA==180):
    print("Triangle is valid")
else:
    print("Triangle is unvalid")    