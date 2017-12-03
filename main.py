"""
This code is used to make the window for the game, Plonk.
"""

# from pygame.org
import pygame
from pygame import Color
from pygame import display, image

from puck import Puck
from paddle import Paddle

width = 720
height = 480
screen_size = (width, height) 

# initialise game
pygame.init()
screen = display.set_mode(screen_size)
display.set_caption('Plonk')

# create objects and data parameters
puck = Puck(width, height, 20, 10)
left_paddle = Paddle(30, height, 2, 80)
right_paddle = Paddle(680, height, 2, 80)

# game loop
while True:

	# check events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# reset the screen to black
	screen.fill(Color('black'))
	# show objects
	puck.show(screen)
	left_paddle.show(screen)
	right_paddle.show(screen)
	# update the screen
	display.flip()