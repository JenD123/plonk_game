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


game = Gameplay(screen)
game.run()

