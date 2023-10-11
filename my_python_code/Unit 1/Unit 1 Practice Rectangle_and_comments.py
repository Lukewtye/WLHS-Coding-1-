'''
Name: Luke Tye, 9/7/23 
Assignment: Rectangle and Comments Practice
Description: This Program will ask a user for a length and width, then calculate the area and 
perimeter and print both. 
Pseudocode:
Ask user for length and store in rect_length (float)
Ask user for width and store in rect_width (float)
Calculate the area (length * width)
Store in rect_area
Calculate the perimeter ((length + width) *2)
Store in rect_perimeter
Print area & perimeter
'''
rect_length = (float(input("Give a length for a rectangle in feet")))
rect_width = (float(input("Give a width for a rectangle in feet")))
rect_area = rect_length * rect_width
rect_perimeter = (rect_width + rect_length) * 2 

print ("This is the area of a rectangle with that area:", rect_area, "in inches")
print ("This is the perimeter:", rect_perimeter, "in inches")

