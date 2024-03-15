# letters to delete
string = input("write whatever you want: ")
letter = input("Enter the letter you want to delete: ")
result = string.replace(letter, "")
print("Result:", string)


# Title
string = input("write whatever you want: ")
print(f'Titled string is: - {string.title()}')


# Revers
string = input("write whatever you want: ")
print(f'Reversed string is: - {string[::-1]}')


#Comparison
string_1 = input("write your first string: ")
string_2 = input("write your second string: ")
if string_1 == string_2:
    print('Strings are same')
else:
    print('Strings are different')



#Repeated string
string = input("write whatever you want: ")
repeat_count = int(input('Write number for repeat:'))
result = string * repeat_count
print(f'Repeated string is - {result}')


#Currency exchenge at 14.03.2024
usd_to_uah = 38.74
uah_to_usd = 0.026
eur_to_uah = 42.39
uah_to_eur = 0.024

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the input currency (UAH, USD, EUR): ")
to_currency = input("Enter the currency to exchange (UAH, USD, EUR): ")

if from_currency == "UAH" and to_currency == "USD":
    result = int(amount * uah_to_usd)
    print(f"{amount} UAH = {result} USD")
elif from_currency == "USD" and to_currency == "UAH":
    result = int(amount * usd_to_uah)
    print(f"{amount} USD = {result} UAH")
elif from_currency == "UAH" and to_currency == "EUR":
    result = int(amount * uah_to_eur)
    print(f"{amount} UAH = {result} EUR")
elif from_currency == "EUR" and to_currency == "UAH":
    result = int(amount * eur_to_uah)
    print(f"{amount} EUR = {result} UAH")
else:
    print("Input error")

