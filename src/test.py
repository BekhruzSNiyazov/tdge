from tdge import *

game = Game(movement=True, width=500, height=500, title="3D Game Engine Test", velocity=1)

cube = Cube(size=[100, 100, 100], color=[255, 255, 255], position=[0, 0, -51], rotation=[0, 45, 0])

display.draw(game, cube)

start_game(game)
