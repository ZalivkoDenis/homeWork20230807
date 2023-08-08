# ШАГ. Д/з по сроку 07/08/2023 © Денис Заливко

from string import String
from list import List

my_str = String("Hellow world! I'm Denis!")
print(my_str)
print(my_str.is_include('world!'))
my_str.replace('Denis', 'Alexandr')
print(my_str)


my_str.replace('Alexandr', 'Denis')
my_list = List(str(my_str).split())
print(my_list)
print(my_list.is_include('Denis!'))
my_list.add('STEP')
print(my_list)
print(f'List length = {my_list.length()}')




