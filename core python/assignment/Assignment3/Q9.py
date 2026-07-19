S1=int(input("Enter first subject"))
S2=int(input("Enter second subject"))
S3=int(input("Enter third subject"))
S4=int(input("Enter fourth subject"))
S5=int(input("Enter fifth subject"))
Total=S1+S2+S3+S4+S5
Percentage=Total/500*100
if(Percentage>=60):
    print("First Class")
elif(Percentage>=50):
    print("Second Class")  
elif(Percentage>=40):
    print("pass Class") 
else:
    print("Faild")

