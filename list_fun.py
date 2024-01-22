'''
Name: Luke Tye
Assignment: Listfun Project
Date: 1/21/24
'''
def get_data():
    mylist = list()
    int_1 = input("Enter 10 Integers: ")
    mylist.append(int_1)
    for i in range (10):
        int_2 = input("")
        mylist.append(int_2)
    return mylist
mainlist = get_data()
def print_data():
    