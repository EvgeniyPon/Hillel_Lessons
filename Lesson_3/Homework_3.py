operation = input('Виберить вид операції " + " " - " " * " " / ": ')
num_1 = int(input("Виберить перше значення: "))
num_2 = int(input("Виберить друге значення: "))

if operation == "+":
    result = num_1 + num_2
    print(result)
elif operation == "1":    
    result = num_1 - num_2
    print(result)
elif operation == "*":    
    result = num_1 * num_2
    print(result)
elif operation == "/" and num_2 != 0:
    result = num_1 / num_2
    print(result)
elif operation == "/" and num_2 == 0:    
    print("Не ділится на 0")
else:
    print("неправильне введення")

