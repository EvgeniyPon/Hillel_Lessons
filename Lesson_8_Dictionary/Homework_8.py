# Task_1 Hello Mr. key
roles = { 'admin' : ['Evgeniy', 'Dmitry', 'asd'], 'maintainer' : ["Marina", "Sergey"],
          'manager' : ["Anastasia", "Dmitry", 'asd'], 'developer': ["Evgeniy"]}
name = input('What is yor name?')
name_roles = []
for key, value in roles.items():
    if name in value:
        name_roles.append(key)
if name_roles:
    print(f'Hello, {' & ' .join(name_roles)}!')
else:
    print('Hello, Guest!')
                                  # Marina's solution
#                                 name = input('Please, enter your name: ').title()
#                                 roles_dict = {'admin' : ['Evgeniy', 'Dmitry', 'asd'], 'maintainer' : ["Marina", "Sergey"],
#                                           'manager' : ["Anastasia", "Dmitry", 'asd'], 'developer': ["Evgeniy"]}
#                                 for role, names in roles_dict.items():
#                                     if name in names:
#                                         print(f'Hello, {role}!')
#                                         break
#                                 else:
#                                     print('Hello, Guest!')

# Task_2 add dictionary to string
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
result_link = initial_str
for key, values in params.items():
    result_link += f'{key}={values}&'
#                                 # result_link = result_link[:-1:] OLD DECISION
# Marina's solution
result_link = result_link.strip('&')
print(result_link)

# Task_3 set to dictionary
result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
result_dict = {}
for _key in result_link:
    if _key in result_dict:
        result_dict[_key] += 1
    else:
        result_dict[_key] = 1
print('quantity of repeated symbols:')
row = 0
for key, value in result_dict.items():
    print(f'{key}: {value}', end='\t')
    row += 1
    if row % 5 == 0:
        print()

                                # Marina's solution
                                # result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
                                # dict_count = {}
                                # for element in result_link:
                                #     if element not in dict_count:
                                #         dict_count [element] = result_link. count (element)
                                #         print(f'How many times an element is repeated in a line:\n{dict_count}')

