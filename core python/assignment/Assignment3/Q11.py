Age=int(input("Enter the Age:"))
TKprice1=int(input("Enter the TKprice:"))
Total_price=0
if(Age<12):
    Total_price=Total_price+(TKprice1-TKprice1*0.3)
elif(Age<59):
    Total_price=Total_price+(TKprice1-TKprice1*0.5)
else:
    Total_price=Total_price+TKprice1
Age=int(input("Enter the Age:"))
TKprice2=int(input("Enter the TKprice:"))
if(Age<12):
    Total_price=Total_price+(TKprice2-TKprice2*0.3)
elif(Age<59):
    Total_price=Total_price+(TKprice2-TKprice2*0.5)
else:
    Total_price=Total_price+TKprice2
Age=int(input("Enter the Age:"))
TKprice3=int(input("Enter the TKprice:"))
if(Age<12):
    Total_price=Total_price+(TKprice3-TKprice3*0.3)
elif(Age<59):
    Total_price=Total_price+(TKprice3-TKprice3*0.5)
else:
    Total_price=Total_price+TKprice3
Age=int(input("Enter the Age:"))
TKprice4=int(input("Enter the TKprice:"))
if(Age<12):
    Total_price=Total_price+(TKprice4-TKprice4*0.3)
elif(Age<59):
    Total_price=Total_price+(TKprice4-TKprice4*0.5)
else:
    Total_price=Total_price+TKprice4
Age=int(input("Enter the Age:"))
TKprice5=int(input("Enter the TKprice:"))
if(Age<12):
    Total_price=Total_price+(TKprice5-TKprice1*0.3)
elif(Age<59):
    Total_price=Total_price+(TKprice5-TKprice1*0.5)
else:
    Total_price=Total_price+TKprice5
print('Total Amount',Total_price)    
                                