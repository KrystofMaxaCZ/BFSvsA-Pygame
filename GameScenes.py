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
        
    # Zlepseni responzivity a vizualni stranky 
    screen_width, screen_height = screen.get_size()

    # prostor pro menu
    menu_panel_width = 200
    padding = 40
    
    # prostor pro mrizku
    available_width = screen_width - menu_panel_width - (2 * padding)
    available_height = screen_height - (2 * padding)
    
    """    
    button = Button(screen,y,x,BOARDER_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 2)
    predtim, ted dynamicky  screen,y,x,BOARDER_COLOR, ...
    """

    calculated_size = min(available_width // GRID_WIDTH, available_height // GRID_HEIGHT)
    
    node_size = min(calculated_size, MAX_NODE_SIZE)
    offset_x = padding + (available_width - (node_size * GRID_WIDTH)) // 2
    offset_y = padding + (available_height - (node_size * GRID_HEIGHT)) // 2


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
        for y in range(GRID_HEIGHT):
            row = []
            for x in range(GRID_WIDTH):
                # pozici mrizky budeme pocitat dynamicky
                pos_x = offset_x + x * node_size
                pos_y = offset_y + y * node_size
                button_size = node_size - 2

                # border - vyroba okraje pole
                if (x == 0) or (x == (GRID_WIDTH - 1)) or (y == 0) or (y==(GRID_HEIGHT - 1)):
                    button = Button(screen,y,x,BOARDER_COLOR, pos_x, pos_y, button_size,button_size, 2)
                    row.append(button)
                # starting and end
                elif (x==1 and y==1) or (x==(GRID_WIDTH-2) and y==(GRID_HEIGHT-2)):
                    button = Button(screen,y,x, STARTING_NODE_COLOR, pos_x, pos_y, button_size,button_size, 0)
                    row.append(button)
                # free space - zelene policka volna 
                else:
                    button = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, pos_x, pos_y, button_size,button_size, 0)
                    row.append(button)
            node_matrix.append(row)
                
    def newGame():
        global starting_node,end_node

        node_matrix.clear()
        prepare2DGrid()
        starting_node = node_matrix[1][1]
        end_node = node_matrix[GRID_HEIGHT-2][GRID_WIDTH-2]

        return starting_node, end_node

    
    # UI pro ovladani aplikace algoritmu
    menu_x = screen_width - menu_panel_width + 20 
    start_y = 100
    button_w = 160 
    button_h = 45
    space = 15 
    

    button_bfs = Button(screen, 0, 0, ACTIVE_COLOR, menu_x, start_y, button_w, button_h, None, "BFS")
    button_astar = Button(screen, 0, 0, NOTACTIVE_COLOR, menu_x, start_y + (button_h + space),  button_w, button_h, None, "A*")
    button_start = Button(screen, 0, 0, START_BUTTON_COLOR, menu_x, start_y + 2*(button_h + space),  button_w, button_h, None, "SPUSTIT")
    button_reset = Button(screen, 0, 0, RESET_BUTTON_COLOR, menu_x, start_y + 3*(button_h + space),  button_w, button_h, None, "RESET")
    button_reset_alg = Button(screen, 0, 0, RESET_ALGO_COLOR, menu_x, start_y + 4*(button_h + space),  button_w, button_h, None, "RESET_ALG")

    button_setup_start_end = Button(screen, 0, 0, BUTTON_START_END_COLOR, offset_x, offset_y - button_h -10,  button_w + 30, button_h, None, "SETUP START/END")

    button_switch_scene = Button(screen, 0, 0, SWITCH_SCENE_COLOR, screen_width//2 - 50, 0, 100, 45, None, "SCENE 2")

    menu_buttons = [button_bfs, button_astar, button_start, button_reset, button_reset_alg, button_switch_scene,button_setup_start_end]


    
    starting_node, end_node = newGame()
    selected_algo = "BFS" # vychozi volba

    select_mode = "create_grid"
    selecting_node = "starting"

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

                elif button_switch_scene.is_clicked(event):
                    return "LEVEL2"
                elif button_setup_start_end.is_clicked(event):
                    select_mode = "start_end"
                    button_setup_start_end.color = (0,255,0)
                else:
                    if select_mode == "start_end":
                        if selecting_node == "starting":
                            for row in node_matrix:
                                for button in row:
                                    if button.is_clicked(event):
                                        starting_node.color = AVAILABLE_COLUMN_COLOR  # stary start zpet na zelenou
                                        starting_node = button                         # novy start
                                        starting_node.color = STARTING_NODE_COLOR            # prebarvit na zlutou

                                        starting_node.text = ""   
                                        selecting_node = "ending"
                        else:
                            for row in node_matrix:
                                for button in row:
                                    if button.is_clicked(event):
                                        end_node.color = AVAILABLE_COLUMN_COLOR  # stary cil zpet na zelenou
                                        end_node = button # novy cil
                                        end_node.color = STARTING_NODE_COLOR           # prebarvit na zlutou

                                        end_node.text = ""   
                                        selecting_node = "starting"
                                        select_mode = "create_grid"
                                        button_setup_start_end.color = BUTTON_START_END_COLOR
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

    
    # opet responzivita UI menu a gridu
    screen_width, screen_height = screen.get_size()


    # priprava rozmeru ohraniceni mrizek
    padding_sides = 50
    padding_top = 120
    gap_between_grids = 60 # Mezera mezi BFS a A*

    # mozne misto pro mrizku
    available_width_per_grid = (screen_width - (2 * padding_sides) - gap_between_grids) // 2 
    available_height = screen_height - padding_top - 50
    
    # responzivni velikost node (buttonu). jednoho policka
    calc_size = min(available_width_per_grid // GRID_WIDTH, available_height // GRID_HEIGHT)
    node_size = min(calc_size, MAX_NODE_SIZE)
    btn_size = node_size - 4 
    
    total_width = (GRID_WIDTH * node_size * 2) + gap_between_grids    
    grid1_x = (screen_width - total_width) // 2 #zacatek prvni mrizky
    grid2_x = grid1_x + (GRID_WIDTH * node_size) + gap_between_grids #zacatek druhe mrizkyy

    # Font pro nadpisy
    font_header = pygame.font.SysFont('Arial', 32, bold=True)
    text_bfs = font_header.render("BFS Algorithm", True, HEADER_SCENE2_COLOR)
    text_astar = font_header.render("A* Algorithm", True, HEADER_SCENE2_COLOR)

    node_matrix_1 = [] #mrizka 1 BFS
    node_matrix_2 = [] #mrizka 2 ASTAR
    
    algs1 = Algorithms(node_matrix_1)
    algs2 = Algorithms(node_matrix_2)

    def prepare2DGrid():
        for y in range(GRID_HEIGHT):
            row1 = []
            row2 = []
            
            for x in range(GRID_WIDTH):
                # pozice prvni mrizky
                p1_x = grid1_x + x * node_size
                p1_y = padding_top + y * node_size

                # pozice druhe mrizky
                p2_x = grid2_x + x * node_size
                p2_y = padding_top + y * node_size

                if (x == 0) or (x == (GRID_WIDTH - 1)) or (y == 0) or (y==(GRID_HEIGHT - 1)):
                    button1 = Button(screen,y,x,BOARDER_COLOR, p1_x, p1_y, btn_size, btn_size, 2)
                    button2 = Button(screen,y,x,BOARDER_COLOR, p2_x, p2_y, btn_size, btn_size, 2)
                    row1.append(button1)
                    row2.append(button2)
                elif (x==1 and y==1) or (x==(GRID_WIDTH-2) and y==(GRID_HEIGHT-2)):
                    button1 = Button(screen,y,x, STARTING_NODE_COLOR, p1_x, p1_y, btn_size, btn_size, 0)
                    button2 = Button(screen,y,x, STARTING_NODE_COLOR, p2_x, p2_y, btn_size, btn_size, 0)
                    row1.append(button1)
                    row2.append(button2)
                else:
                    button1 = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, p1_x, p1_y, btn_size, btn_size, 0)
                    button2 = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, p2_x, p2_y, btn_size, btn_size, 0)
                    row1.append(button1)
                    row2.append(button2)
            
            node_matrix_1.append(row1)
            node_matrix_2.append(row2)
                
    def newGame():
        global starting_node_1, end_node_1, starting_node_2, end_node_2

        node_matrix_1.clear()
        node_matrix_2.clear()
        prepare2DGrid()
        
        starting_node_1 = node_matrix_1[1][1]
        end_node_1 = node_matrix_1[GRID_HEIGHT-2][GRID_WIDTH-2]

        starting_node_2 = node_matrix_2[1][1]
        end_node_2 = node_matrix_2[GRID_HEIGHT-2][GRID_WIDTH-2]

        return starting_node_1, end_node_1, starting_node_2, end_node_2


    starting_node_1, end_node_1, starting_node_2, end_node_2 = newGame()

    # pocitani pruchodu
    bfs_pruchody = 0
    astar_pruchody = 0

    font_counter = pygame.font.SysFont('Arial', 22)

    # Tlacitka SPUSTIT a RESET pod mrizkami
    grid_bottom_y = padding_top + GRID_HEIGHT * node_size + 15
    total_grid_width = GRID_WIDTH * node_size
    button_spustit_x = grid1_x + (total_grid_width - 160) // 2
    button_reset_x = grid2_x + (total_grid_width - 160) // 2
    
    button_spustit = Button(screen, 0, 0, START_BUTTON_COLOR, button_spustit_x, grid_bottom_y + 35, 160, 45, None, "SPUSTIT")
    button_reset_s2 = Button(screen, 0, 0, RESET_BUTTON_COLOR, button_reset_x, grid_bottom_y + 35, 160, 45, None, "RESET")
    button_switch_scene = Button(screen, 0, 0, SWITCH_SCENE_COLOR, screen_width//2 - 50, 0, 100, 45, None, "SCENE 1")
    button_setup_start_end = Button(screen, 0, 0, BUTTON_START_END_COLOR, 0, 0, 200, 45, None, "SETUP START/END")

    buttons_to_print = [button_spustit, button_reset_s2, button_switch_scene, button_setup_start_end]

    def run_algorithms():
        nonlocal bfs_pruchody, astar_pruchody, starting_node_1, end_node_1, starting_node_2, end_node_2
 
        algs1.BFS(starting_node_1, end_node_1, "compare")
        algs2.ASTAR(starting_node_2, end_node_2, "compare")
        # Pocitame nody ktere maji nastavenou vzdalenost (text) - tedy byly navstiveny
        bfs_pruchody = sum(1 for row in node_matrix_1 for b in row if b.text != "")
        astar_pruchody = sum(1 for row in node_matrix_2 for b in row if b.text != "")
    
    def reset_scene():
        nonlocal starting_node_1, end_node_1, starting_node_2, end_node_2, bfs_pruchody, astar_pruchody
        starting_node_1, end_node_1, starting_node_2, end_node_2 = newGame()
        algs1.resetAlg()
        algs2.resetAlg()
        bfs_pruchody = 0
        astar_pruchody = 0

    select_mode = "create_grid"
    selecting_node = "starting"
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return "MENU"               
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_spustit.is_clicked(event):
                    run_algorithms()
                elif button_reset_s2.is_clicked(event):
                    reset_scene()
                elif button_switch_scene.is_clicked(event):
                    return "LEVEL1"
                elif button_setup_start_end.is_clicked(event):
                    select_mode = "start_end"
                    button_setup_start_end.color = (0,255,0)
                else:
                    if select_mode == "start_end":
                        if selecting_node == "starting":
                            for row in node_matrix_1:
                                for button in row:
                                    if button.is_clicked(event):
                                        starting_node_1.color = AVAILABLE_COLUMN_COLOR  # stary start zpet na zelenou
                                        starting_node_2.color = AVAILABLE_COLUMN_COLOR
                                        starting_node_1 = button                         # novy start
                                        starting_node_2 = node_matrix_2[button.row][button.col]
                                        starting_node_1.color = STARTING_NODE_COLOR            # prebarvit na zlutou
                                        starting_node_2.color = STARTING_NODE_COLOR

                                        starting_node_1.text = ""   
                                        starting_node_2.text = ""
                                        selecting_node = "ending"
                            for row in node_matrix_2:
                                for button in row:
                                    if button.is_clicked(event):
                                        starting_node_1.color = AVAILABLE_COLUMN_COLOR  # stary start zpet na zelenou
                                        starting_node_2.color = AVAILABLE_COLUMN_COLOR
                                        starting_node_1 = node_matrix_1[button.row][button.col] # novy start
                                        starting_node_2 = button 
                                        starting_node_1.color = STARTING_NODE_COLOR            # prebarvit na zlutou
                                        starting_node_2.color = STARTING_NODE_COLOR

                                        
                                        starting_node_1.text = ""   
                                        starting_node_2.text = ""

                                        selecting_node = "ending"
                                
                        else:
                            for row in node_matrix_1:
                                for button in row:
                                    if button.is_clicked(event):
                                        end_node_1.color = AVAILABLE_COLUMN_COLOR  # stary cil zpet na zelenou
                                        end_node_2.color = AVAILABLE_COLUMN_COLOR
                                        end_node_1 = button # novy cil
                                        end_node_2 = node_matrix_2[button.row][button.col] 
                                        end_node_1.color = STARTING_NODE_COLOR           # prebarvit na zlutou
                                        end_node_2.color = STARTING_NODE_COLOR

                                        end_node_1.text = ""   
                                        end_node_2.text = ""
                                        selecting_node = "starting"
                                        select_mode = "create_grid"
                                        button_setup_start_end.color = BUTTON_START_END_COLOR
                                        
                            for row in node_matrix_2:
                                for button in row:
                                    if button.is_clicked(event):
                                        end_node_1.color = AVAILABLE_COLUMN_COLOR  # stary cil zpet na zelenou
                                        end_node_2.color = AVAILABLE_COLUMN_COLOR
                                        end_node_1 = node_matrix_1[button.row][button.col]  # novy cil
                                        end_node_2 = button 
                                        end_node_1.color = STARTING_NODE_COLOR           # prebarvit na zlutou
                                        end_node_2.color = STARTING_NODE_COLOR

                                        end_node_1.text = ""   
                                        end_node_2.text = ""
                                    selecting_node = "starting"
                                    select_mode = "create_grid"
                                    button_setup_start_end.color = BUTTON_START_END_COLOR
                    else:
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
        # nadpisy mrizek
        screen.blit(text_bfs, (grid1_x, padding_top - 50))
        screen.blit(text_astar, (grid2_x, padding_top - 50))

        for row in node_matrix_1:
            for button in row:
                button.draw()

        for row in node_matrix_2:
            for button in row:
                button.draw()

        # Labely s poctem navstivenych nodu pod kazdou mrizkou
        label_bfs = font_counter.render(f"Navštíveno nodů: {bfs_pruchody}", True, HEADER_SCENE2_COLOR)
        label_astar = font_counter.render(f"Navštíveno nodů: {astar_pruchody}", True, HEADER_SCENE2_COLOR)
        screen.blit(label_bfs, (grid1_x, grid_bottom_y))
        screen.blit(label_astar, (grid2_x, grid_bottom_y))

        for button in buttons_to_print:
            button.draw()
       
        pygame.display.update()
    return "MENU"
