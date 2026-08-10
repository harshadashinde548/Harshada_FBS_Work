# 10. Write a program to print list after removing even numbers.
li = [10, 22, 42, 54, 56, 67]

new = li.copy()

for i in li:
    if i % 2 == 0:
        new.remove(i)

print("Original List =", li)
print("After Removing Even Numbers =", new)