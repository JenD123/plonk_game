"""
This code is used to make the window for the game, Plonk.
"""


# pygame.org
import pygame
from pygame import Color
from pygame import display, image


width = 720
height = 480
screen_size = (width, height) 

# initialisa game
pygame.init()
screen = display.set_mode(screen_size)
display.set_caption('Plonk')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# reset the screen to black
	screen.fill(Color('black'))
	# update entire screen
	display.flip()