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
	def __init__(self, movement=False, width=10, height=10, title="My Game", icon_path="", rotation=[0, 0, 0], position=[0, 0, 0], resizable=False, velocity=1):
		
		# checking if the user passed correct arguments; if not: raise an error
		if type(movement) != bool:
			raise TypeError("Movement should be a bool. If movement is False the player will not be able to move; otherwise the player will be able to move.")

		if type(width) != int and type(width) != float:
			raise TypeError("Width should be an integer or a float. [Size of width of window] = width pixels.")

		if type(height) != int and type(height) != float:
			raise TypeError("Height should be an integer or a float. [Size of height of window] = height pixels.")

		if type(title) != str:
			raise TypeError("Title should be a string. Title is the title of window.")

		if type(icon_path) != str:
			raise TypeError("Icon path should be a string. To set the icon to the window you need to provide its path.")

		if type(rotation) != list:
			raise TypeError("Rotation should be a list.\nThe first number in the list corresponds to rotation in X direction; the second corresponds to rotation direction in Y direction and the third corresponds to rotation in Z direction.")

		if type(resizable) != bool:
			raise TypeError("resizable should be a bool. If resizable is set to true the user will be able to resize the window.")

		if type(position) != list:
			raise TypeError("Position should be a list.\nThe first number in the list corresponds to position of the player on X axis; the second corresponds to the position on Y axis and the third corresponds to the position on Z axis.")

		if len(rotation) != 3:
			raise ValueError("The length of rotation should be 3.\nThe first number in the list corresponds to rotation in X direction; second corresponds to rotation direction in Y direction and third corresponds to rotation in Z direction.")

		if len(position) != 3:
			raise ValueError("The length of position should be 3.\nThe first number corresponds to position of the player on X axis; the second corresponds to the position on Y axis and third corresponds to the position on Z axis.")

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
			self.win = pygame.display.set_mode((width, height), pygame.RESIZABLE)

		# if resizable is false
		else:
			# creating the game window, that cannot resize
			self.win = pygame.display.set_mode((width, height))

		# making the width, height, movement, rotation, position and velocity global variables
		self.width = width
		self.height = height
		self.movement = movement
		self.rotation = rotation
		self.position = position
		self.velocity = velocity
		self.color = [0, 0, 0]
		self.image_path = ""

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
			raise TypeError("The backrgound_color argument should be of type str.\nThere are possible values for background_type: \"color\" and \"image\".")
		
		if type(color) != list:
			raise TypeError("The color argument should be of type list.")

		if type(image_path) != str:
			raise TypeError("The image_path argument should be of type str.")

		game.background_type = background_type
		game.color = color
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
				raise FileNotFoundError("The given image path is incorrect.")

			game.image = pygame.image.load(image_path)

			# displaying the image on a screen
			game.win.blit(game.image, (0, 0))

		# update the screen so that user will see the difference
		pygame.display.update()

	# this function handles the drawing objects on the display
	def draw(game, object):

		# updating the background
		if game.image_path: game.win.blit(game.image, (0, 0))
		else: game.win.fill(game.color)

		# checking the type of the given object
		if type(object) == Cube:

			if object.rotation == [0, 0, 0]:
				# drawing a 2D rectangle
				pygame.draw.rect(game.win, object.color, ((object.position[0], object.position[1]), (object.size[0], object.size[1])))
			else:
				# getting the sizes on X axis
				y_rotation = object.rotation[1]
				percent = 100 / (90 / y_rotation)
				x_size = object.size[0]
				x0 = x_size / 100 * percent
				x1 = x_size - x0
				number = 255 - (255 / 100 * percent)

				# setting the RGB values
				color0 = object.color[0] - number if object.color[0] >= number else 0
				color1 = object.color[1] - number if object.color[1] >= number else 0
				color2 = object.color[2] - number if object.color[2] >= number else 0

				# drawing two 2D rectangles based on the data above
				pygame.draw.rect(game.win, (color0, color1, color2), ((object.position[0], object.position[1]), (x0, object.size[1])))
				pygame.draw.rect(game.win, object.color, ((object.position[0]+x0, object.position[1]), (x1, object.size[1])))

			# adding the object if it is not in game.objects
			if object not in game.objects:
				print("adding a new object")
				game.objects.append(object)
		else:
			raise TypeError("You should provide the object of supported types by this library.")

		# update the screen so that user will see the difference
		pygame.display.update()

