import os
import csv

# Task_1 copy from file
new_txt_file = '/Users/a123/PycharmProjects/Hillel_Lessons/Lesson_9_files/file_2.txt'
with open('/Users/a123/PycharmProjects/Hillel_Lessons/Lesson_9_files/file_1.txt', 'r', encoding='utf-8') as file_from:
    with open(new_txt_file, 'w+', encoding='utf-8') as file_into:
        print(f'at this moment second file is empty - {file_into.read()}')
        file_into.seek(0)
        file_into.writelines(file_from)
        file_into.seek(0)
        print(f'and now file is filled with data - {file_into.read()}')

# Task_2 csv files
with open('/Users/a123/PycharmProjects/Hillel_Lessons/Lesson_9_files/names.csv', 'r', newline='', encoding='utf-8') as names:
    csv_reader = csv.DictReader(names)
    new_csv_file = '/Users/a123/PycharmProjects/Hillel_Lessons/Lesson_9_files/emails.csv'
    with open(new_csv_file, 'w', newline='', encoding='utf-8') as emails:
        csv_writer = csv.DictWriter(emails, fieldnames=['email'])
        csv_writer.writeheader()
        for i in csv_reader:
            del i['first_name']
            del i['last_name']
            csv_writer.writerow(i)

# Task_3 try/except
course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
key = input('Plase enter your key: ')
try:
    value = course[key]   
except KeyError:
    print(f'Error: The specified key "{key}" does not exist in the dictionary.')
else:
    print(f'value of your key "{key}" is - {value}')
finally:
    print('End')      

