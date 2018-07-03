from pygame import font
import pygameMenu
from scipy.interpolate import interp1d

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
		otherfont = font.Font(pygameMenu.fonts.FONT_MUNRO, 25)
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

		comments = [
			# comments for lose
			'Oh no! Your plonking skills are getting a bit rusty!',
			'Nice try. Keep at it!',
			'So close. Better luck next time!',		
			# comments for win
			'That was a close one!',
			'Woohoo! Good job!',
			'You\'re killing it!',
		]

		score_difference = self.right_score - self.left_score 
		# choose comment from list of commnents based on score difference, map score difference to comments
		choose_comment = interp1d([-11, 11], [0,5.99])
		comment_index = int(choose_comment(score_difference))

		comment = otherfont.render(
			comments[comment_index],
			True,
			Settings.text_colour,
		)

		win_state_width = win_state.get_rect().width
		win_state_height = win_state.get_rect().height
		scoreboard_width = scoreboard.get_rect().width
		scoreboard_height = scoreboard.get_rect().height
		comment_width = comment.get_rect().width
		comment_height = comment.get_rect().height
		self.screen.blit(win_state, (self.screen_width/2 - win_state_width/2, self.screen_height/2 - scoreboard_height*2))
		self.screen.blit(scoreboard, (self.screen_width/2 - scoreboard_width/2, self.screen_height/2 - scoreboard_height/2))
		self.screen.blit(comment, (self.screen_width/2 - comment_width/2, self.screen_height/2 + comment_height*2))