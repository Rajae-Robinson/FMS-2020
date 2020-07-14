import pygame
from Display.display import Display
# handles creation of button images and selecting them
class Button():
    def __init__(self, image, position, size):
        self.display = Display()
        # create surface
        self.image = image

        # get image size and position
        self.rect = pygame.Rect(position, size)

    def draw(self):
        # draw image on rect
        self.display.win.blit(self.image, self.rect)

    def event_handler(self, event, function):
        # listening for event for start button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if left mouse clicked
            if event.button == 1:
                # if you hover over button
                if self.rect.collidepoint(event.pos):
                    function()