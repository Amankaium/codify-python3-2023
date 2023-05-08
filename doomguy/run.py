from lib import *
from time import sleep

map_1 = Map(20)
map_2 = Map(10)
game = Game()
game.current_map = map_1
unit_1 = Unit(name="Alan", x=1, y=1, currrent_map=map_1)
unit_2 = Unit(name="Bob", x=2, y=2, currrent_map=map_1)
unit_3 = Unit(name="Doomguy", x=4, y=5, currrent_map=map_1)

while True:
    map_1.render()
    command = input()
    if command == "w":
        unit_3.move_up()
    sleep(1)
