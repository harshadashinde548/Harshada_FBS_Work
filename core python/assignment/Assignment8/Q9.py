def palindrome_number(num):
    temp=num 
    rev=0
    while(temp>0):
        digit=num%10
        temp=temp//10
        rev=rev*10+digit
    if(rev==temp):
        return True
    else:
        return False
num=int(input("Enter number"))
res=palindrome_number(num) 
print(res)      
