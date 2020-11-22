"""
	Copyright © 2020 Bekhruz Niyazov
	
	THIS CODE IS STILL IN DEVELOPMENT

	This code is licensed with MIT license.

	This is a 3D Game Engine created by Bekhruz Niyazov during the coronavirus pandemic.

	The following code is free to use and open source.

	You can contact me using this email: bekhruzsniyazov@outlook.com.

	Enjoy using this 3D Game Engine!
"""

# importing needed modules
import pygame
from datetime import datetime

# the main Game class
class Game(object):

	# initializing function
	def __init__(self, movement=True, width=10, height=10, title="My Game", icon_path="", rotation=[0, 0, 0], position=[0, 0, 0], resizable=False, fullscreen=False, velocity=1):
		
		# checking if the user passed correct arguments; if not: raise an error
		if type(movement) != bool:
			error = "Movement should be a bool. If movement is False the player will not be able to move; otherwise the player will be able to move."
			raise TypeError(error)

		if type(width) != int and type(width) != float:
			error = "Width should be an integer or a float. [Size of width of window] = width pixels."
			raise TypeError(error)

		if type(height) != int and type(height) != float:
			error = "Height should be an integer or a float. [Size of height of window] = height pixels."
			raise TypeError(error)

		if type(title) != str:
			error = "Title should be a string. Title is the title of window."
			raise TypeError(error)

		if type(icon_path) != str:
			error = "Icon path should be a string. To set the icon to the window you need to provide its path."
			raise TypeError(error)

		if type(rotation) != list:
			error = "Rotation should be a list.\nThe first number in the list corresponds to rotation in X direction; the second corresponds to rotation direction in Y direction and the third corresponds to rotation in Z direction."
			raise TypeError(error)

		if type(resizable) != bool:
			error = "Resizable should be a bool. If resizable is set to true the user will be able to resize the window."
			raise TypeError(error)

		if type(fullscreen) != bool:
			error = "Fullscreen should be a bool."
			raise TypeError(error)

		if type(position) != list:
			error = "Position should be a list.\nThe first number in the list corresponds to position of the player on X axis; the second corresponds to the position on Y axis and the third corresponds to the position on Z axis."
			raise TypeError(error)

		if len(rotation) != 3:
			error = "The length of rotation should be 3.\nThe first number in the list corresponds to rotation in X direction; second corresponds to rotation direction in Y direction and third corresponds to rotation in Z direction."
			raise ValueError(error)

		if len(position) != 3:
			error = "The length of position should be 3.\nThe first number corresponds to position of the player on X axis; the second corresponds to the position on Y axis and third corresponds to the position on Z axis."
			raise ValueError(error)

		if type(velocity) != int and type(velocity) != float:
			error = "Velocity should be an integer or a float."
			raise TypeError(error)

		if icon_path:
			try:
				open(icon_path, "r").close()
			except:
				error = "The given icon path is incorrect."
				raise FileNotFoundError(error)

		# initializing the pygame to make the whole thing work
		pygame.init()

		# if resizable is true
		if resizable:
			# creating the game window that can resize
			self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE)

		# if fullscreen is true and resizable is not true
		elif fullscreen:
			# creating a fullscreen window
			self.win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

		# if resizable is false and fullscreen is false
		else:
			# creating the game window, that cannot resize
			self.win = pygame.display.set_mode((width, height))

		# making the width, height, movement, rotation, position, velocity and update global variables
		self.width = width
		self.height = height
		self.movement = movement
		self.rotation = rotation
		self.position = position
		self.velocity = velocity
		self.color = [0, 0, 0]
		self.image_path = ""
		self.update = False

		# setting the objects variable to []. it should store all objects in the game
		self.objects = []

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
	def set_background(game, background_type="color", color=[0, 0, 0], image_path=""):

		# checking, if user have passsed correct arguments
		if type(background_type) != str:
			error = "The backrgound_color argument should be of type str.\nThere are possible values for background_type: \"color\" and \"image\"."
			raise TypeError(error)
		
		if type(color) != list:
			error = "The color argument should be of type list."
			raise TypeError(error)

		if type(image_path) != str:
			error = "The image_path argument should be of type str."
			raise TypeError(error)

		# setting the background_type of the game to the given background_type
		game.background_type = background_type
		# setting the color of the background of the game to the gived color
		game.color = color
		# setting the path of the background image of the game to the given image path
		game.image_path = image_path

		# if the type of the background is a color: fill the background with this color
		if background_type == "color":

			# warning user if he has passed the image_path argument
			if image_path != "":
				print("Warning. You have provided the image_path, while the background_type is set to \"color\".\nIf you want to set an image as a backround you should set background_type to \"image\".")

			# fill the game window with color
			game.win.fill(color)
		
		# if the type of the background is an image: set the given image as a background
		elif background_type == "image":

			# warning user if he has passed the color argument
			if color != [0, 0, 0]:
				print("Warning. You have provided the color, while the background_type is set to \"image\".\nIf you want to fill background with color, you should set background_type to \"color\".")

			# checking, if the image exists
			try:
				open(image_path, "r").close()
			except:
				error = "The given image path is incorrect."
				raise FileNotFoundError(error)

			game.image = pygame.image.load(image_path)

			# displaying the image on a screen
			game.win.blit(game.image, (0, 0))

		# update the screen so that user will see the difference
		pygame.display.update()

	# this function handles the drawing objects on the display
	def draw(game, object):

		# updating the background if game.update is True
		if game.update:
			if game.image_path: game.win.blit(game.image, (0, 0))
			else: game.win.fill(game.color)

		# checking the type of the given object
		if type(object) == Cube:

			# getting the height of the game window
			height = game.win.get_height()
			# getting the width of the game window
			width = game.win.get_width()
			# getting the X distance between the object and the user
			distanceX = game.position[0] - object.position[0]
			# getting the Z distance between the object and the user
			distanceZ = game.position[2] - object.position[2]
			# setting the size of the object that user will actually see
			display_size = []
			for size in object.size:
				if game.position[2] < object.position[2]:
					display_size.append(size / distanceZ * 1000)
				else: display_size.append(0)
			# creating a position list, storing the position of an object on a 3D coordinate plane
			position = [width / 2 - distanceX - display_size[0] / 2, height / 2 - object.position[1] - display_size[1] / 2, object.position[2]]

			# if player is not "inside" of the object
			if game.position[0] > position[0] + object.size[0] / 2 or \
				game.position[0] < position[0] - object.size[0] / 2 and \
					game.position[1] > position[1] + object.size[1] / 2 or \
						game.position[1] < position[1] - object.size[1] / 2 and \
							game.position[2] > position[2] + object.size[2] / 2 or \
								game.position[2] < position[2] - object.size[2] / 2:

				# if the rotation of the player is [0, 0, 0]
				if game.rotation == [0, 0, 0]:
					# if the rotation of the object is [0, 0, 0]
					if object.rotation == [0, 0, 0]:
						# drawing a 2D rectangle
						pygame.draw.rect(game.win, object.color, ((position[0], position[1]), (display_size[0], display_size[1])))
					# if rotation of the object is not [0, 0, 0]
					else:
						# if the object is rotated on Y axis
						if object.rotation[1] != 0:
							# getting the sizes on X axis
							y_rotation = object.rotation[1]
							percent = 100 / (90 / y_rotation)
							x_size = display_size[0]
							x0 = x_size / 100 * percent
							x1 = x_size - x0
							number = 255 - (255 / 100 * percent)

							# setting the RGB values
							color0 = object.color[0] - number if object.color[0] >= number else 0
							color1 = object.color[1] - number if object.color[1] >= number else 0
							color2 = object.color[2] - number if object.color[2] >= number else 0

							# drawing two 2D rectangles based on the data above
							pygame.draw.rect(game.win, (color0, color1, color2), ((position[0], position[1]), (x0, display_size[1])))
							pygame.draw.rect(game.win, object.color, ((position[0]+x0, position[1]), (x1, display_size[1])))
					# else:
						# TODO
						# write code for displaying object when it is to the right or to the left of the player
						# pass

			# adding the object if it is not in game.objects
			if object not in game.objects:
				game.objects.append(object)
		else:
			error = "You should provide the object of supported type by this library."
			raise TypeError(error)

		# update the screen so that user will see the difference
		pygame.display.update()

