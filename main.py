import pygame
from Button import Button
# https://www.geeksforgeeks.org/python/pygame-tutorial/
# Initialize Pygame
pygame.init()

# Set up the game window
resolution = (750, 750)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Labyrinth")

# Colors
BACKGROUND_COLOR = (177, 191, 170)

POLE_WIDTH = 10
POLE_HEIGHT = 10
WALL_COLOR = (250,0,0)
BOARDER_COLOR = (0,0,0)
AVAILABLE_COLUMN_COLOR = (0,250,0)
# priprava prostredi 
buttons = []
for x in range(POLE_WIDTH):
    for y in range(POLE_HEIGHT):
        if (x == 0) or (x == (POLE_WIDTH - 1)) or (y == 0) or (y==(POLE_HEIGHT - 1)):
            button = Button(screen, BOARDER_COLOR, 200 + x * 35, 200 + y * 35, 25, 25, 3)
            buttons.append(button)
        else:
            button = Button(screen, AVAILABLE_COLUMN_COLOR, 200 + x * 35, 200 + y * 35, 25, 25, 1)
            buttons.append(button)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # kdyz klikneme na talcitko tak se zmeni jeho barva
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_clicked(event):
                    if button.type == 1:
                        button.color = WALL_COLOR # na zelenou
                        button.type = 0
                    elif button.type == 0:
                        button.color = AVAILABLE_COLUMN_COLOR # na cervenou zpatky
                        button.type = 1
    
    screen.fill(BACKGROUND_COLOR)

    for btn in buttons:
        btn.draw()
        

    # pygame.draw.rect(screen, (250,0,0),[100,100,10,10])
    # pygame.draw.rect(screen, (250,0,0),[120,100,10,10])
    # vygeneruje mrizku 25 x 25 ctverecku

    


    pygame.display.update()

# Quit Pygame
pygame.quit()