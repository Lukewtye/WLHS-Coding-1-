'''
Name: Luke Tye
Date: 9/20/23
Assignment: This is my Unit 2 HW1 project.
'''
print ("Luke Tye")
#Exercise 1:
number_of_os = int(input())
letters = "o" * number_of_os
spooky = ("sp" + letters + "ky")
if number_of_os >= 2 and number_of_os <= 20:
    print (spooky)
else:
    print ("enter a valid integer")

#Exercise 2:
month_number = int(input())
date = int(input())
if (month_number <=2 or month_number <=1) and date < 18:
    print ("Before")
if month_number ==2 and date == 18:
    print ("Special")
if (month_number >=2 or month_number >1) and date < 18:
    print ("After")