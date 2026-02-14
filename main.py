import pygame
from Button import Button
from collections import deque

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




#PRIPRAVA PROSTREDI

buttons = [] # nepotrebne, smaze se 
node_matrix = [] # 2D pole, list kde jsou prvky listy obashujici objkety typu Button

# Vyroba policek pomoci objektu Button
for y in range(POLE_HEIGHT):
    row = []
    for x in range(POLE_WIDTH):
        # border - vyroba okraje pole
        if (x == 0) or (x == (POLE_WIDTH - 1)) or (y == 0) or (y==(POLE_HEIGHT - 1)):
            button = Button(screen,y,x,BOARDER_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 2)
            buttons.append(button) # smazat
            row.append(button)
        # border - vyroba okraje pole
        elif (x==1 and y==1) or (x==(POLE_WIDTH-2) and y==(POLE_HEIGHT-2)):
            button = Button(screen,y,x, (231, 245, 39), 200 + x * 35, 200 + y * 35, 33, 33, 0)
            buttons.append(button)
            row.append(button)
        # free space - zelene policka volna 
        else:
            button = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 0)
            buttons.append(button)
            row.append(button)
    node_matrix.append(row)


def wayBack(node: Button, starting_node):
    if node.predecessor != starting_node:
        node.predecessor.color = (0,0,255)
        wayBack(node.predecessor, starting_node)

# https://www.youtube.com/watch?v=HZ5YTanv5QE
def findTheWay(node_matrix, starting_node, end_node):
    # zacneme od startu
    queue = deque()
    starting_node.distnace = 10
    queue.append(starting_node)
    # indexy v 2D poli
    row = starting_node.row
    col = starting_node.col

    # starting_node = node_matrix[row, col]
    found = False
    while len(queue) != 0:
        # nactu node z fronty
        node = queue.popleft()
        row = node.row
        col = node.col

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




# zkouska
# findTheWay(node_matrix, node_matrix[1][1])
# print()
# print()
# print()
# for row in node_matrix:
#     for button in row:
#         print(f"{button.distance} ", end="")
#     print()

# print()
# print()
# for row in node_matrix:
#     for button in row:
#         print(button)

# GAME LOOP
starting_node = node_matrix[1][1]
end_node = node_matrix[POLE_HEIGHT-2][POLE_WIDTH-2]
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
                findTheWay(node_matrix, node_matrix[1][1], node_matrix[8][8])
    screen.fill(BACKGROUND_COLOR)
    
    
    for btn in buttons:
        btn.draw()
        

    pygame.display.update()

# Quit Pygame
pygame.quit()