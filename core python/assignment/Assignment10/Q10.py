# WAP a program to remove all accurrences of a given element in the list
li=[10,20,10,30,10,40,20]
num=int(input("Enter Element to remove"))
new=[]
for i in range(0,len(li)):
    if(li[i]!=num):
        new=new+[li[i]]
print("Original list",li)
print("After Removing",new)        
