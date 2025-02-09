import pygame

from classes.Post import Post
from constants import *
from helpers import *


class Text_Post(Post):
    #   this class creates a text-post object
    #   it contains text on a mono-coloured bg
    def __init__(self, username, location, description, TEXT, TEXT_COLOR, BG_COLOR):
        super().__init__(username, location, description)
        self.font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        self.BG_COLOR = BG_COLOR
        self.TEXT_TO_RENDER = from_text_to_array(TEXT)
        self.TEXT_COLOR = TEXT_COLOR
        self.POST_BG = pygame.Rect((POST_X_POS, POST_Y_POS), (POST_WIDTH, POST_HEIGHT))
    def text_display(self):
        for row in range(0, len(self.TEXT_TO_RENDER)):
            rendered_text = self.font.render(self.TEXT_TO_RENDER[row], True, self.TEXT_COLOR)
            pos = center_text(len(self.TEXT_TO_RENDER), rendered_text, row)
            screen.blit(rendered_text, pos)
    def display(self):
        super().display()
        pygame.draw.rect(screen, self.BG_COLOR, self.POST_BG)
        self.text_display()

