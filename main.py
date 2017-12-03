"""
This code is used to make the window for the game, Plonk.
"""

# from pygame.org
import sys
import pygame
from pygame import Color
from pygame import display, image, mixer

from puck import Puck
from paddle import Paddle

width = 720
height = 480
screen_size = (width, height) 

# initialise game
screen = display.set_mode(screen_size)
display.set_caption('Plonk')

# create objects and data parameters
puck = Puck(width, height, 4, 10)
left_paddle = Paddle(30, height, 2, 80)
right_paddle = Paddle(680, height, 2, 80)

clock = pygame.time.Clock()
mixer.init()
sound = mixer.Sound('boop_sound.ogg')

# game loop
while True:
	clock.tick(60)
	
	# check events to move paddle up or down (downkey pressed, upkey pressed)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# bot player controls
	puck_centre = puck.y + puck.side_length/2
	paddle_centre = left_paddle.y + left_paddle.length/2

	if puck_centre > paddle_centre:
		left_paddle.move_down()
	if puck_centre < paddle_centre:
		left_paddle.move_up()

	# human player controls
	keys = pygame.key.get_pressed()
	if keys[pygame.K_DOWN]:
		right_paddle.move_down()
	if keys[pygame.K_UP]:
		right_paddle.move_up()

	# reset the screen to black
	screen.fill(Color('black'))
	# show objects
	puck.show(screen)
	left_paddle.show(screen)
	right_paddle.show(screen)
	# update the screen
	display.flip()

	# puck changes direction if it collides with left or right paddle
	if puck.collides_with(left_paddle):
		puck.change_x_direction('right')
		sound.play()
	elif puck.collides_with(right_paddle):
		puck.change_x_direction('left')
		sound.play()


