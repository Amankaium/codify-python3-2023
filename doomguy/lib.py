class Map:
    def __init__(self, size=20):
        self.height = int(size / 2)
        self.width = size * 2
        self.create_map()
        self.create_box()
        self.start_game()

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

    def start_game(self):
        self.x = round(self.width / 2)
        self.y = round(self.height / 2)
        self.box[self.y][self.x] = "O"

    def move_up(self):
        self.box[self.y][self.x] = " "
        self.y -= 1
        self.box[self.y][self.x] = "O"
