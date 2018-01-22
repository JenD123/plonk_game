import pygame
from pygame import display, mixer
from pygame import font
import pygameMenu
from pygameMenu.locals import *
import sys

from puck import Puck
from paddle import Paddle
from scoreboard import Scoreboard
from settings import Settings
from specials import Wall, Boost, Coin


class Gameplay:

	# defines variables for class Gameplay
	def __init__(self, screen, puck_speed, paddle_speed, paddle_length, level):
		self.screen = screen
		self.puck_speed = puck_speed
		self.paddle_speed = paddle_speed
		self.paddle_length = paddle_length
		self.level = level
		self.scoreboard = Scoreboard(screen, screen.get_rect().width, screen.get_rect().height)

		self.special = Wall(screen.get_rect().width, screen.get_rect().height)


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
		music = mixer.Sound('8-bit-music.ogg')

		if Settings.music:
			music.play(loops=-1)

		game_playing = True
		end_state = False
		replay = False

		# game loop
		while game_playing:
			clock.tick(60)

			# if either score reaches 11, then stop gameplay
			if self.scoreboard.left_score > 10 or self.scoreboard.right_score > 10:
				game_playing = False
				end_state = True

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
			self.screen.fill(Settings.background_colour)
			# show objects
			puck.show(self.screen, self.scoreboard)
			left_paddle.show(self.screen)
			right_paddle.show(self.screen)
			self.special.show(self.screen)
			self.scoreboard.show()
			# update the screen
			display.flip()

			# puck changes direction if it collides with left or right paddle
			if puck.collides_with(left_paddle):
				puck.change_x_direction('right')
				if Settings.sound_effects:
					sound.play()
			elif puck.collides_with(right_paddle):
				puck.change_x_direction('left')
				if Settings.sound_effects:
					sound.play()

			if self.special.collides_with(puck, self.scoreboard):
				self.special.perform_action(puck, self.scoreboard)

		# certificate screen
		while end_state:
			clock.tick(10)
			
			self.screen.fill(Settings.background_colour)
			self.scoreboard.show_end_state()

			# on certificate display instructions to replay or return to menu 
			myfont = font.SysFont(pygameMenu.fonts.FONT_MUNRO, 20)
			myotherfont = font.SysFont(pygameMenu.fonts.FONT_MUNRO, 30)
			level = myotherfont.render(
				'Level: ' + self.level,
				True,
				Settings.text_colour,
			)
			instructions = myfont.render(
				'press R to replay or ESC to go back',
				True,
				Settings.text_colour,
			)
			screen_width = self.screen.get_rect().width
			screen_height = self.screen.get_rect().height
			level_width = level.get_rect().width
			level_height = level.get_rect().height
			instructions_width = instructions.get_rect().width
			instructions_height = instructions.get_rect().height
			self.screen.blit(level, (screen_width/2 - level_width/2, screen_height/2 - level_height*6))
			self.screen.blit(instructions, (screen_width/2 - instructions_width/2, screen_height/2 + instructions_height*5))
			
			display.flip()

			events = pygame.event.get()
			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						end_state = False
					if event.key == pygame.K_r:
						end_state = False
						replay = True
				if event.type == pygame.QUIT:
					sys.exit()
		
		music.stop()
		if replay:
			self.run()
