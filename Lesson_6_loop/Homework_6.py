# Task_1 divide by a given number
my_list = [1, 2, 2623, 4658, 7567, 6673, 3, 5674, 77739, 8, 6785, 771, 882, 15, 339, 222, 1456, 1]
num = int(input('write the number you want to divide by: '))
result = list()
for i in my_list:
    if i % num == 0:
        result.append(i)
print(result)


# Task_2 sequence in the list
my_list = [1, 2, 3, 4, 6, 7, 8]
index_of_list = 0
result = list()
first_num = my_list[index_of_list]
next_num = my_list[index_of_list + 1]
while next_num == first_num + 1:
    index_of_list += 1
    first_num = my_list[index_of_list]
    next_num = my_list[index_of_list + 1]
    if next_num != first_num + 1: 
        result.append(next_num)
print(f'First unsequenced number is {result[0]}')


# Task_3 cycle pyramid
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 



