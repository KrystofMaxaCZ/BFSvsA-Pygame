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


# priprava prostredi 
buttons = []
for x in range(25):
    for y in range(25):
        button = Button(screen, (250,0,0), 100 + x * 15, 100 + y * 15, 10, 10, 1)
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
                        button.color = (0, 255, 0) # na zelenou
                        button.type = 0
                    elif button.type == 0:
                        button.color = (255, 0, 0) # na cervenou zpatky
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