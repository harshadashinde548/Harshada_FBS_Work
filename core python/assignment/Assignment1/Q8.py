Days=int(input("Enter the days:"))
Years=Days // 365
# print(Years)
Days=Days % 365
# print(Days)
weeks=Days//7
# print(weeks)
Days=Days % 7
print(f'years:{Years},Days:{Days},Weeks:{weeks},Days:{Days}')