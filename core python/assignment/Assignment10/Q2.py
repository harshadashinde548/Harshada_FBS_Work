#Write a program to find maximum and minimum element in a list
li=[13,9,25,30,35]
Max=li[0]
Min=li[0]
for num in li:
    if num>Max:
        Max=num
    if num<Min:
        Min=num
print("Maximum:",Max)
print("Minimum:",Min)        