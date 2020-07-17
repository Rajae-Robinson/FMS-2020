import pygame
import sys
import time
from pygame.locals import *
import random

from Display.display import Display
from Menus.select_team import SelectTeam
from Match.match_variables import MatchVariables
from Match.match import Players, Chances, Foul

class Game:
    """
        Main game loop

    """

    def __init__(self):
        self.display = Display()
        self.select_team = SelectTeam()
        self.match_vars = MatchVariables()

    def run_sim(self):
        """
            Simulator game loop
        """
        # crowd audio
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/audio/match/atm-normal.wav')
        pygame.mixer.music.play(-1)

        while self.match_vars.mins <= 90:    
            rand_events = random.randint(1, 10)

            playersobj = Players()
            
            if self.match_vars.mins == 1:
                self.display.game_com("Kick Off", self.display.font_large)
                pygame.mixer.Sound('assets/audio/match/whistle.wav').play()
                time.sleep(3)

            if self.match_vars.mins == 45:
                self.display.game_com("Half Time", self.display.font_large)
                pygame.mixer.Sound('assets/audio/match/whistle.wav').play()
                time.sleep(3)

            if self.match_vars.mins == 90:
                self.display.game_com("Full Time", self.display.font_large)
                pygame.mixer.Sound('assets/audio/match/whistle.wav').play()
                time.sleep(3)
            
            if rand_events == 1:
                Chances().play()
                self.match_vars.update_mins()
            elif rand_events == 5:
                Foul().play()
                self.match_vars.update_mins()
            else:
                Chances().idle()
                self.match_vars.update_mins()
            
            self.match_vars.update_mins()

            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()