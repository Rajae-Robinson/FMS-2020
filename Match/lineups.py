import pygame, sys
from pygame.locals import *

from Display.display import Display
#from game import Game

class Lineups():
    def __init__(self, home, away):
        self.display = Display()
        self.home = home
        self.away = away

    def display_players(self):
        # lineup boxs image
        lineup_box = pygame.image.load("assets/sprites/Backgrounds/lineup.png").convert()

        # Box for home team
        self.display.draw_image(lineup_box, (20, 20))
        # Box for away team 
        self.display.draw_image(lineup_box, (600, 20))

        home_team = self.home
        away_team = self.away

        # vars to postion text
        # home and away team
        hy = 24
        ay = 24

        # Space between names
        SPACE = 40

        # Displaying home team name
        self.display.display_text(home_team[0], self.display.font_small, (22, 22))
        # Display names of players on home team
        for i in range(1, 12):
            hy += SPACE
            self.display.display_text(home_team[i], self.display.font_extra_small, (22, hy))
            
        # Displaying away team name
        display_text(away_team[0], self.display.font_small, (602, 22))
        # Display names of players on away team
        for i in range(1, 12):
            ay += SPACE
            self.display.display_text(away_team[i], self.display.font_extra_small, (602, ay))
            

    def display_lineups(self):
        # menu audio
        pygame.mixer.music.stop() # stopping main menu audio before playing
        pygame.mixer.music.load("assets/audio/match/lineup.wav")
        pygame.mixer.music.play(-1)

        #loading background
        field_bkg = pygame.image.load("assets/sprites/Backgrounds/play-screen.png").convert()

        while True:
            self.display.display_background(field_bkg)
            self.display_players()
            self.display.display_text("Press Spacebar to continue", self.display.font_small, (400, -5))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # if users presses spacebar start simulator
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # run sims
                        print("Working")

