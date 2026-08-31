# 5. Python Program to Find the Union of two Lists without
# using set concept.
li1=[1,2,3,4,5]
li2=[4,5,6,7,8]
Union=[]
for i in li1:
    Union.append(i)
for j in li2:
    if j not  in Union:
        Union.append(j)
print("Union:",Union)            
