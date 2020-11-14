from tdge import *

game = Game(movement=True, width=500, height=500, title="Rotating cube", resizable=True, velocity=1)

cube = Cube(size=[100, 100, 100], color=[255, 255, 255], position=[200, 200, 0])

display.draw(game, cube)

def code():
    rotate(cube, velocity=0.01)

start_game(game, pygame_code=code)
