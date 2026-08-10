# WAP a program to reverse the list 
li = [13, 9, 25, 30, 35]
rev = []
for i in range(len(li) - 1, -1, -1):
    rev = rev + [li[i]]
print("Original List:", li)
print("Reverse List:", rev)