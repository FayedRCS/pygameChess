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

white_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook", 
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", ]
#given location for each piece based on pygame grid, NOT chessgrid
white_locations = [(0,0)(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)(7,0),
                  (0,1)(1,1),(2,1),(3,1),(4,1),(5,1),(6,1)(7,1)]

black_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook", 
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", ]
#same goes for the black pieces location
black_locations = [(0,7)(1,7),(2,7),(3,7),(4,7),(5,7),(6,7)(7,7),
                  (0,6)(1,6),(2,6),(3,6),(4,6),(5,6),(6,6)(7,6)]
#we will append to these lists when pieces get captured
captured_pieces_white = []
captured_pieces_black = []


#variable to keep track of which player turn, and what action is awaited
#codes: 0 - white turn await selection; 1 - white turn piece selected; 2 - black turn await selection; 3 black turn piece selected
turn_step = 0
selection = 1000

valid_moves = []

# adding game pieces (pawns, rook, knights, bishops, queens, and kingzzz) x2




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
