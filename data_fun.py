'''
Name: Luke Tye
Date: 9/25/23
Description: Ask user for favorite integer and character and print out a variety of information
regarding those numbers.

FOr upper and lowercase and numbers: user
.isupper()
.islower()
.isnumeric()
.isnumeric() (single number)
'''

#Part 1:
integer = int(input("What's your favorite integer? "))
if integer < 0:
    print ("This integer is negative.")
else:
    print ("This integer is positive")
if integer <10 and integer > 100:
    print ("This integer is greater than 10 ")
elif integer <100 and integer > 1000:
    print ("This integer is greater than 100 ")
elif integer <1000: 
    print ("This number is greater than 1000")
else: print ("This number is smaller than 10")
#Odd or even:
if (integer % 2) == 0:
    print ("This number is even.")
else: 
    print ("This number is odd.")
#Noble Gasses Matching
match integer: 
    case 2:
        print ("This is the Noble Gas Helium!")
    case 10:
        print ("This is the Noble Gas Neon!")
    case 18:
        print ("This is the Noble Gas Argon!")
    case 36:
        print ("This is the Noble Gas Krypton!")
    case 54:
        print ("This is the Noble Gas Xenon!")
    case 86:
        print ("This is the Noble Gas Radon!")
    case 118:
        print ("This is the Noble Gas Oganesson!")
    case _:
        print ("This is not one of the Noble Gasses.")
    