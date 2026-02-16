from collections import deque
from constants import *
from Button import Button
from queue import PriorityQueue


class Algorithms:
    def __init__(self, node_matrix):
        self.node_matrix = node_matrix

    def resetAlg(self):
        for row in self.node_matrix:
            for button in row:
                if button.color == AVAILABLE_COLUMN_COLOR or button.color == WAY_COLOR:
                    button.type = 0
                    button.distance = 0
                    button.predecessor = None
                    button.color = AVAILABLE_COLUMN_COLOR
                elif button.color == STARTING_NODE_COLOR:
                    button.type = 0
                    button.distance = 0
                    button.predecessor = None
                    button.color = STARTING_NODE_COLOR
                elif button.color == WALL_COLOR:
                    button.type = 1
                    button.distance = 0
                    button.predecessor = None

    def wayBack(self, node: Button, starting_node):
        """
        Rekurzivne najde cestu z end_node do starting_node a obarvuje
        
        :param node: prvni zavolani je to end_node, dalsi jsou to predchudci, proto pojmenovani pouze node
        :param starting_node: node ze ktereho jsme zacinali, tak tam chceme dorazit
        """
        if node.predecessor != starting_node:
            node.predecessor.color = WAY_COLOR
            self.wayBack(node.predecessor, starting_node)
        
    def nodeScore(self, node, end_node) -> int:
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
    
    def BFS(self, starting_node, end_node):
        """
        Najde nejkratsi cestu mezi starting_node a end_node
        
        :param node_matrix: 2Dpole buttons/node 
        :param starting_node: node ze ktereho zaciname
        :param end_node: node kde koncime
        """
        # vycisteni po vice spustenich
        # resetAlg()
        # zacneme od startu
        self.resetAlg()
        queue = deque()
        starting_node.distance = 0
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

            # node.text = str(node.distance)
            # text_surf = node.font.render(node.text, True, (255, 255, 255)) 
            # text_rect = text_surf.get_rect(center=node.rect.center)
            # node.screen.blit(text_surf, text_rect)
            # pokud jsem v cili, koncim, nasel jsem cestu
            if node == end_node:
                print("Nasel jsem cestu")
                found = True
                self.wayBack(node, starting_node)
                break
            else:
                # osetreni vystupu mimo pole
                if (row - 1) >= 0:
                    neighbour_node = self.node_matrix[row - 1][col]
                    # type = 0 ... zelena availible space 
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.distance = node.distance + 1
                        neighbour_node.type = 10
                        queue.append(neighbour_node)
                if (row + 1) < POLE_HEIGHT:
                    neighbour_node = self.node_matrix[row + 1][col]
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.distance = node.distance + 1
                        neighbour_node.type = 10
                        queue.append(neighbour_node)
                if (col - 1) >= 0:
                    neighbour_node = self.node_matrix[row][col - 1]
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.distance = node.distance + 1
                        neighbour_node.type = 10
                        queue.append(neighbour_node)
                if (col + 1) < POLE_WIDTH:
                    neighbour_node = self.node_matrix[row][col + 1]
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.distance = node.distance + 1
                        neighbour_node.type = 10
                        queue.append(neighbour_node)    

        if found == False:
            print("cesta neexistuje")

        print("BFS: Pocet navstivenych nodes = ", pocet_pruchodu)

    def ASTAR(self, starting_node, end_node):
        """
        Docstring for ASTAR
        velice podobne BFS
        jediny rozdil je ze pouzivame prioritni frontu

        """
        # vycisteni po vice spustenich
        # resetAlg()
    # zacneme od startu
        self.resetAlg()

        pqueue = PriorityQueue()
        starting_node.distance = 0
        pqueue.put((0, starting_node))
        # indexy v 2D poli
        row = starting_node.row
        col = starting_node.col
        pocet_pruchodu = 0


        found = False
        while pqueue.empty() != True:
            # nactu node z fronty
            node = pqueue.get()[1]
            row = node.row
            col = node.col
            pocet_pruchodu += 1

            # node.text = str(node.distance)
            # text_surf = node.font.render(node.text, True, (255, 255, 255)) 
            # text_rect = text_surf.get_rect(center=node.rect.center)
            # node.screen.blit(text_surf, text_rect)
            # pokud jsem v cili, koncim, nasel jsem cestu
            if node == end_node:
                print("Nasel jsem cestu")
                found = True
                self.wayBack(node, starting_node)
                break
            else:
                # osetreni vystupu mimo pole
                if (row - 1) >= 0:
                    neighbour_node = self.node_matrix[row - 1][col]
                    # type = 0 ... zelena availible space 
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.type = 10
                        neighbour_node_score = self.nodeScore(neighbour_node, end_node)

                        pqueue.put((neighbour_node_score, neighbour_node))
                if (row + 1) < POLE_HEIGHT:
                    neighbour_node = self.node_matrix[row + 1][col]
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.type = 10
                        neighbour_node_score = self.nodeScore(neighbour_node, end_node)

                        pqueue.put((neighbour_node_score, neighbour_node))
                if (col - 1) >= 0:
                    neighbour_node = self.node_matrix[row][col - 1]
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.type = 10
                        neighbour_node_score = self.nodeScore(neighbour_node, end_node)

                        pqueue.put((neighbour_node_score, neighbour_node))
                if (col + 1) < POLE_WIDTH:
                    neighbour_node = self.node_matrix[row][col + 1]
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.type = 10
                        neighbour_node_score = self.nodeScore(neighbour_node, end_node)

                        pqueue.put((neighbour_node_score, neighbour_node))    

        if found == False:
            print("cesta neexistuje")

        print("ASTAR: Pocet navstivenych nodes = ", pocet_pruchodu)