import pygame_menu
class MenuScene():
    @staticmethod
    def run_menu(surface):
        result = {"next_state": "MENU"} 

        def start_the_game():
            result["next_state"] = "LEVEL1"
            menu.disable() 

        menu = pygame_menu.Menu('Labyrinth', 400, 400, theme=pygame_menu.themes.THEME_BLUE)
        menu.add.text_input('Name :', default='BFS vs A*')
        menu.add.button('Start', start_the_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)

        menu.mainloop(surface)
        
        return result["next_state"] 
