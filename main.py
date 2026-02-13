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
            button = Button(screen,y,x, (231, 245, 39), 200 + x * 35, 200 + y * 35, 33, 33, 2)
            buttons.append(button)
            row.append(button)
        # free space - zelene policka volna 
        else:
            button = Button(screen,y,x, AVAILABLE_COLUMN_COLOR, 200 + x * 35, 200 + y * 35, 33, 33, 0)
            buttons.append(button)
            row.append(button)
    node_matrix.append(row)


# https://www.youtube.com/watch?v=HZ5YTanv5QE
def findTheWay(node_matrix, starting_node):
    # zacneme od startu
    queue = deque()
    starting_node.distnace = 0
    queue.append(starting_node)
    end_node = node_matrix[9][9]
    # indexy v 2D poli
    row = starting_node.row
    col = starting_node.col

    # starting_node = node_matrix[row, col]
    found = False
    while len(queue) != 0:
        # nactu node z fronty
        node = queue.pop()
        row = node.row
        col = node.col

        # pokud jsem v cili, koncim, nasel jsem cestu
        if node == end_node:
            print("Nasel jsem cestu")
            break
        else:
            # osetreni vystupu mimo pole
            if (row - 1) >= 0:
                neighbour_node = node_matrix[row - 1][col]
                # type = 0 ... zelena availible space 
                if neighbour_node.type == 0:
                    # neighbour_node.predecessor = node
                    # neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)
            if (row + 1) < POLE_HEIGHT:
                neighbour_node = node_matrix[row + 1][col]
                if neighbour_node.type == 0:
                    # neighbour_node.predecessor = node
                    # neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)
            if (col - 1) >= 0:
                neighbour_node = node_matrix[row][col - 1]
                if neighbour_node.type == 0:
                    # neighbour_node.predecessor = node
                    # neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)
            if (col + 1) < POLE_WIDTH:
                neighbour_node = node_matrix[row][col + 1]
                if neighbour_node.type == 0:
                    # neighbour_node.predecessor = node
                    # neighbour_node.distance = node.distance + 1
                    neighbour_node.type = 10
                    queue.append(neighbour_node)    

    if found == False:
        print("cesta neexistuje")



# zkouska
findTheWay(node_matrix, node_matrix[1][1])


# for row in node_matrix:
#     for button in row:
#         print(button)

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
                            button.color = WALL_COLOR # na zelenou
                            button.type = 0
                        elif button.type == 0:
                            button.color = AVAILABLE_COLUMN_COLOR # na cervenou zpatky
                            button.type = 1 

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         buttons[12].color = (0,0,255)
        #         buttons[13].color = (0,0,255)
        #         buttons[14].color = (0,0,255)
        #         buttons[15].color = (0,0,255)
        #         buttons[25].color = (0,0,255)
        #         buttons[35].color = (0,0,255)
        #         buttons[45].color = (0,0,255)
        #         buttons[46].color = (0,0,255)
        #         buttons[47].color = (0,0,255)
        #         buttons[48].color = (0,0,255)
        #         buttons[25].color = (0,0,255)
        #         buttons[48].color = (0,0,255)
        #         buttons[58].color = (0,0,255)
        #         buttons[68].color = (0,0,255)
        #         buttons[78].color = (0,0,255)
    screen.fill(BACKGROUND_COLOR)
    
    
    for btn in buttons:
        btn.draw()
        

    pygame.display.update()

# Quit Pygame
pygame.quit()