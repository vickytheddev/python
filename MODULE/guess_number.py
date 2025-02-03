import random
cnumber=random.randrange(1,101)
userinput=int(input("Guess a number:"))
if userinput>cnumber:
    print("your gauss number is high")
elif cnumber>userinput:
    print("your gauss number is less")
else:
    print("your gauss number is equal")