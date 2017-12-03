import pygame
from pygame import Color
from pygame import draw

class Puck:

	""" Define screen width, height, speed of puck, and side length of te puck 
	    (same for width because puck is a cicle). """
	def __init__(self, screen_width, screen_height, speed, side_length):

		# set puck to middle of the screen when program starts
		self.x = screen_width/2 - side_length/2
		self.y = screen_height/2 - side_length/2

		self.x_speed = speed
		self.y_speed = speed * 0.2

		self.side_length = side_length

		# define boundaries of the puck on screen 
		self.min_x = 0
		self.max_x = screen_width - side_length
		self.min_y = 0
		self.max_y = screen_height - side_length


	def update(self):
		self.x = self.x + self.x_speed
		self.y = self.y + self.y_speed

		# puck changes direction when it collides with top or bottom wall
		if self.y < self.min_y or self.y > self.max_y:
			self.change_y_direction()

	# update puck position and display on screen
	def show(self, screen):
		rectangle = (self.x, self.y, self.side_length, self.side_length)
		draw.rect(screen, Color('white'), rectangle)
		self.update()

	def collides_with(self, paddle):
		# check whether puck collides with paddle
		if (self.x < (paddle.x + paddle.width) 
			and (self.x + self.side_length)> paddle.x 
			and self.y < (paddle.y + paddle.length) 
			and (self.y + self.side_length) > paddle.y):
				return True
		
		return False

	# change direction when puck collides with paddle
	def change_x_direction(self, direction):
		if direction == 'left':
			if self.x_speed > 0:
				self.x_speed *= -1
		elif direction == 'right':
			if self.x_speed < 0:
				self.x_speed *= -1
		else:
			print("Error: invalid direction specified.")



	def change_y_direction(self):
		self.y_speed = self.y_speed * -1













