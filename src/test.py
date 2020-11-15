from tdge import *

game = Game(movement=True, width=500, height=500, title="Rotating cube", resizable=True, velocity=1)

cube = Cube(size=[100, 100, 100], color=[255, 255, 255], position=[100, 200, 0])
cube1 = Cube(size=[100, 100, 100], color=[255, 255, 255], position=[300, 200, 0])

display.draw(game, cube)
display.draw(game, cube1)

def code():
    # rotate(cube, velocity=0.01)
    pass

start_game(game, code=code)
