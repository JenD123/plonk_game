import pygame
from pygame import Color
from pygame import draw

class Paddle:
	
	""" Define an x position, screen height, speed of paddle, length of paddle. """
	def __init__(self, x, screen_height, speed, length):
		# set the paddle to the middle of the screen when program starts
		self.x = x
		self.y = screen_height/2 - length/2

		self.speed = speed
		self.length = length
		self.width = 10

		# define boundaries of paddle on screen
		self.min_y = 0
		self.max_y = screen_height - length

	def move_up(self):
		self.y = self.y - self.speed
		if self.y < self.min_y:
			self.y = self.min_y

	def move_down(self):
		self.y = self.y + self.speed
		if self.y > self.max_y:
			self.y = self.max_y


	# display paddle on screen
	def show(self, screen):
		rectangle = (self.x, self.y, self.width, self.length)
		draw.rect(screen, Color('white'), rectangle)


