class Settings:

	sound_effects = True
	music = True

	background_colour = (0, 0, 0)
	text_colour = (255, 255, 255)
	menu_colour = (255, 0, 0)
	

class Theme:

	themes = {

		# 'theme_name': [(background colour), (text colour), (menu colour)] 
		# where colour is in the form (red, green, blue)
		'dark': [(0, 0, 0), (255, 255, 255), (255, 0, 0)],
		'light': [(255, 255, 255), (20, 20, 20), (255, 179, 179)],
	}

	def set_theme(theme_name):
		themes = Theme.themes
		Settings.background_colour = themes.get(theme_name)[0]
		Settings.text_colour = themes.get(theme_name)[1]
		Settings.menu_colour = themes.get(theme_name)[2]
