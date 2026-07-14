P=int(input("Enter the Principle:"))
T=int(input("Enter the Time:"))
R=int(input("Enter the Rate:"))
#Calculate the compound interset
CI=P*(1+R/100)**T-P
print("compound interset is:",CI)