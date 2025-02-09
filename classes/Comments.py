from constants import *
import pygame
from helpers import *

class Comments:
    def __init__(self, text):
        self.text = text


    def display(self, index):
        draw_comment_text_box()
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + (COMMENT_LINE_HEIGHT * self.index)])