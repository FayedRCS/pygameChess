#Set up variables images and game loop

import pygame

pygame.init()


WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess Pygame!")

#setting font and font sizes (adjustable to preferance)
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)

#Controlling the speed of the game, and number of frames to run at
timer = pygame.time.Clock()
fps = 60

# Game variables and images

# main game loop:

run = True

while run == True:

    timer.tick(fps)
    screen.fill("dark grey")


    # Event handling, gets all events (keyboard, mouse inputs, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
