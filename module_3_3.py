# Домашнее задание по уроку "Распаковка позиционных параметров".
# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
print('1.Функция с параметрами по умолчанию:')

def print_params(a=1, b='строка',c= True):
    print(a, b, c)


print_params()
print_params(a= 'string', b= False, c=15)
print_params('Green', 35)

print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:
print('2.Распаковка параметров:')

values_list = [25,'hello',False]
values_dict = {'a': 25, 'b': 'Apple', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
print('3.Распаковка + отдельные параметры:')

values_list_2 = [54.32,'Строка']
print_params(*values_list_2, 42)

