import random
import time

'''
Name: Luke Tye
Date:10/20/23
Assignment: A text based game using functions
'''

def display_intro():
    """Prints an intro to the game
    
    Parameters: none
    Returns: none
    """
    print()
    print('''You are in a land full of dragons. In front of you, 
you see two caves. In one cave, the dragon is friendly 
and will share his treasure with you. The other dragon 
is greedy and hungry,and will eat you on sight.''')
    print()

def choose_cave():
    """Asks a user to choose the cave they want to enter 
    it will prompt them until they enter 1 or 2.
    s
    Parameters: None
    Return: cave - the cave they chose 
    """
    cave = ''
    while cave != "1" and cave != '2':
        print("Which cave will you do into? (1 or 2)")
        cave = input()
    return cave 

def check_cave(choose_cave):
    """Determines if the user is eaten or not based on
    their cave choice

    Parameters
    ----------
    choose_cave: string
        the cave the user chose
    
        Returns
        -------
        none
        """
    print("You approach the cave...")
    time.sleep(2)
    print("It's dark and spooky...")
    time.sleep(2)
    print('''A large dragon jumps out in front of you!
    He opens his jaws and...''')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if choose_cave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print("gobbles you down in one bite!")
    




#Function Calls
play_again = "yes"

while play_again.lower() == "yes":
    display_intro()
    user_cave = choose_cave()
    check_cave(user_cave)

    print("Do you want to play again? (yes or no)")
    play_again = input()
display_intro()
choose_cave()
