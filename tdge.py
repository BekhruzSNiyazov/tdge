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

# the main Game class
class Game(object):

	# creating the Game window
	def __init__(self, movement=False, width=1000, height=1000, caption="My Game", icon_path=""):

		# initializing the pygame
		pygame.init()

		# making height, width, win and movement global variables to access them in other methods
		self.height = height
		self.width = width
		self.win = pygame.display.set_mode((width, height))
		self.movement = movement

		# set the title of the game ("My Game" is the default)
		pygame.display.set_caption(caption)

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
	def draw_cube(self, xyz=(1, 1, 1), coords=(0, 0), color=(100, 100, 100)):

		# draw a rectangle
		pygame.draw.rect(self.win, color, ((coords[0], coords[1]), (xyz[0]*100, xyz[1]*100)))

		# update the screen so that user will see the difference
		pygame.display.update()

# function, that runs the game
def start_game(game):

	# I use bools instead of just breaking, because 
	# I want the while loop to end first, and then to end the game
	running = True

	while running:

		# if clicked the "x" button: quit the game
		if pygame.event.get(pygame.QUIT): running = False

		# getting all the key presses from the user
		keys = pygame.key.get_pressed()

		# if the user pressed "escape": quit the game
		if keys[pygame.K_ESCAPE]: running = False

		# if the movement is enabled: move the user when he presses WASD keys and rotate if he is moving his mouse
		if game.movement:
			pass

	# exit the game when it is closed
	exit()

# class for creating cutom objects
class CustomObject:
	pass