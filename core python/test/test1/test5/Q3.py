Data = [
    [101, "sanika", 45000],
    [102, "harshada", 13000],
    [103, "prasanna", 12000],
    [104, "kiran", 19000]
]

for i in range(len(Data)):
    for j in range(i + 1, len(Data)):
        if Data[i][2] < Data[j][2]:
            Data[i][2], Data[j][2] = Data[j][2], Data[i][2]

print(Data)