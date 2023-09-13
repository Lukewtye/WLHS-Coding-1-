import math

##Test: IF I put in a height of 5 and a radius of 6, I should get a volume of 565.49

PI = 3.1416
cyl_height = int(input("Height of cylinder: "))
cyl_rad = int(input("Radius of cylinder: "))

area_of_base = (PI*cyl_rad**2)
volume_of_cyl = area_of_base * cyl_height
print ("Volume is", round(volume_of_cyl, 3))