# WAP of having a number of elements in the list and find out even and odd elements in that list and create two separate lists which will have even element and other will have odd elements
n = int(input("Enter the number: "))
li = []
for i in range(n):
    num = int(input("Enter the Element: "))
    li = li + [num]
even = []
odd = []
for j in range(0, len(li)):
    if li[j] % 2 == 0:
        even = even + [li[j]]
    else:
        odd = odd + [li[j]]
print("Original list:", li)
print("Even list:", even)
print("Odd list:", odd)