from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

coincidence = list(map(lambda x, y: x == y, first, second))
print(coincidence)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding = 'utf-8')
        for elem in data_set:
            if type(elem) == str:
                file.write(elem)
                file.write('\n')
            else:
                file.write('[')
                for i in range(len(elem)):
                    file.write(str(elem[i]))
                    if i < len(elem) - 1:
                        file.write(', ')
                    else:
                        file.write(']')
        file.close()
    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)
        print(self.words)
    def __call__(self):
        self.first_ball = choice(self.words)
        return self.first_ball



write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())