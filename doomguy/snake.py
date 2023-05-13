from lib import *

m = SnakeMap(10)
game = Game()
game.current_map = m
snake = Snake(name="Python", x=2, y=3, currrent_map=m)
fruit_1 = Fruit(name="Apple", x=5, y=3, currrent_map=m)
fruit_2 = Fruit(name="Banana", x=7, y=3, currrent_map=m)

while True:
    m.render()
    command = input()
    # snake.move(command)
    snake.move_right()
    # print(snake.short_name)
    # print(m.box)

