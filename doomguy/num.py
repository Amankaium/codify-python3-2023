from random import randint


class LotoNum:
    found = False

    def __init__(self):
        self.num = randint(1, 100)

    def check(self, num):
        if self.found:
            print("Число уже найдено")
            return 0

        if num == self.num:
            self.found = True
            print("ВЕРНО!")
        elif num > self.num:
            return self.less()
        else:
            return self.more()

    def more(self):
        print("Загаданное число больше")

    def less(self):
        print("Загаданное число меньше")


my_num = LotoNum()
while True:
    input_num = int(input())
    my_num.check(input_num)
    if my_num.found:
        break

my_num.check(input_num)
