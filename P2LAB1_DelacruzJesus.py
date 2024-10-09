
#Jesus Delacruz
#October 10, 2024
#P2LAB1
# How to write code that performs mathematical calculations and displays information to users



import math 



# Get the radius from the user

radius = float(input("What is the radius of the circle? "))


# Instructions on how to calculate the diameter, circumference, and the area

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2


# Add up the results with the required data

print(f"\nThe diameter of the circle is {diameter:.1f}\n")


print(f"The circumference of the circle is {circumference:.2f}\n")


print(f"The area of the circle is {area:.3f}")
