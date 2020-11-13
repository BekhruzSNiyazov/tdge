from pygame import color
from tdge import *

game = Game(movement=True, width=500, height=500, title="Hello, test", resizable=True)

cube = Cube([100, 100, 100], color=[255, 255, 255], coords=[100, 100, 100])

display.draw(game, cube)

start_game(game)
