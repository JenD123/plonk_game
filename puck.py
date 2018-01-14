import math
import pygame
from pygame import Color
from pygame import draw
from scipy.interpolate import interp1d

from settings import Settings

class Puck:

	""" Define screen width, height, speed of puck, and side length of te puck 
	    (same for width because puck is a cicle). """
	def __init__(self, screen_width, screen_height, speed, side_length):

		# set puck to middle of the screen when program starts
		self.respawn_x = screen_width/2 - side_length/2
		self.respawn_y = screen_height/2 - side_length/2
		self.x = screen_width/2 - side_length/2
		self.y = screen_height/2 - side_length/2
		
		self.speed = speed
		self.x_speed = -1 * speed
		self.y_speed = speed * 0.2

		self.side_length = side_length

		# define boundaries of the puck on screen 
		self.min_x = 0
		self.max_x = screen_width - side_length
		self.min_y = 0
		self.max_y = screen_height - side_length


	def update(self, score):
		self.x = self.x + self.x_speed
		self.y = self.y + self.y_speed

		# puck changes direction when it collides with top or bottom wall
		if self.y < self.min_y or self.y > self.max_y:
			self.change_y_direction()
		# puck respawns to centre if puck goes goes past left or right wall and update score
		if self.x < self.min_x or self.x > self.max_x:
			if self.x < self.min_x:
				score.increment_right()
			elif self.x > self.max_x:
				score.increment_left()

			self.x = self.respawn_x
			self.y = self.respawn_y
			self.change_x_direction()


	# update puck position and display on screen
	def show(self, screen, score):
		rectangle = (self.x, self.y, self.side_length, self.side_length)
		draw.rect(screen, Settings.text_colour, rectangle)
		self.update(score)

	def collides_with(self, paddle):
		# return true if puck collides with paddle
		# if collision occurs, update the x-speed and y-speed (to change reflection angle)
		if (self.x < (paddle.x + paddle.width) 
			and (self.x + self.side_length)> paddle.x 
			and self.y < (paddle.y + paddle.length) 
			and (self.y + self.side_length) > paddle.y):
		
				translate = interp1d([0, paddle.length + self.side_length], [-50, 50])
				angle = float(translate(self.y - paddle.y + self.side_length))
				self.x_speed = self.speed * math.cos(math.radians(angle))
				self.y_speed = self.speed * math.sin(math.radians(angle))
				return True
		
		return False

	# change direction when puck collides with paddle
	def change_x_direction(self, direction=None):
		if direction == 'left':
			if self.x_speed > 0:
				self.x_speed *= -1
		elif direction == 'right':
			if self.x_speed < 0:
				self.x_speed *= -1
		else:
			self.x_speed *= -1



	def change_y_direction(self):
		self.y_speed = self.y_speed * -1













