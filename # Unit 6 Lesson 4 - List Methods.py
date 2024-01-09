# Unit 6 Lesson 4 - List Methods

import random

# count  - returns the number of times something appears
my_list = [1,2,3,1,2, 'a', 'b']
num_twos = my_list.count(2)
print(num_twos)

# append
my_list.append('c') 
print(my_list)

#pop - removes and returns last item from list
my_list.pop()
print(my_list)

#more appending
my_list.append(['a','b','c'])
print(my_list)

#extend - adds list of items to the end of a list 
my_list.pop()
my_list.extend(['a','b','c'])

# .sort () vs sorted(list)
num_list = []
for i in range(20):
    num_list.append(random.randint(1,100))

print(num_list)
sorted_list = num_list.sort()
print(sorted_list)
print(num_list)

num_list2 = []
for i in range(20):
    num_list.append(random.randint(1,100))
sorted_list2 = sorted(num_list2)
print(num_list2)
print(sorted_list2)
    
print("\n"* 3)
my_chars = ['a', 'A', 'b', '$']
print(sorted(my_chars))
