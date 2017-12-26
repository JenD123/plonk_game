from pygame import font
import pygameMenu

class Scoreboard:

	def __init__(self, screen, screen_width, screen_height):

		self.screen = screen
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.left_score = 0
		self.right_score = 0
		self.font = font.SysFont(pygameMenu.fonts.FONT_MUNRO, 30) # or monospace

	def increment_left(self):

		self.left_score = self.left_score + 1

	def increment_right(self):

		self.right_score = self.right_score + 1

	def reset_score(self):
		
		self.left_score = 0
		self.right_score = 0

	def show(self):

		scoreboard = self.font.render(
			f"{self.left_score} - {self.right_score}", 	#text
			True, 	#antialias
			(255, 255, 255), 	#colour
		)
		scoreboard_width = scoreboard.get_rect().width
		scoreboard_height = scoreboard.get_rect().height
		self.screen.blit(scoreboard, (self.screen_width/2 - scoreboard_width/2, scoreboard_height/2))


