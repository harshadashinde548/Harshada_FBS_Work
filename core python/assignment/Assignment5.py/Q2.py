n=int(input("Enter number of Student:"))
total_Percentage=0
for i in range(1,n+1):
    print("Student,i")
    total=0
    for j in range(1,6):
        marks=int(input("Enter marks of subject{j}:"))
        total=total+marks
        Percentage=total/5
        print("Percentage",Percentage)
        total_Percentage=total_Percentage+Percentage
    average=total_Percentage/n
print("Average Percentage=",average)   