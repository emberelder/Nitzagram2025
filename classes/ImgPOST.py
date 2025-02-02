import pygame
from constants import *
from helpers import screen
from Post import *
class Image_Post(Post):
    #   this class creates an image-post object
    #   it contains a square-shape picture
    def __init__(self):
        super(Post)
    def post_contents(self, IMG_DIR):
        self.IMAGE = pygame.image.load(IMG_DIR)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (POST_WIDTH, POST_WIDTH))
    def display(self):
        screen.blit(self.IMAGE, (POST_X_POS,POST_Y_POS))
        self.display_likes()
        self.display_description()
        self.display_location()
        self.display_username()
        self.display_comments()
        pass