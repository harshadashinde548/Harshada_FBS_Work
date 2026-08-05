#WAP to calculate area of circle
def area_circle(r):
    area=(3.14*(r**2))
    return area
r=int(input("Enter the radius"))
res=area_circle(r)
print(res)