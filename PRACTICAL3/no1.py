def check_armstrong(number):
    num_str = str(number)  
    num_digits = len(num_str)
    
    armstrong_sum = 0
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    
    return armstrong_sum == number

num = int(input("Enter a number: "))
if check_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

