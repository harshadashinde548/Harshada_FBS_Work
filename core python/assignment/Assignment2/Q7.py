num = int(input("Enter 3-digit Number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
sum = a + b + c
print("Sum =", sum)