from pygame import font
import pygameMenu

from settings import Settings

class Scoreboard:

	def __init__(self, screen, screen_width, screen_height):

		self.screen = screen
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.left_score = 0
		self.right_score = 0

	def increment_left(self):

		self.left_score = self.left_score + 1

	def increment_right(self):

		self.right_score = self.right_score + 1

	def reset_score(self):
		
		self.left_score = 0
		self.right_score = 0

	def show(self):

		myfont = font.Font(pygameMenu.fonts.FONT_MUNRO, 30) # or monospace
		scoreboard = myfont.render(
			f"{self.left_score} - {self.right_score}", 	#text
			True, 	#antialias
			Settings.text_colour, 	#colour
		)
		scoreboard_width = scoreboard.get_rect().width
		scoreboard_height = scoreboard.get_rect().height
		self.screen.blit(scoreboard, (self.screen_width/2 - scoreboard_width/2, scoreboard_height/2))

	def show_end_state(self):

		myfont = font.Font(pygameMenu.fonts.FONT_MUNRO, 60)
		win_state = myfont.render(
			'WIN' if self.right_score > 10 else 'LOSE',
			True,
			Settings.text_colour,
		)
		scoreboard = myfont.render(
			f'{self.left_score} - {self.right_score}', 	#text
			True, 	#antialias
			Settings.text_colour, 	#colour
		)

		win_state_width = win_state.get_rect().width
		win_state_height = win_state.get_rect().height
		scoreboard_width = scoreboard.get_rect().width
		scoreboard_height = scoreboard.get_rect().height
		self.screen.blit(win_state, (self.screen_width/2 - win_state_width/2, self.screen_height/2 - scoreboard_height*2))
		self.screen.blit(scoreboard, (self.screen_width/2 - scoreboard_width/2, self.screen_height/2 - scoreboard_height/2))


