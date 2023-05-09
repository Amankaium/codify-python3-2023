from random import randint


class Game:
    current_map = None
    # def __init__(self):
        # self.start_game()


    def start_game(self):
        self.current_map = Map(20)


class Map:
    units = []

    def __init__(self, size=20):
        self.height = int(size / 2)
        self.width = size * 2
        self.create_map()
        self.create_box()
        # self.start_game()

    def create_box(self):
        box = []
        box.append([])
        for i in range(self.width):
            box[0].append("#")

        for i in range(self.height-2):
            box.append([])
            box[-1].append('#')
            for j in range(self.width-2):
                box[-1].append(' ')
            box[-1].append('#')

        box.append([])
        for i in range(self.width):
            box[-1].append("#")
        self.box = box

    def render(self):
        for row in self.box:
            for pixel in row:
                print(pixel, end="")
            print()

    def show_box(self):
        for row in self.box:
            print(row)

    def create_map(self):
        print("#" * self.width)
        for i in range(self.height):
            print(f"#{' ' * (self.width - 2)}#")
        print("#" * self.width)

    def add_unit(self, unit_object):
        self.units.append(unit_object)
        y = unit_object.y
        x = unit_object.x
        self.box[y][x] = unit_object


class Unit:
    def __init__(self, **kwargs):  # пренадлежность
        # name, x, y, current_map is required
        self.name = kwargs["name"]
        self.short_name = kwargs["name"].upper()[0]
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.current_map = kwargs["currrent_map"]
        self.current_map.add_unit(self)

    def __str__(self):
        return self.short_name

    def move_up(self):
        self.current_map.box[self.y][self.x] = " "
        self.y -= 1
        self.current_map.box[self.y][self.x] = self.short_name

    def move_right(self):
        self.current_map.box[self.y][self.x] = " "
        self.x += 1
        self.current_map.box[self.y][self.x] = self.short_name


class Player(Unit):
    def move(self, button):
        if button == "w":
            self.move_up()
        elif button == "d":
            self.move_right()


class Snake(Player):
    def move(self, button):
        fruits = []
        for unit in self.current_map.units:
            if isinstance(unit, Fruit):
                fruits.append(unit)
        if button == "d":
            next_x = self.x + 1
            next_y = self.y
        # TODO

        eat = False
        for fruit in fruits:
            if fruit.x == next_x and fruit.y == next_y:
                eat = True

        if eat:
            ln = len(self.short_name)
            self.short_name = self.name.upper()[:ln+1]
        else:
            super().move(button)





class Bot(Unit):
    def do_something(self):
        num = randint(1, 2)
        if num == 1:
            self.move_up()
        elif num == 2:
            self.move_right()

class Fruit(Unit):
    weight = 1