import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
rez = list(map(lambda f, s: f == s, first, second))
print(rez)


def  get_advanced_writer(file_name):
    def write_everything(*data_set):
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                for elem in data_set:
                    file.write(str(elem) + "\n")
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())