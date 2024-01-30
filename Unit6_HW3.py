'''
Name: Luke Tye
Assignment: Unit 6 Homework 3
Date: 1/19/23
'''
print("Luke Tye")
def print_reverse(string):
    """'
    Reverses the submitted string
    Parameters
    ----------
    string: str
        The string you want reversed

    Returns
    Reversed string, each letter on a new line
    """
    string = string[::-1]
    for letter in string:
        print (letter)

def unique(L):
    """
    Returns the unique elements in L
    Parameters: 
    L is a list
    Returns:
    L, with only the unique elements and with a unmuted list
    """
    elemental_list = []
    for element in L:
        if element not in elemental_list:
            elemental_list.append(element)
    print (elemental_list)

#Calls
print(print_reverse("Suzanne Tye"))
test_list = [1,1,1,1,2,2,2,2,3,4]
unique(test_list)