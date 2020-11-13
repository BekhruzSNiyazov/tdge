from tdge import *

game = Game(movement=True, width=500, height=500, title="Hello, test", resizable=True, velocity=0.1)

cube = Cube(size=[100, 100, 100], color=[255, 255, 255], position=[200, 200, 100])

display.draw(game, cube)

start_game(game)
