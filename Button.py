import pygame

class Button:
    """
    Objekt Button, budeme vyuzivat v main.py pro prehlednejsi generovani tlacitek = pole v 2D
    takhle budeme mit kazde policko jako obejkt ktery ma sve interakce
    """
    # konstruktor tridy Button, potrebujeme vedet baru, souradnice, velikost 
    def __init__(self, screen, row, col,  color, x, y, width, height, button_type, text=""):
        self.screen = screen
        self.row = row
        self.col = col
        self.predecessor = None
        self.distance = 0
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.type = button_type # budu vyuzivat pozdeji mozna
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont('Arial', 20)
    def draw(self):
        pygame.draw.rect(self.screen, self.color,[self.x,self.y,self.width,self.height])
        
        if self.text != "":
            text_surf = self.font.render(self.text, True, (255, 255, 255)) 
            text_rect = text_surf.get_rect(center=self.rect.center)
            self.screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Levé tlačítko
                return self.rect.collidepoint(event.pos)
        return False
    
    # Tento kus kodu vygenerovala AI, reseni toho jak funguje prioritni fronta kdyz maji oba prvky stejne score
    def __lt__(self, other):
        # Tímto říkáš: "Je mi jedno, které tlačítko je dřív"
        return False
    def print(self):
        print(f"Button: row:{self.row}, col:{self.col}, color: {self.color}, type:{self.type}, text:{self.text}")