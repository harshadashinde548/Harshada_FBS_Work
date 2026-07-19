Unit=int(input("Enter the Unit:"))
if(Unit<=50):
    bill=Unit*0.50
elif(Unit<=150):
    bill=50*0.50+((Unit-50)*0.75)
elif(Unit<=250):
    bill=(50*0.50)+(100*0.75)+((Unit-150)*1.20)    
else:
    bill=(50*0.50)+(100*0.75)+(100*1.20)+((Unit-250)*1.50)
surcharge=bill*20/100
Total_bill=bill+surcharge
print("Total_bill",Total_bill)   

