#WAP to find the second largest element int list
li = [13, 9, 25, 30, 35]

Max = li[0]
SecondMax = li[0]

for num in range(1, len(li)):
    if li[num] > Max:
        SecondMax = Max
        Max = li[num]
    elif li[num] > SecondMax:
        SecondMax = li[num]

print("Maximum element:", Max)
print("Second Maximum element:", SecondMax)