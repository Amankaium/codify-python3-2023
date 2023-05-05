from lib import *
from time import sleep

my_map = Map()
# print(my_map.show_box())
# print(my_map.render())


while True:
    my_map.render()
    command = input()
    if command == "w":
        my_map.move_up()
    sleep(1)
