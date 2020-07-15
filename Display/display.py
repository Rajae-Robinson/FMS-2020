import pygame
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

class Display:
    """
        Handles displaying images and text to screen

    """

    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font_title = pygame.font.SysFont('Lato', 45)
        self.font_large = pygame.font.SysFont('Lato', 35)
        self.font_small = pygame.font.SysFont('Lato', 25)
        self.font_extra_small = pygame.font.SysFont('Lato', 20)

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

    """
    # game commentary function displays text then sleeps
    def game_com(self, surface, text, font, color, position):
        playersobj = Players()
        engineobj = Engine()
        score = "{} {}-{} {}".format(playersobj.home_team[0], playersobj.home_goals, playersobj.away_goals, playersobj.away_team[0])

        self.win.fill(BLACK)
        display_background(field_bkg)

        # display scores
        display_text(self.win, score, font_large, WHITE, (280, 220))

        # display commentary
        display_text(surface, text, font, color, position)

        # display minutes
        display_text(self.win, f"{engineobj.mins} minutes", font_large, WHITE, (410, 350))
        pygame.display.update()
        # time given to read commentary
        sleep(2)

    """