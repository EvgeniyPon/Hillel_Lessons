# palindrome 
string = input("write whatever you want: ")
result = string == string[::-1]
print(f'your string is palindrome - {result}')


# list to string & to list corrected
list_1 = ['Hillel', 'AQA', 'TEST']
list_to_str = ', '.join(list_1)
str_to_list = list_to_str.split(', ')
print(f'list to string - {list_to_str} - {type(list_to_str)} \nstring back to list - {str_to_list} - {type(str_to_list)}')



#                   list to string & to list before correction
#                   list_1 = ['Hillel', 'AQA', 'TEST']
#                   list_to_str = list_1[0] +', ' + list_1[1] +', ' + list_1[2]
#                   str_to_list = list_to_str.split(', ')
#                   print(f'list to string - {list_to_str} - {type(list_to_str)} \nstring back to list - {str_to_list} - {type(str_to_list)}')


# # Sort list
list_1 = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
list_1.sort(key=str.lower)
print(f'Sorted list is {list_1}')


# List inside of list corrected
list_1 = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
list_win = list_1[6][3][0]
print(f'New list = {[list_win]}')


#                  List inside of list before correction
#                  list_1 = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
#                  list_win = list_1[6][3][0].split(',')
#                  print(f'New list = {list_win}')


# Sorted list
list_1 = ['8', 'a', 'f', '4', 'A', 'J', '1']
sort_check = list_1 == sorted(list_1)
print(f'This list is sorted - {sort_check}')

