# # Task_1 divide by a given number
# my_list = [1, 2, 2623, 4658, 7567, 6673, 3, 5674, 77739, 8, 6785, 771, 882, 15, 339, 222, 1456, 1]
# num = int(input('write the number you want to divide by: '))
# result = list()
# for i in my_list:
#     if i % num == 0:
#         result.append(i)
# print(result)


# # Task_2 sequence in the list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(1, len(my_list)):
#     if my_list[i-1] + 1 != my_list[i]:
#         print(f'First unsequenced number is {my_list[i]}')
#         break    
#     if i + 1 == len(my_list):
#         print('This list is sequenced!')
        

# # Task_3 cycle pyramid
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print() 


a = [1, 2, 3, 5, True, False, 'test']
a.sort()
print(a)

