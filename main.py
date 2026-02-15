import pygame
from Button import Button
from collections import deque
from queue import PriorityQueue
from Algorithms import Algorithms
from constants import *

# https://www.geeksforgeeks.org/python/pygame-tutorial/
# Initialize Pygame
pygame.init()

# Set up the game window
resolution = (1500, 800)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Labyrinth")



button_bfs = Button(screen, 0, 0, ACTIVE_COLOR, 700, 100, 90, 50, None, "BFS")
button_astar = Button(screen, 0, 0, NOTACTIVE_COLOR, 700, 170, 90, 50, None, "A*")
button_start = Button(screen, 0, 0, START_BUTTON_COLOR, 700, 240, 90, 50, None, "SPUSTIT")
button_reset = Button(screen, 0, 0, RESET_BUTTON_COLOR, 700, 310, 90, 50, None, "RESET")
button_reset_alg = Button(screen, 0, 0, RESET_ALGO_COLOR, 700, 380, 90, 50, None, "RESET_ALG")

menu_buttons = [button_bfs, button_astar, button_start, button_reset, button_reset_alg]
selected_algo = "BFS" # vychozi volba


#PRIPRAVA PROSTREDI
node_matrix = [] # 2D pole, list kde jsou prvky listy obashujici objkety typu Button

# objekt pro algorimty 
algs = Algorithms(node_matrix)

# Vyroba policek pomoci objektu Button
def prepare2DGrid():
    """
    Docstring for prepare2DGrid
    Vyroba policek pomoci objektu Button
    - rozlisujeme border/hranici a starting/end node

    objekty jsou ulozene logicky:
        - v row jsou samotne prvky buttons
        - v node_matric jsou ulozene listy row
    """
    for y in range(POLE_HEIGHT):
        row = []
        for x in range(POLE_WIDTH):
            # border - vyroba okraje pole
            if (x == 0) or (x == (POLE_WIDTH - 1)) or (y == 0) or (y==(POLE_HEIGHT - 1)):
                button = Button(screen,y,x,BOARDER_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 2)
                row.append(button)
            # starting and end
            elif (x==1 and y==1) or (x==(POLE_WIDTH-2) and y==(POLE_HEIGHT-2)):
                button = Button(screen,y,x, STARTING_NODE_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 0)
                row.append(button)
            # free space - zelene policka volna 
            else:
                button = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 0)
                row.append(button)
        node_matrix.append(row)
            
def newGame():
    global starting_node,end_node, node_matrix

    node_matrix .clear()
    prepare2DGrid()
    starting_node = node_matrix[1][1]
    end_node = node_matrix[POLE_HEIGHT-2][POLE_WIDTH-2]

    return starting_node, end_node


starting_node, end_node = newGame()
# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # kdyz klikneme na talcitko tak se zmeni jeho barva
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_bfs.is_clicked(event):
                selected_algo = "BFS"
                button_bfs.color = ACTIVE_COLOR
                button_astar.color = NOTACTIVE_COLOR

            elif button_astar.is_clicked(event):
                selected_algo = "ASTAR"
                button_astar.color = ACTIVE_COLOR
                button_bfs.color = NOTACTIVE_COLOR

            elif button_start.is_clicked(event):
                if selected_algo == "BFS":
                    algs.BFS(starting_node, end_node)
                else:
                    algs.ASTAR(starting_node, end_node)

            elif button_reset.is_clicked(event):
                starting_node, end_node = newGame()

            elif button_reset_alg.is_clicked(event):
                algs.resetAlg()

            else:
                for row in node_matrix:
                    for button in row:
                        if button.is_clicked(event):
                            if button.type == 1:
                                button.color = AVAILABLE_COLUMN_COLOR 
                                button.type = 0
                            elif button.type == 0 and button != starting_node and button!=end_node:
                                button.color = WALL_COLOR 
                                button.type = 1 
                            # vypsat o jaky button se jedna
                            button.print()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                BFS(node_matrix, starting_node, end_node)
            if event.key == pygame.K_q:
                ASTAR(node_matrix, starting_node, end_node)
            if event.key == pygame.K_r:
                # RESET
                starting_node, end_node = newGame()


    screen.fill(BACKGROUND_COLOR)
    # vykresleni mrizky
    for row in node_matrix:
        for button in row:
            button.draw()
    
    for button in menu_buttons:
        button.draw()

    pygame.display.update()

# Quit Pygame
pygame.quit()