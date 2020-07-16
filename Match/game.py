import pygame, sys
from pygame.locals import *
import random


from Menus.button import Button
from Display.display import Display
from Menus.select_team import SelectTeam
#from Match.match import Chances, Fouls

# Initializing
pygame.init()
# Pre-initializing music
pygame.mixer.pre_init(44100, -16, 2, 512)


# Setting display caption
pygame.display.set_caption("SMS 2020")

# player who recieved yellow
yellow = []
# Vars to position text
CENTER = (410, 300)
TO_LEFT = (100, 300)

"""
class Player:
    def __init__(self):
        #selects the team lineups for both home and way
        #selects the attacking team, opposing team, player with ball, defender, and gk

        # selecting attacking team at random
        self.attacking_team = random.choice([self.home_team, self.away_team])

        # Figuring out which team is not in possession
        if self.attacking_team == self.home_team:
            self.opposing_team = self.away_team
        else:
            self.opposing_team = self.home_team

        # setting the first elevens for both attacking and opposing teams
        self.atkfirst_eleven = self.attacking_team[1:12]
        self.oppfirst_eleven = self.opposing_team[1:12]

        # players that will attack for the team in possession
        self.attackers = self.atkfirst_eleven[0:3]
        self.midfielders = self.atkfirst_eleven[3:6]

        # choosing between the forwards and midfielders
        self.position = random.choice([self.attackers, self.midfielders])
        self.player = random.choice(self.position) #player with the ball

        # if player was removed he cannot have the ball
        while self.player is None:
            self.player = random.choice(self.position)

        # Set-piece takers
        # Checking if the setpiece taker is on the field
        if self.player in self.atkfirst_eleven:
            self.fk_taker = self.attacking_team[15]
            self.ck_taker = self.attacking_team[16]
            self.pk_taker = self.attacking_team[17]
        else:
            self.fk_taker = random.choice(self.attackers)
            self.ck_taker = random.choice(self.midfielders)
            self.pk_taker = random.choice(self.attackers)

        # selecting a defender and the goalkeeper of the defending team
        self.defender = random.choice(self.oppfirst_eleven[6:10])

        # if defender is removed he cannot be selected
        while self.defender is None:
            self.defender = random.choice(self.oppfirst_eleven[6:10])

        # selecting gk
        self.gk = self.oppfirst_eleven[10]
"""



class Game:
    """
        Main game loop

    """

    def __init__(self):
        self.display = Display()
        self.select_team = SelectTeam()

    def start_scene(self):
        # main menu audio
        pygame.mixer.music.load('assets/audio/menu/main_menu.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        # loading main menu background
        main_menu_img = pygame.image.load("assets/sprites/Backgrounds/main-menu.png").convert()

        # creating start button
        start_btn = Button(pygame.image.load("assets/sprites/Buttons/start-game.png").convert(), (410, 380), (200, 80))

        while True:
            self.display.display_background(main_menu_img)
            self.display.display_text("Soccer Match Simulator 2020", self.display.font_title, (250, 300))
            start_btn.draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                # if start game is clicked move to SelectTeam class
                start_btn.event_handler(event, self.select_team.select_home)
                        
            pygame.display.update()


        def run_sim(self):
            """
                Simulator game loop
            """
            pass