import pygame

from classes.Post import Post
from constants import *
from helpers import screen


class Image_Post(Post):
    #   this class creates an image-post object
    #   it contains a square-shape picture
    def __init__(self, username, location, description, IMG_DIR):
        super().__init__(username, location, description)
        self.IMAGE = pygame.image.load(IMG_DIR)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (POST_WIDTH, POST_HEIGHT))

    def display(self):
        screen.blit(self.IMAGE, (POST_X_POS, POST_Y_POS))
        super().display()
