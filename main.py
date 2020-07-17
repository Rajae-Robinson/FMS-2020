import pygame, sys
from pygame.locals import *
pygame.init()

# Setting display caption
pygame.display.set_caption("SMS 2020")

def main():
    """
       Runs the start screen 
    """
    from Menus.select_team import SelectTeam # placing the import in a func makes python import that module only when needed
    from Menus.button import Button
    from Display.display import Display
    select_team = SelectTeam()
    display = Display()
    # start scene audio
    pygame.mixer.music.load('assets/audio/menu/main_menu.wav')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # loading main menu background
    main_menu_img = pygame.image.load("assets/sprites/Backgrounds/main-menu.png").convert()

    # creating start button
    start_btn = Button(pygame.image.load("assets/sprites/Buttons/start-game.png").convert(), (410, 380), (200, 80))

    while True:
        display.display_background(main_menu_img)
        display.display_text("Soccer Match Simulator 2020", display.font_title, (250, 300))
        start_btn.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # if start game is clicked move to SelectTeam class
            start_btn.event_handler(event, select_team.select_home)
                    
        pygame.display.update()

if __name__ == "__main__":
    main()