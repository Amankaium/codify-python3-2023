from random import randint


class LotoNum:
    found = False

    def __init__(self):
        self.my_num = randint(1, 100)
    # необходимо создать свойство my_num, используя библиотеку random
    # число my_num и есть загаданное число

    def check(self, num):
        if self.found:
            print("Число уже найдено")
            return 0
            # вывести что число уже найдено и вернуть 0

        # далее вам надо разобрать 3 варианта:
        # когда num больше загаданного числа, должен вызываться метод more;
        # когда num меньше загаданного числа, должен вызываться метод less;
        # когда num равен загаданному числу, должен вызываться метод win
        if self.my_num > num:
            self.more()
        elif self.my_num < num:
            self.less()
        else:
            self.win()

    def win(self):
        # поменять значение свойства found на True и вывести "ВЕРНО!"
        self.found = True
        print("Верно")

    def more(self):
        # Вывести "Загаданное число больше"
        print("Загаданное число больше")

    def less(self):
        # Вывести "Загаданное число меньше"
        print("Загаданное число меньше")


# Код ниже нужен для проверки
num_1 = LotoNum()
while True:
    input_num = int(input())
    num_1.check(input_num)
    if num_1.found:
        break
num_1.check(input_num)
