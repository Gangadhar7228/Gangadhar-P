import math

radius=float(input("enter the radius of the circle="))

area=math.pi*radius**2
circumference=2*math.pi*radius
area_integer=int(area)

print(f"area  :{area:.2f}")
print(f"circumference  :{circumference:.2f}")
print(f"area as int   :{area_integer}")