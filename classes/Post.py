import pygame

from constants import *
from helpers import *
from buttons import *
from classes.Comment import *

class Post:
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def mouse_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_in_button(like_button, mouse_pos):
            self.likes_counter+=1
        if mouse_in_button(comment_button, mouse_pos):
            #self.display_comments()
            pass
    def display_comments(self):
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))
        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def display_username(self):
        font = pygame.font.SysFont("chalkduster.ttf", 18)
        un = font.render(self.username, True, BLACK)
        screen.blit(un, [USER_NAME_X_POS, USER_NAME_Y_POS])

    def display_location(self):
        font = pygame.font.SysFont("chalkduster.ttf", 16)
        loc = font.render(self.location, True, BLACK)
        screen.blit(loc, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

    def display_description(self):
        font = pygame.font.SysFont("chalkduster.ttf", 14)
        des = font.render(self.description, True, BLACK)
        screen.blit(des, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

    def display_likes(self):
        font = pygame.font.SysFont("chalkduster.ttf", 14)
        likes = font.render("Liked by " + str(self.likes_counter) + " users", True, BLACK)
        screen.blit(likes, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])


    def display(self):
        self.display_likes()
        self.display_description()
        self.display_location()
        self.display_username()
        self.display_comments()