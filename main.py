from constants import *
import pygame
from MenuScene import MenuScene
from GameScenes import run_scene_1, run_scene_2

def main():
    # https://www.geeksforgeeks.org/python/pygame-tutorial/
    # Initialize Pygame
    pygame.init()
    menu = MenuScene()
    # Set up the game window
    resolution = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Labyrinth")

    state = "MENU"

    # GAME LOOP
    while state != "QUIT":
        if state == "MENU":
            state = menu.run_menu(screen)
        elif state == "LEVEL1":
            state = run_scene_1(screen)
        elif state == "LEVEL2":
            state = run_scene_2(screen)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()