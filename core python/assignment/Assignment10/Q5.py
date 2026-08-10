#Accept a number from user and check if this element is present in the list or not also tell how many times it is present in the list
li = [10, 20, 40, 60, 80,20]

num = int(input("Enter the number: "))
count = 0

for i in range(0, len(li)):
    if li[i] == num:
        count = count + 1

if count > 0:
    print("Element is present")
    print("Count of element:", count)
else:
    print("Element is not present")