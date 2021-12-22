import string
import random

list_s = string.ascii_letters + string.digits
result_list = random.sample(list_s, 10)
print("Список из случайных 10 символов:", result_list, sep='\n')
