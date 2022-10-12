import pygame 


pygame.init()

#create the game window and loop through the game instance
SCREEN_WIDTH = 1428
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#load stage 
bg_image = pygame.image.load("assets/images/backgrounds/placeholder-bg.gif")

#function to run the background / stage
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))


# run game loop // start game
run = True 

while run:
    
    #draw the stage
    draw_bg() 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False

    #update display 
    pygame.display.update()

#exit game
pygame.quit() 