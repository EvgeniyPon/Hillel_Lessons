# palindrome
string = input("write whatever you want: ")
result = string == string[::-1]

# list to string & to list
list_1 = ['Hillel', 'AQA', 'TEST']
list_to_str = list_1[0] +', ' + list_1[1] +', ' + list_1[2]
str_to_list = list_to_str.split(', ')


# Sort list
list_1 = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
list_1.sort(key=str.lower)


# List inside of list
list_1 = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
list_win = list_1[6][3][0].split(',')


# Sorted list
list_1 = ['8', 'a', 'f', '4', 'A', 'J', '1']
sort_check = list_1 == sorted(list_1)

