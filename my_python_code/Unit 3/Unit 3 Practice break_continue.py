
x = int(input("number: "))

while True:
    x = int(input("Number: "))
    if x > 0:
        break
    else: 
        continue
    print("Error: Must be positive")
print("you chose ", x)

for i in range(4):
    if i == 7:
        break
    else:
        continue
print("you found 7")

for i in range(6):
    print(str(i) + "", end = "-")