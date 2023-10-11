'''
int = 1
while int <11:
    print(str(int) + "", end = " ")
    int = int+1

print ('')

for i in range(1, 10):
    print(str(i) + "", end = "-")
print ("10")

print('')

count = 0
for i in range (2):
    for i in range(6):
        count = count+1
        print(str(count)+" bookshelf")
'''
row = (int(input("Enter Row Length ")))
column = (int(input("Enter Column Length ")))
for row in range (row):
    row = row +1
    for column in range (column):
        column = column +1
        print(row*column, end = '\t')
    print('')
