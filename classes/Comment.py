from constants import *
import pygame
from helpers import *

class Comment:
    def __init__(self, text):
        self.text = text


    def display(self, index):
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + (COMMENT_LINE_HEIGHT * index)])