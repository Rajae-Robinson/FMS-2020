import pygame, sys
import random

# Initializing
pygame.init()
# Pre-initializing music
pygame.mixer.pre_init(44100, -16, 2, 512)

# Setting color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Setting height and width of screen
HEIGHT = 600
WIDTH = 1000

# Setting display surface
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(WHITE)
pygame.display.set_caption("SMS 2020")

# Fonts
font_title = pygame.font.SysFont('Lato', 45)
font_large = pygame.font.SysFont('Lato', 35)
font_small = pygame.font.SysFont('Lato', 25)
font_extra_small = pygame.font.SysFont('Lato', 20)

# game vars and other vars
home = ""
away = ""
# player who recieved yellow
yellow = []
# Vars to position text
CENTER = (410, 300)
TO_LEFT = (100, 300)

# loading main background
background = pygame.image.load("assets/sprites/Backgrounds/background.png").convert()

class Game():
	"""
		Main game loop

		Responsible for running game scenarios, and other functions such as draw
	"""

	def __init__(self):
		pass

	def run(self):
		clock = pygame.time.Clock()

	def display_background(image):
    # Displaying background to fit screen
    win.blit(pygame.transform.scale(image, (WIDTH, HEIGHT)), (0, 0))

	# display text to screen
	def display_text(surface, text, font, color, position):
	    msg = font.render(text, 1, color)
	    text_rect = msg.get_rect()
	    text_rect.topleft = position
	    surface.blit(msg, text_rect)
	    return (text, text_rect)

	# game commentary function displays text then sleeps
	def game_com(surface, text, font, color, position):
	    playersobj = Players()
	    engineobj = Engine()
	    score = "{} {}-{} {}".format(playersobj.home_team[0], playersobj.home_goals, playersobj.away_goals, playersobj.away_team[0])

	    win.fill(BLACK)
	    display_background(field_bkg)

	    # display scores
	    display_text(win, score, font_large, WHITE, (280, 220))

	    # display commentary
	    display_text(surface, text, font, color, position)

	    # display minutes
	    display_text(win, f"{engineobj.mins} minutes", font_large, WHITE, (410, 350))
	    pygame.display.update()
	    # time given to read commentary
	    sleep(2)

	# draw images to screen
	def draw_image(surface, image, position):
	    surface.blit(image, position)

