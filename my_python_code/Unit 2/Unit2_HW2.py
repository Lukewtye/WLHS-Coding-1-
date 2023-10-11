'''
Name: Luke Tye
Date: 9/21/23
Assignment: Unit 2 Homework 2 
'''

print ("Luke Tye")

#Exercise 1:
stick_1 = input(int())
stick_2 = input(int())
stick_3 = input(int())

if stick_1 > stick_2 + stick_3:
    print ("No")
elif stick_2 > stick_1 + stick_3:
    print ("No")
elif stick_3 > stick_1 + stick_2:
    print ("No")
else: 
    print ("Yes")