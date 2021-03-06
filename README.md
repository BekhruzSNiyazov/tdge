# 3D Game Engine (TDGE)

TDGE is a Python library for creating 3D Games. **It is still in development**.

## Installation

You will be able to install this library using **pip** later. This code is still in development.
## Usage

```python
# importing the library
import tdge

# creating a game surface
game = tdge.Game(movement=True, width=800, height=800, title="Hello, test")
# you can disable movement of the player by calling the disable_movement() method
game.disable_movement()
 # you can enable movement of the player by calling the enable_movement() method
game.enable_movement()

# you can set the background of the game using set_background() method
# if you don't want to make the window resizable, set resizable to False, or just skip this argument
# background_type can be an image or a color
# if you want to set a background as an image
# you need to provide image_path argument to the path of image like that:
tdge.display.set_background(game, background_type="image", image_path="the_path_image", resizable=True)
# alternatively, you can fill the background with color like that:
tdge.display.set_background(game, background_type="color", color=[255, 255, 255], resizable=True)
# you can create a cube using Cube object included in the library
cube = Cube([100, 100, 100], color=[255, 255, 255], coords=[0, 0, 100])
# and after creating a cube, you can draw it
tdge.display.draw(game, cube)
# to start the game you need to call the start_game() method
tdge.start_game(game)
```
To add code that will repeat every frame you need to define a function and with the code and then pass it as an argument to start_game
```python
def code():
    pygame.draw.rect(game.win, (0, 0, 0), (100, 100, 10, 10)) # replace "game" with whatever you assigned the Game object to
    pygame.display.update()
    
tdge.start_game(game, code=code) # you don't need need brackets after passing code function as an argument to pygame_code
```

## Full documentation
You can view the full documentation of this library [here](https://bekhruzsniyazov.github.io/).

## License
This code is licensed with MIT license.

## Contacts
If you have any ideas or ran in any kind of problem contact me using this email: bekhuzsniyazov@outlook.com. 
