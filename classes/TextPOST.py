import pygame
from constants import *
from helpers import *
from Post import *
class Text_Post(Post):
    #   this class creates a text-post object
    #   it contains text on a mono-coloured bg
    def __init__(self):
        super(Post)
        self.font = "chalkduster.ttf"
    def post_contents(self, TEXT, TEXT_COLOR, BG_COLOR):
        self.BG_COLOR = BG_COLOR
        self.POST_CONTENTS = self.font.render(TEXT, True, TEXT_COLOR)
        self.POST_BG = pygame.rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
    def display(self):
        self.display_likes()
        self.display_description()
        self.display_location()
        self.display_username()
        self.display_comments()
        pass