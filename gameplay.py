import pygame
from pygame import Color
from pygame import display, mixer
import sys

from puck import Puck
from paddle import Paddle
from scoreboard import Scoreboard


class Gameplay:

	# defines variables for class Gameplay
	def __init__(self, screen, puck_speed, paddle_speed, paddle_length):
		self.screen = screen
		self.puck_speed = puck_speed
		self.paddle_speed = paddle_speed
		self.paddle_length = paddle_length
		self.scoreboard = Scoreboard(screen, screen.get_rect().width, screen.get_rect().height)


	def run(self):

		self.scoreboard.reset_score()
		
		width = self.screen.get_rect().width
		height = self.screen.get_rect().height

		# create objects and data parameters
		puck = Puck(width, height, self.puck_speed, 10)
		left_paddle = Paddle(30, height, self.paddle_speed, self.paddle_length)
		right_paddle = Paddle(680, height, self.paddle_speed, self.paddle_length)

		clock = pygame.time.Clock()
		mixer.init()
		sound = mixer.Sound('boop_sound.ogg')

		# game loop
		game_playing = True
		while game_playing:
			clock.tick(60)

			# determine win/lose when either score reaches 11, then stop gameplay
			if self.scoreboard.left_score > 10:
				print('left wins')
				game_playing = False
			if self.scoreboard.right_score > 10:
				print('right wins')
				game_playing = False

			# close application when cross is pressed
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
			# check events to move paddle up or down (downkey pressed, upkey pressed)
			keys = pygame.key.get_pressed()
			if keys[pygame.K_DOWN]:
				right_paddle.move_down()
			if keys[pygame.K_UP]:
				right_paddle.move_up()
			# check events to exit gameplay
			if keys[pygame.K_ESCAPE]:
				game_playing = False

			# reset the screen to black
			self.screen.fill(Color('black'))
			# show objects
			puck.show(self.screen, self.scoreboard)
			left_paddle.show(self.screen)
			right_paddle.show(self.screen)
			self.scoreboard.show()
			# update the screen
			display.flip()

			# puck changes direction if it collides with left or right paddle
			if puck.collides_with(left_paddle):
				puck.change_x_direction('right')
				sound.play()
			elif puck.collides_with(right_paddle):
				puck.change_x_direction('left')
				sound.play()
