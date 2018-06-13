"""
This code is used to make the window for the game, Plonk.
"""


# from pygame.org
import pygame
from pygame import display, image, mixer
import pygameMenu
from pygameMenu.locals import *
import sys

from gameplay import Gameplay
from gamerules import GameRules
from settings import Settings, Theme


width = 720
height = 480
screen_size = (width, height) 

pygame.init()
# initialise game
screen = display.set_mode(screen_size)
display.set_caption('Plonk')



def mainmenu_background():
	# fill the screen
	screen.fill(Settings.background_colour)

# create Main Menu
menu = pygameMenu.Menu(
	screen,
	window_width=width, 
	window_height=height, 
	font=pygameMenu.fonts.FONT_MUNRO,
	font_title=pygameMenu.fonts.FONT_8BIT, 
	font_color = Settings.text_colour,
	option_shadow=False,
	title='Plonk',
	menu_color_title=Settings.menu_colour,
	menu_color=Settings.background_colour,
	bgfun=mainmenu_background,
)

# create Play submenu (level selection)
play_menu = pygameMenu.Menu(
	screen,
	window_width= width,
	window_height= height,
	font=pygameMenu.fonts.FONT_MUNRO,
	font_title=pygameMenu.fonts.FONT_8BIT,
	font_color=Settings.text_colour,
	option_shadow=False,
	title='Play',
	onclose=PYGAME_MENU_BACK,	#go back one menu
	menu_color_title=Settings.menu_colour,
	menu_color=Settings.background_colour,
	bgfun=mainmenu_background,
)

gamerules_menu = GameRules(screen)

# create the text for the About textmenu
ABOUT = [
'Plonk v1.0',
'inspired by Pong',
'Created by: Jennifer Du',
'Individual Programming Project 2017-2018',	
]

# create About textmenu
about_menu = pygameMenu.TextMenu(
	screen,
	window_width=width,
	window_height=height,
	font=pygameMenu.fonts.FONT_MUNRO,
	font_title=pygameMenu.fonts.FONT_8BIT,
	font_color = Settings.text_colour,
	option_shadow=False,
	title='About',
	onclose=PYGAME_MENU_BACK,	
	menu_color_title=Settings.menu_colour,
	menu_color=Settings.background_colour,
	bgfun=mainmenu_background,
)

for line in ABOUT:
	# add line (from ABOUT) to the textmenu
	about_menu.add_line(line)
#add new line when specified in ABOUT
about_menu.add_line(TEXT_NEWLINE)	

# create Settings submenu
settings_menu = pygameMenu.Menu(
	screen,
	window_width=width,
	window_height=height,
	font=pygameMenu.fonts.FONT_MUNRO,
	font_title=pygameMenu.fonts.FONT_8BIT,
	font_color = Settings.text_colour,
	option_shadow=False,
	title='Settings',
	onclose=PYGAME_MENU_BACK,
	menu_color_title=Settings.menu_colour,
	menu_color=Settings.background_colour,
	bgfun=mainmenu_background,
)

ALL_MENUS = [
	menu,
	play_menu,
	# does not include custom gameplay_menu
	about_menu,
	settings_menu,
]

def sound_effects(is_on):
	Settings.sound_effects = is_on

def music(is_on):
	Settings.music = is_on

def set_special(mode):
	Settings.special = mode

def set_theme(theme_name):
	Theme.set_theme(theme_name)
	try:
		for menu in ALL_MENUS:
			menu.set_background_color(Settings.background_colour)
			menu.set_font_color(Settings.text_colour)
			menu.set_title_tab_color(Settings.menu_colour)
	except Exception as error:
		print(error)

# add menu options to the Main Menu
menu.add_option('Play', play_menu)
menu.add_option('Game Rules', gamerules_menu.run)
menu.add_option('About', about_menu)
menu.add_option('Settings', settings_menu)
menu.add_option('Exit', PYGAME_MENU_EXIT) #closes application
# create object (different levels) from Gameplay class and pass level details
game_level1 = Gameplay(screen, puck_speed=4, paddle_speed=2, paddle_length=80, level='Easy')
game_level2 = Gameplay(screen, puck_speed=6, paddle_speed=2, paddle_length=80, level='Medium')
game_level3 = Gameplay(screen, puck_speed=8, paddle_speed=2, paddle_length=60, level='Hard')
game_level4 = Gameplay(screen, puck_speed=10, paddle_speed=4, paddle_length=60, level='Expert')
# add mode selector and level options to Play submenu
play_menu.add_selector(
	'Mode',
	[
		('Normal', 'NO_SPECIAL'),
		('Wall', 'WALL'),
		('Boost', 'BOOST'),
		('Coin', 'COIN'),
	],
	onchange=set_special,
	onreturn=None
)
play_menu.add_option('Easy', game_level1.run)
play_menu.add_option('Medium', game_level2.run)
play_menu.add_option('Hard', game_level3.run)
play_menu.add_option('Expert', game_level4.run)

# add settings selectors
settings_menu.add_selector(
	'Sound Effects',	#selector title
	[
		('On', True), 	#selector field value
		('Off', False),	
	],
	onchange=sound_effects, # function (above)
	onreturn=None
)
settings_menu.add_selector(
	'Music',
	[
		('On', True),
		('Off', False),
	],
	onchange=music,
	onreturn=None
)
settings_menu.add_selector(
	'Theme',
	Theme.get_list_of_themes(),
	onchange=set_theme,
	onreturn=None
)

# add return to menu options to the the submenus
play_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
about_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
settings_menu.add_option('Return to Menu', PYGAME_MENU_BACK)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    menu.enable()
    menu.mainloop(events)
