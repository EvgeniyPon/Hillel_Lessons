# Task_1_Class
# class Company:
#     def __init__(self, name, industry, location, founder, founded_year):
#         self.name = name
#         self.industry = industry
#         self.location = location
#         self.founder = founder
#         self.founded_year = founded_year
#
#     def __str__(self):
#         return (f'Company: {self.name}\nIndustry: {self.industry}'
#                 f'\nLocation: {self.location}\nFounder: {self.founder}\nFounded year: {self.founded_year}')

# Task_2_*args
from my_max import *
from my_min import *
if __name__ == '__main__':
    nums = input('Enter numbers separated by spaces: ').split()
    nums = list(nums)
    max_value = my_max(*nums)
    min_value = my_min(*nums)
    print(f'MAX = {max_value}')
    print(f'MIN = {min_value}')




