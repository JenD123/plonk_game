class Paddle:
	
	def __init__(self, x, screen_height, speed, width):
		""" Define an x position, screen height, speed of paddle, width of paddle. """
		self.x = x
		self.y = screen_height/2 - width/2

		self.speed = speed
		self.width = width

		self.min_y = 0
		self.max_y = screen_height - width

	def move_up(self):
		y = y - speed
		if y < min_y:
			y = min_y

	def move_down(self):
		y = y + speed
		if y > max_y:
			y = max_y


