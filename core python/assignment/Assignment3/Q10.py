Gender=(input("Enter the Gender(M,F)"))
Age=int(input("Enter the Age"))
if(Gender=='F'):
    if(Age>=18):
        print("Eligiable for mary")
    else:
        print("Not Eligible")
else:
    if(Age>=21):
        print("Eligible for mary")
    else:
        print("Not Eligiable")                