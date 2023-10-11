'''
Unit 1 Project Pseudocode
Name: Luke Tye
Date: 9/7/23
Description: This is Pseudocode for my Unit 1 Project: 
Objectives for project: 
Write a program named geometry_fun.py which prompts a user for a positive whole number
 and outputs the following:
The perimeter and area of a square whose side length is the entered number
The radius, circumference, and area of a circle whose diameter is the entered number
The perimeter and area of an equilateral triangle whose side length is equal to the entered number.
The program will use the command line for its input and output (I/O). 

Technical Details:
PI should be declared as a constant with 5 digits of precision: 3.1416.
User input (the whole number) should be stored in an int.
Results of all computations should be stored in variables (dont do calculations and output 
at the same time).
Program should use integer math when appropriate and floating point math when appropriate.
The program should demonstrate the use of the tab character (\t)
The program should demonstrate the use of the pow() and sqrt() functions.
Decimal numbers should be output with 3 digits after the decimal point

Pseudocode:
input math
PI = 3.1416
Prompt user for a positive whole number 
Store number as positive_number (STORE AS INT)
Store 1/2 number as positive_radius (Store as INT)
Calculate perimeter of the square with a side of positive_number  (positive number * 4)
Store as square_perimeter
Calculate area of the square with a side length of positive_number (positive number * 2)
Store as square_area
Calculate radius of circle with a diameter of positive_number (positive number / 2)
Store as circle_radius
Calculate the circumfrence of a circle with a diameter of positive_number (positive number * PI)
Store as circle_circumfrence
Calculate the area of a circle with the diameter of positive_number (PI * pow(positive_radius 2))
(CHECK HOW TO USE POW)
Store area of circle as circle_area
Calculate the perimeter of equilateral triangle with the side length of positive_number 
(positive_number * 3)
Store the perimeter as eq_triangle_perimeter
Calculate the height of an equilateral triangle w side length of positive_number
(1/2 (sqrt(3 * positive_number)))
Store as eq_triangle_height
Calculate the area of a equilateral triangele with the side length of postitive_number
(sqrt(3/4) * pow(positive_number 2 ))
Print the perimeter and area of the square
Print the radius and circumference and area of the circle
Print the perimeter and height and area of the eq triangle
'''
