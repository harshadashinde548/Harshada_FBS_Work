# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists
li = [10, 21, 32, 43, 54, 65]
even = []
odd = []
for i in li:
    if i % 2 == 0:
        even = even + [i]
    else:
        odd = odd + [i]
print("Original List:", li)
print("Even List:", even)
print("Odd List:", odd)
