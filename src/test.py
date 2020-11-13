from pygame import color
from tdge import *

game = Game(movement=True, width=500, height=500, title="Hello, test", resizable=True)

cube = Cube([100, 100, 100], color=[255, 255, 255], coords=[200, 200, 100])

display.draw(game, cube)

def code():
    game.win.fill((0, 255, 255))
    pygame.display.update()

start_game(game, pygame_code=code)
