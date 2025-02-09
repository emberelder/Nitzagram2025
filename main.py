import pygame

from buttons import *
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK

from classes.ImgPOST import *
from classes.TextPOST import *

posts = []
def switch_post(posts, current_post):
    temp = posts.index(current_post)+1
    if temp >= 3:
        temp -= 3
    return posts[temp]
def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    running = True
    post = Image_Post("Noa Kirel","Desert","I am on fire",'Images/noa_kirel.jpg')
    posts.append(post)
    posts.append(Text_Post("nitzan17", "Israel", "This is Text Post on Nitzagram!!", "Text Post is the best kind of post!", (201, 10, 61), (25, 112, 156)))
    posts.append(Image_Post("nitzan17","Madrid, Spain","Yes i`m on NitzaGram!",'Images/ronaldo.jpg'))

    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(click_post_button, pygame.mouse.get_pos()):
                    post = switch_post(posts, post)
                else:
                    post.mouse_pressed()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
