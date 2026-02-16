import pygame
import pygame_menu
from Button import Button
from collections import deque
from queue import PriorityQueue
from Algorithms import Algorithms
from constants import *

def run_scene_1(screen):
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
        global starting_node,end_node

        node_matrix.clear()
        prepare2DGrid()
        starting_node = node_matrix[1][1]
        end_node = node_matrix[POLE_HEIGHT-2][POLE_WIDTH-2]

        return starting_node, end_node

    
    button_bfs = Button(screen, 0, 0, ACTIVE_COLOR, 700, 100, 90, 50, None, "BFS")
    button_astar = Button(screen, 0, 0, NOTACTIVE_COLOR, 700, 170, 90, 50, None, "A*")
    button_start = Button(screen, 0, 0, START_BUTTON_COLOR, 700, 240, 90, 50, None, "SPUSTIT")
    button_reset = Button(screen, 0, 0, RESET_BUTTON_COLOR, 700, 310, 90, 50, None, "RESET")
    button_reset_alg = Button(screen, 0, 0, RESET_ALGO_COLOR, 700, 380, 90, 50, None, "RESET_ALG")

    menu_buttons = [button_bfs, button_astar, button_start, button_reset, button_reset_alg]

    starting_node, end_node = newGame()
    selected_algo = "BFS" # vychozi volba
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return "MENU" 
                if event.key == pygame.K_2: return "LEVEL2"    
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
                        algs.BFS(starting_node, end_node, "find")
                    else:
                        algs.ASTAR(starting_node, end_node, "find")

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

        screen.fill(BACKGROUND_COLOR)
        # vykresleni mrizky
        for row in node_matrix:
            for button in row:
                button.draw()
        
        for button in menu_buttons:
            button.draw()

        pygame.display.update()


def run_scene_2(screen):
    """
    Myslenka sceny 2:
        tentokrat mame dve matice tlacitek
        na jednom gridu bude videt jak prochazi algoritmus BFS
        na druhem jak to dela ASTAR

        Maji spolecne bludiste

        Takze vlastne udelame dvakrat node_matrix jen je od sebe odlisime a druhy posuneme

        A pak synchronizaci nastavovani zdi v poli
    """

    node_matrix_1 = [] 
    node_matrix_2 = [] 
    
    algs1 = Algorithms(node_matrix_1)
    algs2 = Algorithms(node_matrix_2)

    def prepare2DGrid():
        grid1_start_x = 50
        grid_width = POLE_WIDTH * 35
        gap = 50
        grid2_start_x = grid1_start_x + grid_width + gap

        for y in range(POLE_HEIGHT):
            row1 = []
            row2 = []
            for x in range(POLE_WIDTH):
                # Grid 1 logic
                if (x == 0) or (x == (POLE_WIDTH - 1)) or (y == 0) or (y==(POLE_HEIGHT - 1)):
                    button1 = Button(screen,y,x,BOARDER_COLOR, grid1_start_x + x * 35, 200 + y * 35, 33, 33, 2)
                    btn2 = Button(screen,y,x,BOARDER_COLOR, grid2_start_x + x * 35, 200 + y * 35, 33, 33, 2)
                    row1.append(button1)
                    row2.append(btn2)
                elif (x==1 and y==1) or (x==(POLE_WIDTH-2) and y==(POLE_HEIGHT-2)):
                    button1 = Button(screen,y,x, STARTING_NODE_COLOR, grid1_start_x + x * 35, 200 + y * 35, 33, 33, 0)
                    btn2 = Button(screen,y,x, STARTING_NODE_COLOR, grid2_start_x + x * 35, 200 + y * 35, 33, 33, 0)
                    row1.append(button1)
                    row2.append(btn2)
                else:
                    button1 = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, grid1_start_x + x * 35, 200 + y * 35, 33, 33, 0)
                    btn2 = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, grid2_start_x + x * 35, 200 + y * 35, 33, 33, 0)
                    row1.append(button1)
                    row2.append(btn2)
            
            node_matrix_1.append(row1)
            node_matrix_2.append(row2)
                
    def newGame():
        global starting_node_1, end_node_1, starting_node_2, end_node_2

        node_matrix_1.clear()
        node_matrix_2.clear()
        prepare2DGrid()
        
        starting_node_1 = node_matrix_1[1][1]
        end_node_1 = node_matrix_1[POLE_HEIGHT-2][POLE_WIDTH-2]

        starting_node_2 = node_matrix_2[1][1]
        end_node_2 = node_matrix_2[POLE_HEIGHT-2][POLE_WIDTH-2]

        return starting_node_1, end_node_1, starting_node_2, end_node_2

    starting_node_1, end_node_1, starting_node_2, end_node_2 = newGame()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return "MENU"
                if event.key == pygame.K_1: return "LEVEL1"
                
                if event.key == pygame.K_l:
                    # starting_node_1, end_node_1, starting_node_2, end_node_2 = newGame()
                    algs1.BFS(starting_node_1, end_node_1, "compare")
                    algs2.ASTAR(starting_node_2, end_node_2, "compare")

                if event.key == pygame.K_r:
                    starting_node_1, end_node_1, starting_node_2, end_node_2 = newGame()
                    algs1.resetAlg()
                    algs2.resetAlg()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Loop pro prvni grid
                for row in node_matrix_1:
                    for button in row:
                        if button.is_clicked(event):
                            # chci synchronizovat nastaveni zdi (cervene barvy) aby oba dva meli stejne prostredi
                            row_button = button.row
                            col_button = button.col
                            button_matrix_2 = node_matrix_2[row_button][col_button]
                            if button.type == 1:
                                button.color = AVAILABLE_COLUMN_COLOR 
                                button.type = 0
                                
                                button_matrix_2.color = AVAILABLE_COLUMN_COLOR 
                                button_matrix_2.type = 0
                            elif button.type == 0 and button != starting_node_1 and button!=end_node_1:
                                button.color = WALL_COLOR 
                                button.type = 1 
                                
                                button_matrix_2.color = WALL_COLOR 
                                button_matrix_2.type = 1 
                            button.print()
                
                # Loop pro druhy grid
                for row in node_matrix_2:
                    for button in row:
                        if button.is_clicked(event):
                            row_button = button.row
                            col_button = button.col
                            button_matrix_1 = node_matrix_1[row_button][col_button]
                            if button.type == 1:
                                button.color = AVAILABLE_COLUMN_COLOR 
                                button.type = 0

                                button_matrix_1.color = AVAILABLE_COLUMN_COLOR 
                                button_matrix_1.type = 0
                            elif button.type == 0 and button != starting_node_2 and button!=end_node_2:
                                button.color = WALL_COLOR 
                                button.type = 1 

                                button_matrix_1.color = WALL_COLOR 
                                button_matrix_1.type = 1 
                            button.print()

        screen.fill(BACKGROUND_COLOR)
        
        for row in node_matrix_1:
            for button in row:
                button.draw()

        for row in node_matrix_2:
            for button in row:
                button.draw()

        pygame.display.update()
    return "MENU"
