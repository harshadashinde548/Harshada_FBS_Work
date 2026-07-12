#Take input
feet = int(input("Enter Feet: "))
inch = int(input("Enter Inches: "))
#calculate inch
total_inch = (feet * 12) + inch
cm = total_inch * 2.54
meter = cm / 100

print(f'Meter =, {meter},Centimeter =, {cm}')
