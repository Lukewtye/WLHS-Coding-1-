#Swapping w tuples
a = 5
b = 10
print(f"a: {a}, b: {b}")

(a,b) = (b,a)
print(f"a: {a}, b: {b}")

# assigning multiple values at once

c,d = 15,20
print(f"c: {c}, d: {d}")

#enumeration

nfc_north = ['Lions', 'Vikings', 'Packers','Bears']
enum_list = enumerate(nfc_north)
for index, team in enum_list:
    print(f"Team {index+1}: {team}")

# limitations of nesting lsits and tuples 

my_list = [1,2,(3,4)]
print(my_list[2][1])
#valid
my_list[1] = -2
print(my_list)
#valid

#my_list = [2][0] = -3
#INVALID

#valid
my_list[2] = 3
print(my_list)
#TO DO HOMEWORK FOR TUESDAY
8.3.6
8.3.8
8.3.9
