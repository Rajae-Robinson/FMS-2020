import pygame, sys
from pygame.locals import *
import random


from Menus.button import Button
from Display.display import Display
from Menus.select_team import SelectTeam
#from Match.players import Players
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

class Game():
    """
        Main game loop

        Responsible for running game scenarios, and other functions such as draw
    """

    def __init__(self):
        self.display = Display()
        self.select_team = SelectTeam()


    def run_sim(self):
        """
            Simulator game loop
        """

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

                start_btn.event_handler(event, self.select_team.select_home)
                        
            pygame.display.update()


def main():
    Game().start_scene()

if __name__ == "__main__":
    main()