# function, that runs the game
def start_game(game, code=None):

	# giving the user instructions on how to close the game
	print("To exit the game press ESC.")

	pygame.init()

	# checking if user has passed correct arguments
	if type(game) != Game:
		error = "Game should be a Game object. To create a Game object you need to import it from this library."
		raise TypeError(error)

	if code is not None:
		# if user have passed the pygame_code argument but it is not a function...
		if not callable(code):
			# ...raise an error
			error = "The pygame_code argument should be a function. Make sure you have not added \"(\" and \")\" (brackets)."
			raise TypeError(error)

	# preparing to count FPS
	start = datetime.now().second

	# starting couting frames from 0
	frame_count = 0

	# creating a pygame clock
	clock = pygame.time.Clock()

	# I use bools instead of just breaking, because
	# I want the while loop to end first, and then to end the game
	running = True

	while running:

		# printing FPS every second
		# getting the current time
		now = datetime.now().second
		# checking, if one second is over
		if now - start >= 1:
			# printing FPS
			print(frame_count)
			# resetting the timer
			start = datetime.now().second
			# resetting the FPS
			frame_count = 0

		# if clicked the "x" button: quit the game
		if pygame.event.get(pygame.QUIT): running = False

		# getting all the key presses from the user
		keys = pygame.key.get_pressed()

		# if the user pressed "escape": quit the game
		if keys[pygame.K_ESCAPE]: running = False

		# when game.update is False the background will not be updated
		game.update = False

		# if the movement is enabled: move the user when he presses WASD keys and rotate if he is moving his mouse
		if game.movement:
			
			# if user presses WASD keys: update the position of the player

			# if the user pressed "w"
			if keys[pygame.K_w]:
				game.position = (game.position[0], game.position[1], game.position[2] + game.velocity)
				game.update = True
			# if the user pressed "s"
			if keys[pygame.K_s]:
				game.position = (game.position[0], game.position[1], game.position[2] - game.velocity)
				game.update = True
			# if the user pressed "a"
			if keys[pygame.K_a]:
				game.position = (game.position[0] - game.velocity, game.position[1], game.position[2])
				game.update = True
			# if the user pressed "d"
			if keys[pygame.K_d]:
				game.position = (game.position[0] + game.velocity, game.position[1], game.position[2])
				game.update = True

		for object in game.objects:
			display.draw(game, object)

		# increasing FPS because the while loop ended and will start again
		frame_count += 1

		if callable(code):
			code()

		clock.tick(120)

	# exit the game when it is closed
	pygame.quit()

