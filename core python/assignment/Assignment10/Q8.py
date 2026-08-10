# WAP to create a duplicate of an existing list it should not point to same list
li=[20,40,60,90]
new=[]
for i in li:
    new=new+[i]
print("Original List",li)
print("Duplicate List",new)
print("li is new")    