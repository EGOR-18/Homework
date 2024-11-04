def personal_sum(numbers):
    sum = 0
    incorrect_data = 0
    for num in numbers:
        try:
            sum += num
        except:
            incorrect_data += 1
    return sum, incorrect_data

def calculate_average(numbers):
    count = 0
    try:
        for num in numbers:
            try:
                if isinstance(num, int or float):
                    count+=1
                else:
                    raise TypeError
            except TypeError:
                print(f"Некорректный тип данных для подсчёта суммы - {num}")
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


    try:
        rez = personal_sum(numbers)[0] / count
        return rez
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать