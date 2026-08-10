#WAP a program to remove duplicates from the list
li = [10, 20, 40, 60, 80, 10]
new = []
for i in li:
    if i not in new:
        new = new + [i]
print("Original List:", li)
print("New List:", new)