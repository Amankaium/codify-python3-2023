from lib import *
from time import sleep

map_1 = Map(20)
map_2 = Map(10)
game = Game()
game.current_map = map_1
bot_1 = Bot(name="Alan", x=1, y=1, currrent_map=map_1)
bot_2 = Bot(name="Bob", x=2, y=2, currrent_map=map_1)
player = Player(name="Doomguy", x=4, y=5, currrent_map=map_1)

while True:
    map_1.render()
    command = input()
    # if command == "BOOM":
    #     player.short_name = "*"
    #     bot_1.short_name = "*"
    #     bot_2.short_name = "*"
    #     map_1.render()
    #     print("GAME OVER!")
    #     # print(map_1.show_box())
    #     break

    player.move(command)
    # bot_1.do_something()
    # bot_2.do_something()
    sleep(1)

