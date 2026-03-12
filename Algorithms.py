from collections import deque
from constants import *
from Node import Node
from queue import PriorityQueue


class Algorithms:
    def __init__(self, node_matrix):
        self.node_matrix = node_matrix

    def resetAlg(self):
        for row in self.node_matrix:
            for button in row:
                button.text = ""
                if button.color == AVAILABLE_COLUMN_COLOR or button.color == WAY_COLOR:
                    button.type = 0
                    button.distance = float('inf')
                    button.predecessor = None
                    button.color = AVAILABLE_COLUMN_COLOR
                elif button.color == STARTING_NODE_COLOR:
                    button.type = 0
                    button.distance = 0
                    button.predecessor = None
                    button.color = STARTING_NODE_COLOR
                elif button.color == ENDING_NODE_COLOR:
                    button.type = 0
                    button.distance = float('inf')
                    button.predecessor = None
                    button.color = ENDING_NODE_COLOR
                elif button.color == WALL_COLOR:
                    button.type = 1
                    button.distance = float('inf')
                    button.predecessor = None

    def wayBack(self, node: Node, starting_node: Node):
        """
        Rekurzivne najde cestu z end_node do starting_node a obarvuje
        
        :param node: prvni zavolani je to end_node, dalsi jsou to predchudci, proto pojmenovani pouze node
        :param starting_node: node ze ktereho jsme zacinali, tak tam chceme dorazit
        """
        if node.predecessor != starting_node:
            node.predecessor.color = WAY_COLOR
            self.wayBack(node.predecessor, starting_node)

    def processNeighborBFS(self, queue, row: int, col: int, current_node: Node): 
        neighbor_node = self.node_matrix[row][col]

        if neighbor_node.type == 0:
            neighbor_node.predecessor = current_node
            neighbor_node.distance = current_node.distance + 1
            neighbor_node.type = 10 # uzamkneme node, navstivili jsme ho

            queue.append(neighbor_node)
    

    def BFS(self, starting_node: Node, end_node: Node, purpose: str):
        """
        Najde nejkratsi cestu mezi starting_node a end_node
        
        :param node_matrix: 2Dpole buttons/node 
        :param starting_node: node ze ktereho zaciname
        :param end_node: node kde koncime
        """
        # vycisteni po vice spustenich
        self.resetAlg()

        # zacneme od startu
        queue = deque()
        starting_node.distance = 0
        starting_node.type = 10
        queue.append(starting_node)
        
        visited_count = 0

        # starting_node = node_matrix[row, col]
        found = False
        while len(queue) != 0:
            # nactu node z fronty
            node = queue.popleft()
            row = node.row
            col = node.col
            visited_count += 1

            # abychom nemeli tu samou funkci ale videli postup tak pouzijeme promennou purpose, tedy ucel jestli je to na porovnani nebo ne
            if purpose == "compare":
                node.text = str(node.distance)
                text_surf = node.font.render(node.text, True, (255, 255, 255)) 
                text_rect = text_surf.get_rect(center=node.rect.center)
                node.screen.blit(text_surf, text_rect)
            
            # pokud jsem v cili, koncim, nasel jsem cestu
            if node == end_node:
                found = True
                self.wayBack(node, starting_node)
                break
            else:
                # osetreni vystupu mimo pole
                if (row - 1) >= 0:
                    self.processNeighborBFS(queue, row - 1, col, node)
                if (row + 1) < GRID_HEIGHT:
                    self.processNeighborBFS(queue, row + 1, col, node)
                if (col - 1) >= 0:
                   self.processNeighborBFS(queue, row, col - 1, node)
                if (col + 1) < GRID_WIDTH:
                    self.processNeighborBFS(queue, row, col + 1, node)  

        if found == False:
            print("cesta neexistuje")

    def nodeScore(self, node: Node, end_node: Node) -> int:
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
    
    def processNeighborASTAR(self, pqueue, row: int, col: int, current_node: Node, end_node: Node): 
        neighbor_node = self.node_matrix[row][col]

        if neighbor_node.type == 0:
            # pokud je cesta kratsi, pouziju souseda, pokud ne, tak to nema smysl
            new_distance = current_node.distance + 1
            if new_distance < neighbor_node.distance:
                neighbor_node.distance = new_distance

                neighbor_node.predecessor = current_node
                neighbor_node_score = self.nodeScore(neighbor_node, end_node)

                pqueue.put((neighbor_node_score, neighbor_node))

    def ASTAR(self, starting_node: Node, end_node: Node, purpose: str):
        """
        Docstring for ASTAR
        velice podobne BFS
        jediny rozdil je ze pouzivame prioritni frontu

        """
        # vycisteni po vice spustenich
        self.resetAlg()

        pqueue = PriorityQueue()

        #zacneme od startu
        starting_node.distance = 0
        starting_node.type = 10
        pqueue.put((0, starting_node))
        
        visited_count = 0

        found = False
        while pqueue.empty() != True:
            # nactu node z fronty
            node = pqueue.get()[1]
            row = node.row
            col = node.col
            visited_count += 1
            node.type = 10 # uzamkneme node, musime to delat az po zpracovani


            if purpose == "compare":
                node.text = str(node.distance)
                text_surf = node.font.render(node.text, True, (255, 255, 255)) 
                text_rect = text_surf.get_rect(center=node.rect.center)
                node.screen.blit(text_surf, text_rect)

            # pokud jsem v cili, koncim, nasel jsem cestu
            if node == end_node:
                found = True
                self.wayBack(node, starting_node)
                break
            else:
                # osetreni vystupu mimo pole
                if (row - 1) >= 0:
                    self.processNeighborASTAR(pqueue, row - 1, col, node, end_node)
                if (row + 1) < GRID_HEIGHT:
                    self.processNeighborASTAR(pqueue, row + 1, col, node, end_node)
                if (col - 1) >= 0:
                    self.processNeighborASTAR(pqueue, row, col - 1, node, end_node)
                if (col + 1) < GRID_WIDTH:
                   self.processNeighborASTAR(pqueue, row, col + 1, node, end_node)

        if found == False:
            print("cesta neexistuje")

