PI = 3.1415
radius = float(input("Enter the radius of a sphere "))
vol_of_sphere = 4/3 * PI * (radius ** 3)
print ("The Volume of a sphere with that radius is",vol_of_sphere)


PRICE_PER_BOOK = 24.95
SHIPPING_COST = .75
INITIAL_SHIPPING_COST = 3
Copies = float(input("How many copies would you like to buy?"))
total_cost = ((Copies * 24.95)*0.4) + (SHIPPING_COST * Copies + 3)
print ("Your total cost is $",total_cost)