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

# Task_2 add dictionary to string
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
result_link = initial_str
for key, values in params.items():
    result_link += f'{key}={values}&'
result_link = result_link[:-1:]
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

