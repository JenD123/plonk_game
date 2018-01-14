class Settings:

	sound_effects = True
	music = True

	background_colour = (0, 0, 0)
	text_colour = (255, 255, 255)
	menu_colour = (255, 0, 0)
	

class Theme:

	themes = {

		# 'theme_name': [(background colour), (text colour), (menu tab colour)] 
		# where colour is in the form (red, green, blue)
		'dark': [(0, 0, 0), (255, 255, 255), (255, 0, 0)],
		'light': [(255, 255, 255), (20, 20, 20), (255, 179, 179)],
		'grey': [(100, 100, 100), (200, 200, 200), (70, 70, 70)],
		'vintage': [(114, 107, 86), (202, 203, 204), (67, 60, 56)],
		'cream': [(252, 238, 220), (107, 92, 97), (207, 196, 182)],
		'rainbow': [(182, 58, 78), (228, 212, 123), (13, 181, 180)],
		'starry night': [(33, 73, 81), (235,204,106), (60,101,114)],
		'solar': [(249,127,68), (253,225,153), (238,108,74)],
		'lime': [(73,187,130), (243,241,188), (45, 134, 89)],
		'cobalt': [(16,63,111), (234,240,235), (19,33,48)],
	}

	# assign colours to the bg, text, tab for chosen theme
	def set_theme(theme_name):
		themes = Theme.themes
		Settings.background_colour = themes.get(theme_name)[0]
		Settings.text_colour = themes.get(theme_name)[1]
		Settings.menu_colour = themes.get(theme_name)[2]

	# return a selector name and a list of tuples where each tuple is a colour in the theme (for selectors in main.py)
	def get_list_of_themes():
		all_themes = []
		for theme in Theme.themes:
			theme_tuple = (theme.capitalize(), theme)
			all_themes.append(theme_tuple)
		return all_themes
		