# function, that runs the game
def start_game(game, code=None):

	# giving the user instructions on how to close the game
	print("To exit the game press ESC.")

	pygame.init()

	# checking if user has passed correct arguments
	if type(game) != Game:
		raise TypeError("Game should be a Game object. To create a Game object you need to import it from this library.")

	if code is not None:
		# if user have passed the pygame_code argument but it is not a function...
		if not callable(code):
			# ...raise an error
			raise TypeError("The pygame_code argument should be a function. Make sure you have not added \"(\" and \")\" (brackets).")

	# preparing to count FPS
	start = datetime.now().second

	# starting couting frames from 0
	frame_count = 0

	# I use bools instead of just breaking, because 
	# I want the while loop to end first, and then to end the game
	running = True

	if callable(code):
		# I am repeating this code twice to increase efficiency
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

			# if the movement is enabled: move the user when he presses WASD keys and rotate if he is moving his mouse
			if game.movement:
				
				# if user presses WASD keys: update the position of the player

				# if the user pressed "w"
				if keys[pygame.K_w]:
					game.position = (game.position[0], game.position[1], game.position[2] + game.velocity)
				# if the user pressed "s"
				if keys[pygame.K_s]:
					game.position = (game.position[0], game.position[1], game.position[2] - game.velocity)
				# if the user pressed "a"
				if keys[pygame.K_a]:
					game.position = (game.position[0] - game.velocity, game.position[1], game.position[2])
				# if the user pressed "d"
				if keys[pygame.K_d]:
					game.position = (game.position[0] + game.velocity, game.position[1], game.position[2])

				# updating the image that user is seeing
				update(game)

			# increasing FPS because the while loop ended and will start again
			frame_count += 1

			# calling the function that user passed in
			code()
	else:
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

			# if the movement is enabled: move the user when he presses WASD keys and rotate if he is moving his mouse
			if game.movement:
				
				# if user presses WASD keys: update the position of the player

				# if the user pressed "w"
				if keys[pygame.K_w]:
					game.position = (game.position[0], game.position[1], game.position[2] + game.velocity)
				# if the user pressed "s"
				if keys[pygame.K_s]:
					game.position = (game.position[0], game.position[1], game.position[2] - game.velocity)
				# if the user pressed "a"
				if keys[pygame.K_a]:
					game.position = (game.position[0] - game.velocity, game.position[1], game.position[2])
				# if the user pressed "d"
				if keys[pygame.K_d]:
					game.position = (game.position[0] + game.velocity, game.position[1], game.position[2])

				# updating the image that user is seeing
				update(game)

			# increasing FPS because the while loop ended and will start again
			frame_count += 1

	# exit the game when it is closed
	pygame.quit()

# function that handles the update of the location of all objects
def update(game):
	
	# getting the offset on Z axis
	z_offset = game.position[2]

	if z_offset:
		# updating every object in game
		for object in game.objects:
			# change the size of the object if it will be >= 0
			if object.size[2] + z_offset >= 0 and object.size[1] + z_offset >= 0 and object.size[0] + z_offset >= 0:
				# changing the size of the object
				object.size = [i + z_offset for i in object.size]
				# changing the position of the object
				object.position = [object.position[0] - z_offset / 2, object.position[1] - z_offset / 2, object.position[2]]
				# drawing the object on the screen
				display.draw(game, object)
		# setting the position of the player to [0, 0, 0]
		game.position = [0, 0, 0]
	else:
		for object in game.objects: display.draw(game, object)

# this function handles the rotation of the given object
def rotate(object, axis="y", velocity=0.1):
	# error-checking
	if type(axis) != str:
		raise TypeError("Axis should be a string. Axis should be \"x\"or  \"y\" or \"z\".")
	if axis not in ["x", "y", "z"]:
		raise ValueError("Axis should be \"x\" or \"y\" or \"z\".")
	if type(velocity) not in [int, float]:
		raise TypeError("Velocity should be int or float.")

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
		raise TypeError("You should provide the object of supported types by this library.")

# class for creating Cube objects
class Cube(object):

	# initializing function
	def __init__(self, size=[100, 100, 100], color=[0, 0, 0], position=[0, 0, 0], rotation=[0, 0, 0]):

		# error-checking
		if type(size) != list:
			raise TypeError("Size should be a list.\nThe first number in the list corresponds to size on X-axis; the second corresponds to size on Y-axis and the third corresponds to size on Z-axis.")
		if len(size) != 3:
			raise ValueError("The length of size should be 3.")
		if type(color) != list:
			raise TypeError("Color should be a list.\nThe first number in the list corresponds to the amount of red color (from 0 to 255); the second corresponds to amount of green color (from 0 to 255) and the third corresponds to the amount of blue color (from 0 to 255).")
		if len(color) != 3:
			raise ValueError("The length of color should be 3.")
		for number in color:
			if number > 255 or number < 0: raise ValueError("Every number in color should be in range 0 and 256 (it should be >= 0 and <= 255).")
		if type(position) != list:
			raise TypeError("Position should be a list.\nThe first number in the list corresponds to the position on X-axis; the second corresponds to the position on Y-axis and the third corresponds to the position on Z-axis.")
		if type(rotation) != list:
			raise TypeError("Rotation should be a list.\nThe first number in the list corresponds to the rotation on X-axis; the second corresponds to the rotation on Y-axis and the third corresponds to the rotation on Z-axis.")
		if len(rotation) != 3:
			raise ValueError("The length of rotation should be 3.")
		
		self.size = size
		self.color = color
		self.position = position
		self.rotation = rotation

# class for creating cutom objects
class CustomObject:
	pass

# function, that converts hex colors to rgb colors
# just a nice time saver :)
def hex_to_rgb(hex):
	
	# checking, if the user passed correct argument
	if type(hex) != str:
		raise TypeError("You need to pass one argument, which should represent the hex color in a form of string.")

	# if the first character of color is not "#": return an error
	if hex[0] != "#":
		raise ValueError("The first argument should represent a hex color in a form of string. The first character should be \"#\".")

	# removing "#" from color
	hex = hex.lstrip("#")
	# if that will not work, return an error
	try:
		# returning a converted color
		return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
	except:
		raise ValueError("Couldn't convert the given hex color to rgb. Try a different one.")