# this function handles the rotation of the given object
def rotate(object, axis="y", velocity=0.1):
	# error-checking
	if type(axis) != str:
		error = "Axis should be a string. Axis should be \"x\"or  \"y\" or \"z\"."
		raise TypeError(error)
	if axis not in ["x", "y", "z"]:
		error = "Axis should be \"x\" or \"y\" or \"z\"."
		raise ValueError(error)
	if type(velocity) not in [int, float]:
		error = "Velocity should be int or float."
		raise TypeError(error)

	# checking the type of the object
	if type(object) == Cube:
		# changing the rotation of the object
		if axis == "x":
			object.rotation[0] += velocity
		if axis == "y":
			if object.rotation[1] + velocity <= 89:
				object.rotation[1] += velocity
			else: object.rotation[1] = 0
		if axis == "z":
			object.rotation[2] += velocity
	# if object is not supported by the library: raise an error
	else:
		error = "You should provide the object of supported types by this library."
		raise TypeError(error)

# class for creating Cube objects
class Cube(object):

	# initializing function
	def __init__(self, name="New Cube", size=[100, 100, 100], color=[0, 0, 0], position=[0, 0, 0], rotation=[0, 0, 0]):

		# error-checking
		if type(name) != str:
			error = "The name of the cube should be a string."
			raise TypeError(error)
		if type(size) != list:
			error = "Size should be a list.\nThe first number in the list corresponds to size on X-axis; the second corresponds to size on Y-axis and the third corresponds to size on Z-axis."
			raise TypeError(error)
		if len(size) != 3:
			error = "The length of size should be 3."
			raise ValueError(error)
		if type(color) != list:
			error = "Color should be a list.\nThe first number in the list corresponds to the amount of red color (from 0 to 255); the second corresponds to amount of green color (from 0 to 255) and the third corresponds to the amount of blue color (from 0 to 255)."
			raise TypeError(error)
		if len(color) != 3:
			error = "The length of color should be 3."
			raise ValueError(error)
		for number in color:
			if number > 255 or number < 0:
				error = "Every number in color should be in range 0 and 256 (it should be >= 0 and <= 255)."
				raise ValueError(error)
		if type(position) != list:
			error = "Position should be a list.\nThe first number in the list corresponds to the position on X-axis; the second corresponds to the position on Y-axis and the third corresponds to the position on Z-axis."
			raise TypeError(error)
		if type(rotation) != list:
			error = "Rotation should be a list.\nThe first number in the list corresponds to the rotation on X-axis; the second corresponds to the rotation on Y-axis and the third corresponds to the rotation on Z-axis."
			raise TypeError(error)
		if len(rotation) != 3:
			error = "The length of rotation should be 3."
			raise ValueError(error)
		
		self.size = size
		self.color = color
		self.position = position
		self.rotation = rotation
		self.name = name

# class for creating cutom objects
class CustomObject:
	pass

# function, that converts hex colors to rgb colors
# just a nice time saver :)
def hex_to_rgb(hex):
	
	# checking, if the user passed correct argument
	if type(hex) != str:
		error = "You need to pass one argument, which should represent the hex color in a form of string."
		raise TypeError(error)

	# if the first character of color is not "#": return an error
	if hex[0] != "#":
		error = "The first argument should represent a hex color in a form of string. The first character should be \"#\"."
		raise ValueError(error)

	# removing "#" from color
	hex = hex.lstrip("#")
	# if that will not work, return an error
	try:
		# returning a converted color
		return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
	except:
		error = "Couldn't convert the given hex color to rgb. Try a different one."
		raise ValueError(error)
