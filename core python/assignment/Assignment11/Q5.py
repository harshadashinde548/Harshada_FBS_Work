# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.
li = ["apple", "table", "chair", "cake", "mango"]
print("Original List",li)
for i in range(1,len(li)):
    for j in range(0,len(li)-i):
        if(len(li[j])>len(li[j+1])):
            li[j],li[j+1]=li[j+1],li[j]

print("Sorted List =", li)