'''
Name: Luke Tye
Date: 9/7/23
Description:
This is my Unit 1 Coding Final Project. These are the objectives:

Write a program named geometry_fun.py which prompts a user for a positive whole number and outputs the following:

The perimeter and area of a square whose side len
eq_triangle_height = (1/2(math.sqrt (3 * positive_number)))gth is the entered number
The radius, circumference, and area of a circle whose diameter is the entered number
The perimeter and area of an equilateral triangle whose side length is equal to the entered number.
The program will use the command line for its input and output (I/O). 
'''
import math

PI = 3.1416
positive_number = int(input("Give a whole, positive number: "))
number_of_sides = int(input("Give a whole, positive number of sides: "))
positive_radius = int(positive_number / 2)

square_peri = (positive_number * 4)
square_area = (positive_number * 2)
circle_radius = (positive_number / 2)
circle_circumference = (positive_number * PI)
circle_area = PI * math.pow(positive_radius, 2)

eq_triangle_perimeter = (positive_number * 3)
eq_triangle_height = (1/2*(math.sqrt(3 * positive_number)))
eq_triangle_area = (math.sqrt(3/4) * math.pow(positive_number,2))

polygon_apothem = positive_number/(2 * 2(math.tan) * (180/number_of_sides))
polygon_peri = positive_number * number_of_sides
polygon_area = (1/2) * (polygon_apothem * polygon_apothem)

print ("A square with a side length of", round(positive_number, 3))
print ("\t Has a perimeter of", round(square_peri, 3))
print ("\t Has a area of", round(square_peri, 3))

print ("A circle with a diameter of", round(positive_number, 3))
print ("\t Has a radius of", round(circle_radius, 3))
print ("\t Has a circumference of", round(circle_circumference, 3))
print ("\t Has an area of", round(circle_area, 3))

print ("An equilateral triangle with a side length of", round(positive_number, 3))
print ("\t Has a perimeter of", round (eq_triangle_perimeter, 3))
print ("\t Has an area of", round (eq_triangle_area, 3))

print ("A normal polygon with the side number of", number_of_sides + "and the side length of ", positive_number)
print ("\t Has a apothem of", round (polygon_apothem, 3))
print ("\t Has a perimeter of", round (polygon_peri, 3))
print ("\t Has a area of", round(polygon_area, 3))


