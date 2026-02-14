import pygame
from Button import Button
from collections import deque
from queue import PriorityQueue

# https://www.geeksforgeeks.org/python/pygame-tutorial/
# Initialize Pygame
pygame.init()

# Set up the game window
resolution = (1500, 800)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Labyrinth")

# Colors
BACKGROUND_COLOR = (177, 191, 170)

POLE_WIDTH = 10
POLE_HEIGHT = 10
WALL_COLOR = (179, 2, 2)
BOARDER_COLOR = (71, 62, 44)
WAY_COLOR = (20, 86, 199)
AVAILABLE_COLUMN_COLOR = (0, 209, 42)




#PRIPRAVA PROSTREDI
node_matrix = [] # 2D pole, list kde jsou prvky listy obashujici objkety typu Button

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
                button = Button(screen,y,x, (231, 245, 39), 200 + x * 35, 200 + y * 35, 33, 33, 0)
                row.append(button)
            # free space - zelene policka volna 
            else:
                button = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 0)
                row.append(button)
        node_matrix.append(row)

def newGame():
    global starting_node,end_node, node_matrix

    node_matrix = []
    prepare2DGrid()
    starting_node = node_matrix[1][1]
    end_node = node_matrix[POLE_HEIGHT-2][POLE_WIDTH-2]

    return starting_node, end_node


def wayBack(node: Button, starting_node):
    """
    Rekurzivne najde cestu z end_node do starting_node a obarvuje
    
    :param node: prvni zavolani je to end_node, dalsi jsou to predchudci, proto pojmenovani pouze node
    :param starting_node: node ze ktereho jsme zacinali, tak tam chceme dorazit
    """
    if node.predecessor != starting_node:
        node.predecessor.color = WAY_COLOR
        wayBack(node.predecessor, starting_node)
        
# https://www.youtube.com/watch?v=HZ5YTanv5QE
def BFS(node_matrix, starting_node, end_node):
    """
    Najde nejkratsi cestu mezi starting_node a end_node
    
    :param node_matrix: 2Dpole buttons/node 
    :param starting_node: node ze ktereho zaciname
    :param end_node: node kde koncime
    """
    # zacneme od startu
    queue = deque()
    starting_node.distance = 10
    queue.append(starting_node)
    # indexy v 2D poli
    row = starting_node.row
    col = starting_node.col
    pocet_pruchodu = 0

    # starting_node = node_matrix[row, col]
    found = False
    while len(queue) != 0:
        # nactu node z fronty
        node = queue.popleft()
        row = node.row
        col = node.col
        pocet_pruchodu += 1
        # pokud jsem v cili, koncim, nasel jsem cestu
        if node == end_node:
            print("Nasel jsem cestu")
            found = True
            wayBack(node, starting_node)
            break
        else:
            # osetreni vystupu mimo pole
            if (row - 1) >= 0:
                neighbour_node = node_matrix[row - 1][col]
                # type = 0 ... zelena availible space 
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)
            if (row + 1) < POLE_HEIGHT:
                neighbour_node = node_matrix[row + 1][col]
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)
            if (col - 1) >= 0:
                neighbour_node = node_matrix[row][col - 1]
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)
            if (col + 1) < POLE_WIDTH:
                neighbour_node = node_matrix[row][col + 1]
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)    

    if found == False:
        print("cesta neexistuje")

    print("Pocet navstivenych nodes = ", pocet_pruchodu)



def nodeScore(node, end_node) -> int:
    """
    Docstring for nodeScore
    
    :param node: Description
    :param end_node: Description
    :return: vrati score toho 
    :rtype: int, score pro heruistiku
    """
    node_predecessor = node.predecessor
    node.distance = node_predecessor.distance + 1
    row_end = end_node.row
    col_end = end_node.col
    row_node = node.row
    col_node = node.col

    score = abs(row_end - row_node) + abs(col_end - col_node)
    score += node.distance
    return score
    
def ASTAR(node_matrix, starting_node, end_node):
    """
    Docstring for ASTAR
    velice podobne BFS
    jediny rozdil je ze pouzivame prioritni frontu

    """
 # zacneme od startu
    pqueue = PriorityQueue()
    starting_node.distance = 0
    pqueue.put((0, starting_node))
    # indexy v 2D poli
    row = starting_node.row
    col = starting_node.col
    pocet_pruchodu = 0

    # starting_node = node_matrix[row, col]
    found = False
    while pqueue.empty() != True:
        # nactu node z fronty
        node = pqueue.get()[1]
        row = node.row
        col = node.col
        pocet_pruchodu += 1
        # pokud jsem v cili, koncim, nasel jsem cestu
        if node == end_node:
            print("Nasel jsem cestu")
            found = True
            wayBack(node, starting_node)
            break
        else:
            # osetreni vystupu mimo pole
            if (row - 1) >= 0:
                neighbour_node = node_matrix[row - 1][col]
                # type = 0 ... zelena availible space 
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.type = 10
                    neighbour_node_score = nodeScore(neighbour_node, end_node)

                    pqueue.put((neighbour_node_score, neighbour_node))
            if (row + 1) < POLE_HEIGHT:
                neighbour_node = node_matrix[row + 1][col]
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.type = 10
                    neighbour_node_score = nodeScore(neighbour_node, end_node)

                    pqueue.put((neighbour_node_score, neighbour_node))
            if (col - 1) >= 0:
                neighbour_node = node_matrix[row][col - 1]
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.type = 10
                    neighbour_node_score = nodeScore(neighbour_node, end_node)

                    pqueue.put((neighbour_node_score, neighbour_node))
            if (col + 1) < POLE_WIDTH:
                neighbour_node = node_matrix[row][col + 1]
                if neighbour_node.type == 0:
                    neighbour_node.predecessor = node
                    neighbour_node.type = 10
                    neighbour_node_score = nodeScore(neighbour_node, end_node)

                    pqueue.put((neighbour_node_score, neighbour_node))    

    if found == False:
        print("cesta neexistuje")

    print("Pocet navstivenych nodes = ", pocet_pruchodu)
# # PREPARE GAME
# prepare2DGrid()

# starting_node = node_matrix[1][1]
# end_node = node_matrix[POLE_HEIGHT-2][POLE_WIDTH-2]

starting_node, end_node = newGame()
# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # kdyz klikneme na talcitko tak se zmeni jeho barva
        if event.type == pygame.MOUSEBUTTONDOWN:
            for row in node_matrix:
                for button in row:
                    if button.is_clicked(event):
                        if button.type == 1:
                            button.color = AVAILABLE_COLUMN_COLOR 
                            button.type = 0
                        elif button.type == 0 and button != starting_node and button!=end_node:
                            button.color = WALL_COLOR 
                            button.type = 1 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                BFS(node_matrix, starting_node, end_node)
            if event.key == pygame.K_q:
                ASTAR(node_matrix, starting_node, end_node)
            if event.key == pygame.K_r:
                starting_node, end_node = newGame()
    screen.fill(BACKGROUND_COLOR)
    
    
    for row in node_matrix:
        for button in row:
            button.draw()
        

    pygame.display.update()

# Quit Pygame
pygame.quit()