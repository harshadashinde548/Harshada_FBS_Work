#Take input
h = int(input("Enter Hours: "))
m = int(input("Enter Minutes: "))
s = int(input("Enter Seconds: "))
#calculate tatal seconds
total = (h * 3600) + (m * 60) + s
print("Total Seconds =", total)