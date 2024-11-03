def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print("Вызов без аргументов:")
print_params()

print("\nВызов с одним аргументом:")
print_params(10)

print("\nВызов с двумя аргументами:")
print_params(10, 'новая строка')

print("\nВызов с изменением b:")
print_params(b = 25)

print("\nВызов с изменением c:")
print_params(c=[1, 2, 3])

values_list = [3.14, 'пример строки', False]
values_dict = {'a': 42, 'b': 'словарь', 'c': None}

print("\nРаспаковка списка и словаря:")
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print("\nРаспаковка второго списка с добавлением отдельного параметра:")
print_params(*values_list_2, 42)