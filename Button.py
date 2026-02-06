import pygame

class Button:
    """
    Objekt Button, budeme vyuzivat v main.py pro prehlednejsi generovani tlacitek = pole v 2D
    takhle budeme mit kazde policko jako obejkt ktery ma sve interakce
    """
    # konstruktor tridy Button, potrebujeme vedet baru, souradnice, velikost 
    def __init__(self, screen, color, x, y, width, height, button_type):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.type = button_type # budu vyuzivat pozdeji mozna
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color,[self.x,self.y,self.width,self.height])

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Levé tlačítko
                return self.rect.collidepoint(event.pos)
        return False
    