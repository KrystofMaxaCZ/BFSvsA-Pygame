import pygame_menu
from pygame_menu import themes

class MenuScene():
    @staticmethod
    def run_menu(surface):
        result = {"next_state": "MENU"} 

        def start_level(level_name):
            result["next_state"] = level_name
            menu.disable() 

        my_theme = themes.THEME_DARK.copy()
        my_theme.title_font_size = 40
        my_theme.widget_font_size = 25
        my_theme.widget_margin = (0, 15) 

        menu = pygame_menu.Menu('Labyrinth', 600, 500, theme=my_theme)

        menu.add.label("BFS vs A*", font_size=30, font_color=(0, 255, 150))
        
        menu.add.button('Scéna 1: Samostatný Algoritmus', lambda: start_level("SCENE1"))
        menu.add.button('Scéna 2: Porovnání BFS vs A*', lambda: start_level("SCENE2"))
        
        menu.add.label("-" * 20, font_size=20)
        menu.add.button('Ukončit aplikaci', pygame_menu.events.EXIT)

        menu.mainloop(surface)
        
        return result["next_state"]