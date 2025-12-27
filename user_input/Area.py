# Write a program to accept user input to calculate the following :-
# Area of a circle & rectangle
# Perimeter of circle & rectangle
# Volume of circle & rectangle

import math

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
height = float(input("Enter the height: "))
radius = float(input("Enter radius: "))

area_rect = length * breadth
area_circ = math.pi * math.pow(radius,2)

perimeter_rect = 2 * (length + breadth)
perimeter_circ = 2 * math.pi * radius

volume_rect = length * breadth * height
volume_circ = (4/3) * math.pi * math.pow(radius,3)

# for RECTANGLE
print(f"The area of rectangle is: {area_rect} m²")
print(f"The perimeter of rectangle is: {perimeter_rect} m")
print(f"The volume of rectangle is: {volume_rect} m³")

# for CIRCLE
print(f"The area of circle is: {area_circ} m²")
print(f"The perimeter of circle is: {perimeter_circ} m")
print(f"The volume of circle is: {volume_circ} m³")


