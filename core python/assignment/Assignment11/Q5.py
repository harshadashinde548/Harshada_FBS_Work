# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.
li = ["apple", "table", "chair", "cake", "mango"]
print("Original List",li)
li.sort(key=len)
print("Sorted List =", li)