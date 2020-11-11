# 3D Game Engine (TDGE)

TDGE is a Python library for creating 3D Games. **It is still in development**.

## Installation

You will be able to install this library using **pip** later. This code is still in development.
## Usage

```python
# importing the library
import tdge

# creating a game surface
game = tdge.Game(movement=True, width=8, height=8, title="Hello, test")
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
tdge.display.set_background(game, background_type="color", color=(255, 255, 255), resizable=True)
# you can draw a cube by calling the draw_cube method()
tdge.display.draw_cube(game, size=(1, 1, 1), coords=(1, 1, 1), color=(0, 0, 255))
# to start the game you need to call the start_game() method
tdge.start_game(game)
```
If you want to add some code developed using pygame you can do that easily.
Just put all pygame code in a function and when you call the start_game() method you need to pass that function as a argument to pygame_code. Here is an example:
```python
def code_in_pygame():
    pygame.draw.rect(game.win, (0, 0, 0), (100, 100, 10, 10)) # replace "game" with whatever you assigned the Game object to
    pygame.display.update()
    
tdge.start_game(game, pygame_code=code_in_pygame) # you don't need need brackets after passing code_in_pygame function as an argument to pygame_code
```

## Full documentation
You can view the full documentation of this library [here](https://bekhruzsniyazov.github.io/).

## License
This code is licensed with MIT license.

## Contacts
If you have any ideas or ran in any kind of problem contact me using this email: bekhuzsniyazov@outlook.com. 
