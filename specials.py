from pygame import draw
from random import randint

from puck import Puck
from settings import Settings

class Specials:

	def __init__(self, screen_width, screen_height, special_width):
		self.special_width = special_width
		# define boundaries for special on screen (middle third)
		self.min_x = screen_width/3
		self.max_x = screen_width/3 * 2 - special_width
		self.min_y = 40
		self.max_y = screen_height - 40

		self.respawn()

	# set special to random point on screen that is within the boundaries
	def respawn(self):
		self.x = randint(self.min_x, (self.max_x + 1))
		self.y = randint(self.min_y, (self.max_y + 1))

	# display special on screen
	def show(self, screen):
		rectangle = (self.x, self.y, self.width, self.length)
		draw.rect(screen, Settings.menu_colour, rectangle)

	def perform_action(self, puck, score):
		pass

	def collides_with(self, puck, score):
		# return true if puck collides with special
		if (self.x < (puck.x + puck.side_length)
			and (self.x + self.width) > puck.x
			and self.y < (puck.y + puck.side_length)
			and (self.y + self.length) > puck.y):

			return True

		return False


class Wall(Specials):

	def __init__(self, screen_width, screen_height):
		self.length = 40
		self.width =  5
		super().__init__(screen_width, screen_height, self.width)

	def __str__(self):
		return 'Wall'

	def perform_action(self, puck, score):
		puck.change_x_direction()
		self.respawn()


class Boost(Specials):

	def __init__(self, screen_width, screen_height):
		self.length = 15
		self.width = 15
		super().__init__(screen_width, screen_height, self.width)

	def __str__(self):
		return 'Boost'

	def perform_action(self, puck, score):
		puck.increase_speed()
		self.respawn()


class Coin(Specials):

	def __init__(self, screen_width, screen_height):
		self.length = 15
		self.width = 15
		super().__init__(screen_width, screen_height, self.width)

	def __str__(self):
		return 'Coin' 	

	def perform_action(self, puck, score):
		if puck.x_speed > 0:
			# puck is moving right, increase left player score
			score.increment_left()
		else:
			# puck is moving left, increase right player score
			score.increment_right()
		self.respawn()


class NoSpecial(Specials):

	def __init__(self, screen_width, screen_height):
		pass

	def __str__(self):
		return 'Normal'

	def respawn(self):
		pass

	def show(self, screen):
		pass

	def perform_action(self, puck, score):
		pass

	def collides_with(self, puck, score):
		pass