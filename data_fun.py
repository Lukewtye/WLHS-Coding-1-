'''
Name: Luke Tye
Date: 9/25/23
Description: Ask user for favorite integer and character and print out a variety of information
regarding those numbers.
'''

#Part 1:
integer = int(input("What's your favorite integer? "))
if integer < 0:
    print ("This integer is negative.")
else:
    print ("This integer is positive")
if integer <10 and > 100:
    print ("This integer is greater than 10 ")
elif integer <100 and > 1000:
    print ("This integer is greater than 100 ")
elif integer <1000: 
    print ("This number is greater than 1000")
else: print ("This number is smaller than 10")