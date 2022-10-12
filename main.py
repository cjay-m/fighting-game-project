import pygame 

pygame.init()

#create the game window and loop through the game instance
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# run game loop // start game
run = True 

while run:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False

#exit game
pygame.quit() 