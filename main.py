"""
This code is used to make the window for the game, Plonk.
"""

# from pygame.org
import sys
import pygame
from pygame import Color
from pygame import display, image, mixer

from gameplay import Gameplay

width = 720
height = 480
screen_size = (width, height) 

# initialise game
screen = display.set_mode(screen_size)
display.set_caption('Plonk')

# create object (different levels) from Gameplay class and pass level details
game_level1 = Gameplay(screen, puck_speed=4, paddle_speed=2, paddle_length=80)
game_level1.run()

game_level2 = Gameplay(screen, puck_speed=6, paddle_speed=2, paddle_length=80)
game_level2.run()
