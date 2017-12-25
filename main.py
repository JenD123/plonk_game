"""
This code is used to make the window for the game, Plonk.
"""


# from pygame.org
import pygame
from pygame import Color
from pygame import display, image, mixer
import pygameMenu
from pygameMenu.locals import *
import sys

from gameplay import Gameplay


width = 720
height = 480
screen_size = (width, height) 

pygame.init()
# initialise game
screen = display.set_mode(screen_size)
display.set_caption('Plonk')
# create object (different levels) from Gameplay class and pass level details
game_level1 = Gameplay(screen, puck_speed=4, paddle_speed=2, paddle_length=80)
game_level2 = Gameplay(screen, puck_speed=6, paddle_speed=2, paddle_length=80)


def mainmenu_background():
	# fill the screen black
	screen.fill((0, 0, 0))

# create Main Menu
menu = pygameMenu.Menu(
	screen,
	window_width=width, 
	window_height=height, 
	font=pygameMenu.fonts.FONT_MUNRO,
	font_title=pygameMenu.fonts.FONT_8BIT, 
	title='Main Menu',
	menu_color_title=(255, 0, 0),	#(red, green, blue)
	bgfun=mainmenu_background,
)


# create the text for the About menu
ABOUT = ['Plonk v1.0',
'inspired by Pong',
'Created by: Jennifer Du',
'Individual Programming Project 2017-2018',	
TEXT_NEWLINE,
'[insert more text if needed here]',
]

# create About menu (submenu)
about_menu = pygameMenu.TextMenu(
	screen,
	window_width=width,
	window_height=height,
	font=pygameMenu.fonts.FONT_MUNRO,
	font_title=pygameMenu.fonts.FONT_8BIT,
	title='About',
	onclose=PYGAME_MENU_BACK,	#go back one menu
	menu_color_title=(255, 0, 0),
	bgfun=mainmenu_background,
)

for line in ABOUT:
	# add line (from ABOUT) to the menu
	about_menu.add_line(line)
#add new line when specified in ABOUT
about_menu.add_line(TEXT_NEWLINE)	


# add menu options to the Main Menu
menu.add_option('Play', game_level1.run)
menu.add_option('About', about_menu)
menu.add_option('Exit', PYGAME_MENU_EXIT) #closes application

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    menu.enable()
    menu.mainloop(events)

# if the user clicks play:
	# choose diff
	# if difficulty is easy:
		# easy
	# elif dif is medium:





