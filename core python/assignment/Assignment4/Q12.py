#WAP to check if given number is Armstrong number or not
no=int(input("Enter the number you want check="))
count=len(str(no))
temp=no
total=0
while no>0:
    d=no%10
    total=total+(d**count)
    no=no//10
print(total)
if total==temp:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")        