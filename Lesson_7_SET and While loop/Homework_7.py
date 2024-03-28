# Task_1 unique & common elements in 2 lists
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
first_set = set(first)
second_set = set(second)
intersection_set = first_set & second_set
print(f'unique & common elements in 2 lists is {intersection_set}')

# Task_2 mismatch in list_1 compare with list_2
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
first_set = set(first)
second_set = set(second)
difference_set_1 = first_set - second_set
print(f'mismatch in list_1 compare with list_2 is {difference_set_1}')

#Task_3 unique element in list
import random
random_list = []
for _ in range(1, 20):
    random_list.append(random.randint(1, 1000))
if len(random_list) == len(set(random_list)):
    print(f'the list contains only unique items \nList = {random_list} \nSet = {set(random_list)}')
else:
    print(f'some list items are duplicated \nList = {random_list} \nSet = {set(random_list)}')

# Task_4  minimum value in list
elements = [1, 5, 68, 0]
min_value = elements[0]
for value in elements:
    if value < min_value:
        min_value = value
print(f'min value in list is -  {min_value}')

# Task_5 summ of elements in list
elements = [1, 5, 68, 0]
summ_elements = 0
index = 0
while index < len(elements):
    summ_elements += elements[index]
    index += 1
print(summ_elements)
