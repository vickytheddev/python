a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

count= 0
max= None

if a % 2!= 0:
    count += 1
    max = a

if b % 2 != 0:
    count += 1
    if max is None or b > max:
        max = b

if c % 2 != 0:
    count += 1
    if max is None or c > max:
        max = c

print(f"Count of odd numbers: {count}")
if max is not None:
    print(f"Maximum odd number: {max}")
else:
    print("Anyone is not odd number")




