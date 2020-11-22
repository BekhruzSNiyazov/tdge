from tdge import *

game = Game(movement=True, width=1920, height=1080, title="3D Game Engine Test", velocity=1, fullscreen=True)

cube = Cube(size=[25, 25, 25], color=[255, 255, 255], position=[0, 0, 100], rotation=[0, 0, 0])
test = Cube(size=[25, 25, 25], color=[0, 0, 0], position=[500, 0, 100], rotation=[0, 0, 0])

display.draw(game, cube)
display.draw(game, test)

display.set_background(game, background_type="color", color=[0, 255, 0])

# def code():
    # rotate(cube, velocity=0.1)

start_game(game)
