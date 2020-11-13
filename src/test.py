from tdge import *

game = Game(movement=True, width=500, height=500, title="Hello, test", resizable=True, velocity=0.1)

display.set_background(game, background_type="color", color=[255, 0, 0])

cube = Cube(size=[100, 100, 100], color=[0, 255, 0], position=[200, 200, 100])

display.draw(game, cube)

start_game(game)
