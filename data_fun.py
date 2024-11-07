"""
Name: Luke Tye
Date: 9/25/23
Description: Ask user for favorite integer and character and print out a variety of information
regarding those numbers.

"""
integer = int(input("What's your favorite integer? "))
if integer < 0:
    print("\tThis integer is negative.")
else:
    print("\tThis integer is positive")

if 10 < integer <= 100:
    print("\tThis integer is greater than 10")
elif 100 < integer <= 1000:
    print("\tThis integer is greater than 100")
elif integer > 1000:
    print("\tThis number is greater than 1000")
else:
    print("\tThis number is smaller than 10")

if integer % 2 == 0:
    print("\tThis number is even.")
else:
    print("\tThis number is odd.")

match integer:
    case 2:
        print("\tThis is the Noble Gas Helium!")
    case 10:
        print("\tThis is the Noble Gas Neon!")
    case 18:
        print("\tThis is the Noble Gas Argon!")
    case 36:
        print("\tThis is the Noble Gas Krypton!")
    case 54:
        print("\tThis is the Noble Gas Xenon!")
    case 86:
        print("\tThis is the Noble Gas Radon!")
    case 118:
        print("\tThis is the Noble Gas Oganesson!")
    case _:
        print("\tThis is not one of the Noble Gasses.")

user_character = input("Give me your favorite character ")
print(user_character)

if user_character.isdigit():
    print("\tYour character is a numeric digit.")
elif user_character.islower():
    print("\tYour character is a lowercase letter")
    if user_character in "aeiou":
        print("\tIt's a lowercase vowel")
    else:
        print("\tIt's a consonant.")
elif user_character.isupper():
    print("\tYour character is an uppercase letter")
    if user_character in "AEIOU":
        print("\tIt's an uppercase vowel")
    else:
        print("\tIt's a consonant.")
else:
    print("\tInvalid input.")

ascii_value = ord(user_character)
print("\tThe ASCII value of user_character is " + str(ascii_value))

if user_character.islower() or user_character.isupper():
    letter_position = ord(user_character) - ord("A") + 1
    if letter_position == 1:
        suffix = "st"
    elif letter_position == 2:
        suffix = "nd"
    elif letter_position == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(
        "\tAnd it is the " + str(letter_position) + suffix + " letter of the alphabet."
    )
