"""
	THIS CODE IS STILL IN DEVELOPMENT

	This code is licensed with MIT license.

	This is a 3D Game Engine created by Bekhruz Niyazov during the coronavirus pandemic.

	The following code is free to use and open source.

	You can contact me using this email: bekhruzsniyazov@outlook.com.

	Enjoy using this 3D Game Engine!

	Bekhruz Niyazov, 2020.
"""

# importing needed modules
import pygame
from datetime import datetime

# the main Game class
class Game(object):

	# creating the Game window
	def __init__(self, movement=False, width=10, height=10, title="My Game", icon_path="", rotation=(0, 0, 0), position=(0, 0, 0), resizable=False):
		
		# checking if the user passed correct arguments; if not: raise an error
		if type(movement) != bool:
			raise TypeError("ERROR. Movement should be a bool. If movement is False the player will not be able to move; otherwise the player will be able to move.")

		if type(width) != int and type(width) != float:
			raise TypeError("ERROR. Width should be an integer or a float. [Size of width of window] = (width*100) pixels.")

		if type(height) != int and type(height) != float:
			raise TypeError("ERROR. Height should be an integer or a float. [Size of height of window] = (height*100) pixels.")

		if type(title) != str:
			raise TypeError("ERROR. Title should be a string. Title is the title of window.")

		if type(icon_path) != str:
			raise TypeError("ERROR. Icon path should be a string. To set the icon to the window you need to provide its path.")

		if type(rotation) != tuple:
			raise TypeError("ERROR. Rotation should be a tuple.\nThe first number in touple corresponds to rotation in X direction; second corresponds to rotation direction in Y direction and third corresponds to rotation in Z direction.")

		if type(resizable) != bool:
			raise TypeError("ERROR. resizable should be a bool. If resizable is set to true the user will be able to resize the window.")

		if type(position) != tuple:
			raise TypeError("ERROR. Position should be a tuple.\nThe first number corresponds to position of the player on X axis; the second corresponds to the position on Y axis and third corresponds to the position on Z axis.")

		if len(rotation) != 3:
			raise ValueError("ERROR. The length of rotation should be 3.\nThe first number in touple corresponds to rotation in X direction; second corresponds to rotation direction in Y direction and third corresponds to rotation in Z direction.")

		if len(position) != 3:
			raise ValueError("ERROR. The length of position should be 3.\nThe first number corresponds to position of the player on X axis; the second corresponds to the position on Y axis and third corresponds to the position on Z axis.")

		if icon_path:
			try:
				open(icon_path, "r").close()
			except:
				raise FileNotFoundError("The given icon path is incorrect.")

		# initializing the pygame to make the whole thing work
		pygame.init()

		# if resizable is true
		if resizable:
			# creating the game window that can resize
			self.win = pygame.display.set_mode((width*100, height*100), pygame.RESIZABLE)

		# if resizable is false
		else:
			# creating the game window, that cannot resize
			self.win = pygame.display.set_mode((width * 100, height * 100))

		# making the width, height, movement, rotation and position global variables
		self.width = width * 100
		self.height = height * 100
		self.movement = movement
		self.rotation = (0, 0, 0)
		self.position = (0, 0, 0)

		# set the title of the game ("My Game" is the default)
		pygame.display.set_caption(title)

		# if the icon path is given: change the icon to the custom one
		if icon_path: pygame.display.set_icon(pygame.image.load(icon_path))

	# enable the movement of the player
	def enable_movement(self):
		self.movement = True
	
	# disable the movement of the player
	def disable_movement(self):
		self.movement = False
	
# changing the display
class display(object):

	# changing the background of the game
	def set_background(self, background_type="color", color=(0, 0, 0), image_path=""):
		
		# if the type of the background is a color: fill the background with this color
		if background_type == "color":

			# fill the game window with color
			self.win.fill(color)

			# update the screen so that user will see the difference
			pygame.display.update()
		
		# if the type of the background is an image: set the given image as a background
		elif background_type == "image":
			self.win.blit(pygame.image.load(image_path), (0, 0))

	# drawing the objects on the screen

	# drawing a cube
	def draw_cube(self, size=(1, 1, 1), coords=(0, 0, 0), color=(100, 100, 100)):

		# drawing a 2D rectangle
		pygame.draw.rect(self.win, color, ((coords[0]*100, coords[1]*100), (size[0]*100, size[1]*100)))

		# update the screen so that user will see the difference
		pygame.display.update()

# function, that runs the game
def start_game(game, pygame_code=None):

	# if user have given the function with pygame code...
	if callable(pygame_code):
		# ...call this function
		pygame_code()

	# preparing to count FPS
	start = datetime.now().second

	# I use bools instead of just breaking, because 
	# I want the while loop to end first, and then to end the game
	running = True

	frame_count = 0
	while running:

		# printing FPS every second
		now = datetime.now().second
		if now - start >= 1:
			print(frame_count)
			start = datetime.now().second
			frame_count = 0

		# if clicked the "x" button: quit the game
		if pygame.event.get(pygame.QUIT): running = False

		# getting all the key presses from the user
		keys = pygame.key.get_pressed()

		# if the user pressed "escape": quit the game
		if keys[pygame.K_ESCAPE]: running = False

		# if the movement is enabled: move the user when he presses WASD keys and rotate if he is moving his mouse
		if game.movement:
			pass

		# increasing FPS because the while loop ended and will start again
		frame_count += 1

	# exit the game when it is closed
	exit()

# class for creating cutom objects
class CustomObject:
	pass
