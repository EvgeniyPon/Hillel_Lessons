# Task_1 calc by def
operation = input('Choose type of operation " + " " - " " * " " / ": ')
num_1 = (input("Enter first number: "))
num_2 = (input("Enter second number: "))
errors = []
def input_check(operation, num_1, num_2):
    global errors
    try:
        num_1 = float(num_1)
    except ValueError:
        errors.append(f'({num_1}) is not a calculated type')
    try:
        num_2 = float(num_2)
    except ValueError:
        errors.append(f'({num_2}) is not a calculated type')
    if operation == "/" and num_2 == 0:
        errors.append('Error: division by zero!')
    if operation not in ["+", "-", "*", "/"]:
        errors.append(f'this ({operation}) is not an operator in the math')
input_check(operation, num_1, num_2)
if not errors:
    def calc(num_1, num_2, operation):
        if operation == "+":
            return num_1 + num_2
        elif operation == "-":
            return num_1 - num_2
        elif operation == "*":
            return num_1 * num_2
        elif operation == "/" and num_2 != 0:
            return num_1 / num_2
    result = calc(float(num_1), float(num_2), operation)
    print(f'Result of {num_1} {operation} {num_2} = {result}')
else:
    for error in errors:
        print(error)


# Task_2 prime number
import random
play = True
while play:
    num = random.randint(2, 1000)
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    result = is_prime(num)
    if result is True:
        print(f'the {num} is a prime number')
    else:
        print(f'the {num} is not a prime number')
    request = input('Do you want check one more time? yes (y) or no (n) ')
    def again(request):
        if request.lower() == 'y':
            play = True
        elif request.lower() == 'n':
            play = False
        return play
    play = again(request)