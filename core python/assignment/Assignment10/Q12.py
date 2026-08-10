# WAP to create three list of numbers their sequares and cubes
li = [1, 2, 3, 4, 5]
Square = []
Cube = []
for i in range(0, len(li)):
    Square = Square + [li[i] ** 2]
    Cube = Cube + [li[i] ** 3]
print("Number:", li)
print("Square:", Square)
print("Cube:", Cube)