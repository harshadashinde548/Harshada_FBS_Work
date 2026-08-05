def leap(year):
    if(year%400==0)or(year%4==0)and(year%100):
        print('Leap year')
    else:
        print('Not Leap year')
year=int(input("Enter the year:"))
leap(year)            