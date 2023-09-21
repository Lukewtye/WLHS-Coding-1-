user_number = int(input("Enter your favorite number: "))

match user_number % 2:
    case 0:
        print ("even")
    case 1:
        print ("odd")
    case _:
        print ("NaN")


match user_number:
    case 1:
        print ("Boring")
    case 2:
        print ("Interesting, first prime!")
    case 3: 
        print ("Totally agree!")
    case _:
        print ("What a bad choice!")

#You could make all of this using if and else's but this is an alternative.