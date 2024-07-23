# Lakeesha King 
# 06/25//20
# P2LAB1
# Assignment tests students knowledge of how to write code that
#performs mathematical calculations and displays information to users

# Import math module to use the constant, math.pi
import math
#get the radius from the user

radius= float(input("what is the radius of the circle? "))
print()
# Calculate the diameter
diameter = 2 * radius
circumference = 2* radius *math.pi
area = math.pi * radius**2
# Display the output
print(f'The diameter of the circle is {diameter:.1f}\n')
print(f'The circumference of the circle is {circumference:.2f}\n')
print(f'The area of the circle is {area:.3f}\n')

input("Press enter to exit")
