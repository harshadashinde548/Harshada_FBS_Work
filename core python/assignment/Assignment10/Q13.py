# WAP to print list after removing even number
li = [30, 43, 44, 15, 8]
new = []
for i in range(len(li)):
    if li[i] % 2 != 0:
        new = new + [li[i]]
print("Original List:", li)
print("List after removing even numbers:", new)