"""
Name: Luke Tye
Assignment: While Loops practice 
Date: 9/29/23
Pseudocode:

WElcome user
get user choice
get computer choice
determine win, loss, tie
print thanks for playing
"""
import random

print("Welcome, User!")
print("Pick rock, paper, or scissors: ")
user_choice = ""
while user_choice != "rock" and user_choice != "scissors" and user_choice != "paper":
    print ("Please select rock, paper, or scissors: ")
    user_choice = input(">").lower()
random_int = random.randint(1,3)
computer_choice = ""
if random_int == 1:
    computer_choice = "paper"
elif random_int == 2:
    computer_choice = "rock"
elif random_int == 3:
    computer_choice = "scissors"
else:
    computer_choice = "Invalid"
print ("The computer chose", computer_choice)

if user_choice == "rock" and computer_choice == "scissors":
    print("User wins!")
elif user_choice == "paper" and computer_choice == "rock":
    print("User wins!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("User wins!")
elif user_choice == "scissors" and computer_choice == "scissors":
    print("Tie! Play again?")
elif user_choice == "paper" and computer_choice == "paper":
    print("Tie! Play again?")
elif user_choice == "rock" and computer_choice == "rock":
    print("Tie! Play again?")
else:
    print("Computer wins!")
