#take input
basic = float(input("Enter Basic Salary: "))
# calculate Dearness Allowance
da = basic * 10 / 100
# calculate Travel Allowance
ta = basic * 12 / 100
# calculate House Rent Allowance
hr = basic * 15 / 100
#calculate Total Salary
salary = basic + da + ta + hr
print("Total Salary =", salary)