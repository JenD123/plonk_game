import pygame
from pygame import display, font
import pygameMenu
import sys

from settings import Settings

PAGES = [
	'Move your paddle with the UP and DOWN arrow keys.',
	'Score a point by hitting the puck past the opponent '
		'on the right side of the screen. Your opponent can '
		'score a point if they hit the puck past your paddle '
		'to the left side of the screen.',
	'First to 11 points wins!',
	'WALLS will deflect the puck.',
	'BOOST PADS pads will increase the speed of the puck temporarily.',
	'COINS will give the player which hit it an extra point.',
]


class GameRules:

	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.Font(pygameMenu.fonts.FONT_MUNRO, 25)
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height

	# adapted from http://pygame.org/wiki/TextWrap
	# draw some text into an area of a surface, automatically wrapping words
	# return any text that didn't get blitted
	def drawText(self, text, bkg=None):

		rect = pygame.Rect(
			self.screen_width/4, 	# top-left x-value  
			self.screen_height/3, 	# top-left y-value
			self.screen_width/2,		# rectangle width
			self.screen_height/3, 	# rectangle height
		)
		y = rect.top
		line_spacing = 3

		# get the height of the font
		font_height = self.font.size("Tg")[1]

		while text:
			i = 1
			# determine if the row of text will be outside our area
			if y + font_height > rect.bottom:
				break
			# determine maximum width of line
			while self.font.size(text[:i])[0] < rect.width and i < len(text):
				i += 1
			# if we've wrapped the text, then adjust the wrap to the last word      
			if i < len(text): 
				i = text.rfind(" ", 0, i) + 1
			# render the line and blit it to the surface
			image = self.font.render(text[:i], False, Settings.text_colour, bkg)

			self.screen.blit(image, (rect.left, y))
			y += font_height + line_spacing
			# remove the text we just blitted
			text = text[i:]

		return text

	def run(self):

		clock = pygame.time.Clock()
		gamerules_state = True
		current_page = 0

		while gamerules_state:
			clock.tick(10)

			self.screen.fill(Settings.background_colour)
			self.drawText(PAGES[current_page])
			arrow_text = f'< {current_page + 1} >' if current_page != 0 else f'{current_page + 1} >'
			navigation_arrows = self.font.render(arrow_text, False, Settings.text_colour)
			self.screen.blit(navigation_arrows, (
				self.screen_width/4 * 3 - navigation_arrows.get_rect().width,
				self.screen_height/3 * 2, 
			))
			display.flip()

			events = pygame.event.get()
			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gamerules_state = False
					elif event.key == pygame.K_RIGHT:
						current_page += 1
						if current_page >= len(PAGES):
							gamerules_state = False
					elif event.key == pygame.K_LEFT and current_page > 0:
						current_page -= 1
				if event.type == pygame.QUIT:
					sys.exit()
