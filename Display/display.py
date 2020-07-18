import pygame, sys
from pygame.locals import *
import time

from Match.match_variables import MatchVariables
pygame.init()

# Setting height and width of screen
HEIGHT = 600
WIDTH = 1000

# Setting color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Vars to position text
CENTER = (410, 300)
TO_LEFT = (100, 300)

class Display:
    """
        Creates window and handles displaying images and text to screen

    """
    score = " "

    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        # fonts
        self.font_title = pygame.font.SysFont('Lato', 45)
        self.font_large = pygame.font.SysFont('Lato', 35)
        self.font_small = pygame.font.SysFont('Lato', 25)
        self.font_extra_small = pygame.font.SysFont('Lato', 20)
        self.match_vars = MatchVariables()

    def display_background(self, image):
        # Displaying background to fit screen
        self.win.blit(pygame.transform.scale(image, (WIDTH, HEIGHT)), (0, 0))

    
    def display_text(self, text, font, position):
        """
            display text to screen
        """
        msg = font.render(text, 1, WHITE)
        text_rect = msg.get_rect()
        text_rect.topleft = position
        self.win.blit(msg, text_rect)
        return (text, text_rect)

    
    def draw_image(self, image, position):
        """
            draw images to screen
        """
        self.win.blit(image, position)

    
    def game_com(self, text, font):
        """
                game commentary function displays text then sleeps
        """
        from Menus.select_team import SelectTeam
        self.select_team = SelectTeam()
        Display.score = "{} {}-{} {}".format(self.select_team.home_team[0], self.match_vars.home_goals, self.match_vars.away_goals, self.select_team.away_team[0])

        # loading the background image
        field_bkg = pygame.image.load("assets/sprites/Backgrounds/play-screen.png").convert()
        self.display_background(field_bkg)

        # display scores
        self.display_text(self.score, self.font_large, (280, 220))

        # display commentary
        self.display_text(text, font, TO_LEFT)

        # display minutes
        self.display_text(f"{self.match_vars.mins} minutes", self.font_large, (410, 350))
        pygame.display.update()
        # time given to read commentary
        time.sleep(2)

    def scoresheet(self):
        """
            Print who scored for each team at the end of game
        """
        bkg = pygame.image.load("assets/sprites/Backgrounds/background.png").convert()

        while True:
            self.display_background(bkg)
            self.display_text(self.score, self.font_large, (300, 260))

            SPACE = 40
            y = 310
            # Displaying home team scorers to the left of win
            for scorer in self.match_vars.home_scorers:
                # if list is empty; empty sequences are false
                if not self.match_vars.home_scorers:
                    self.display_text("No Scorer", self.font_small, (310, y))
                else:
                    self.display_text(f"{scorer[0]} {scorer[1]}'", self.font_small, (310, y))
                    y += SPACE

            # resetting white's original position
            y = 310

            # Displaying away team scorers to the right of win
            for scorer in self.match_vars.away_scorers:
                # if list is empty
                if not self.match_vars.away_scorers:
                    self.display_text("No Scorer", self.font_small, (580, y))
                else:
                    self.display_text(f"{scorer[0]} {scorer[1]}'", self.font_small, (580, y))
                    y += SPACE

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()



