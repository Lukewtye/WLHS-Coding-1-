'''
Name: Luke Tye
Date: 10/11/23
Assignment: Prompt a user for two integers called 
m and n and use those numbers to create an m x n multiplication table. 
'''
print("Luke Tye")
m = (int(input("Enter Row Length ")))
n = (int(input("Enter Column Length ")))
for m in range (m):
    m = m +1
    for n in range (n):
        n = n +1
        print(m*n, end = '\t')
    print('')
#M = Row
#N = Column