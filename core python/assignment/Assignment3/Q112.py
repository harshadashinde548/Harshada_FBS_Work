num=int(input("Enter 3 digits"))
temp=num
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
d3=num//10
reverse=d1*100+d2*10*d3
if(temp==reverse):
    print("Palindrome Digit")
else:
    print("not a palindrome Digit")    