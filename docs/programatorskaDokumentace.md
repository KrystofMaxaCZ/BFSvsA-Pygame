# Programátorská dokumentace
## Architektura kódu
Aplikace je rozdělena do několika tříd: Algorithms.py, Button.py, constants.py, GameScenes.py, main.py a MenuScene.py. Každou z nich detailněji popíši zvlášť níže.
Obecně:
 - **Třída main**: Zde se spouští celá aplikace.
 - **Třída Algorithms**: Obsahuje algoritmy BFS a A* a k nim potřebné funkce.
 - **Třída Button**: Speciální objekt, který využívám pro vykreslování políček a práci pro algoritmy.
 - **Třída GameScenes**: Obsahuje jednotlivé scény oddělené do samostatných funkcí.
 - **Třída MenuScene**: Obsahuje scénu s hlavním menu.
 - **Soubor constants**: Obsahuje konstanty.

### Main
Třída `main.py` slouží k inicializaci knihovny Pygame a nastavení okna aplikace. Hlavní částí je game loop, kde se pomocí parametru `state` řeší přepínání mezi jednotlivými scénami (menu, level 1, level 2). Každá scéna je funkce, která po svém skončení vrátí název dalšího stavu, čímž se aplikace plynule posouvá dál nebo se ukončí.

**Ukázka přepínání scén v game loopu:**
```python
state = "MENU"

# GAME LOOP
while state != "QUIT":
    if state == "MENU":
        state = menu.run_menu(screen)
    elif state == "LEVEL1":
        state = run_scene_1(screen)
    elif state == "LEVEL2":
        state = run_scene_2(screen)
```
## Třída Algorithms
Hlavním obsahem třídy `Algorithms.py` jsou dvě funkce: `BFS(...)` a `ASTAR(...)`, tedy dva algoritmy pro vyhledávání cesty.

### Algoritmus BFS
Myšlenka je taková, že z fronty načteme políčko. Prvně zpracujeme samotné políčko a následně jeho sousedy. Odkaz [zde](https://en.wikipedia.org/wiki/Breadth-first_search).

* **Zpracování políčka:** Zjistíme, jestli jsme v cíli. Pokud ano, končíme. Pokud ne, vyhodnotíme sousedy.
* **Zpracování sousedů:** Podíváme se, kdo je náš soused, a toto políčko přidáme do fronty. Přidat můžeme pouze volná políčka (tedy tam, kde pro node platí `node.type = 0`).

### Algoritmus A* (ASTAR)
Dalo by se říct, že ASTAR je ten stejný algoritmus jako BFS, který ovšem obsahuje **heuristiku**. Díky ní nemusíme procházet tolik uzlů v grafu (políček v naší mřížce). 

Myšlenka této heuristiky spočívá v tom, že místo obyčejné fronty budeme používat **prioritní frontu**, a tedy z fronty vybírat ten nejlepší prvek (s nejmenším skóre).

## Vysvětlení heuristiky
Jak jsem zmínil, ASTAR využívá prioritní frontu. Každý prvek má vlastní skóre. Pro výpočet skóre používám funkci `node_score()`, která vrací hodnotu typu `int`. Výpočet skóre je jednoduchý.

Myšlenka je taková, že si k políčku (node) vypočítáme relativní vzdálenost od cílového políčka (end\_node). K této vzdálenosti přičteme, jak daleko je políčko od startovního bodu, a výsledek je celkové skóre. V prioritní frontě pak vybíráme node s nejmenším skóre.

### Implementace výpočtu skóre
```python
 def nodeScore(self, node, end_node) -> int:
        """
        ...
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
```
### Ukázka A*
```python
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
                if (row + 1) < GRID_HEIGHT:
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
                if (col + 1) < GRID_WIDTH:
                    neighbour_node = self.node_matrix[row][col + 1]
                    if neighbour_node.type == 0:
                        neighbour_node.predecessor = node
                        neighbour_node.distance = node.distance + 1
                        neighbour_node.type = 10
                        queue.append(neighbour_node) 
```
### Pomocné funkce
Dále jsou zde funkce `wayBack(...)` a `resetAlg(...)`.

#### wayBack()
Funkci `wayBack()` používám pro rekurzivní nalezení zpáteční cesty. 
**Myšlenka:** Každý uzel (node) si pamatuje, odkud jsem se k němu dostal, tedy svého předchůdce. Zpáteční cestu najdu tak, že začneme od cílového políčka a postupně obarvujeme předchůdce.

```python
def wayBack(self, node: Button, starting_node):
    """
    Rekurzivne najde cestu z end_node do starting_node a obarvuje ji.
    ...
    """
    if node.predecessor != starting_node:
        node.predecessor.color = WAY_COLOR
        self.wayBack(node.predecessor, starting_node)
```
## Třída Button
Tato třída definuje objekt `Button`. Objekt Button slouží jak ke generování a práci s mřížkou, tak se využívá v samotných algoritmech. Obsahuje několik parametrů, které níže popíši a vysvětlím, k čemu slouží.

### Konstruktor třídy
Ve funkci `__init__` nastavujeme všechno, co políčko (node) potřebuje vědět, aby mohlo fungovat v mřížce a v algoritmu.

* **screen**: Objekt okna, na které se bude vykreslovat.
* **row**: Index řádku v `node_matrix` (v mřížce).
* **col**: Index sloupce v `node_matrix`.
* **color**: Barva políčka. Uživatel díky ní pozná, zda se jedná o zeď, volné políčko, cestu nebo hranici.
* **x**: Souřadnice na obrazovce (osa x), kam se má objekt vykreslit.
* **y**: Souřadnice na obrazovce (osa y), kam se má objekt vykreslit.
* **width**: Šířka objektu pro vykreslení.
* **height**: Výška objektu pro vykreslení.
* **button_type**: Využívá se pro rozlišení funkce políčka (viz tabulka níže).
* **text**: Textový popisek zobrazený na tlačítku.

Poté třída obsahuje další funkce, např. `draw()` pro vykreslení objektu na obrazovku a `is_clicked()`, která zjišťuje, zda bylo políčko stisknuto.

### Logika button_type

| Hodnota | Význam | Využití |
| :--- | :--- | :--- |
| **0** | Volné políčko | Prázdný prostor, kudy může algoritmus procházet. |
| **1** | Zeď | Překážka, kterou algoritmus musí obejít. |
| **2** | Border | Hranice nebo okraj mřížky. |
| **10** | Navštívený | Políčko, které již algoritmus během průchodu zpracoval. |

### Ukazka pouziti button_type (type)
```python
for row in node_matrix:
  for button in row:
      if button.is_clicked(event):
        # zmena policka po kliknuti
          if button.type == 1:
              button.color = AVAILABLE_COLUMN_COLOR 
              button.type = 0
          elif button.type == 0 and button != starting_node and button!=end_node:
              button.color = WALL_COLOR 
              button.type = 1 
```

## GameScenes
Aplikace je rozdělena na tři hlavní scény: **Menu**, **Scéna 1** a **Scéna 2**. 

### Hlavní funkce třídy
Pro zajištění chodu a přípravu prostředí využívá třída tyto klíčové funkce:

| Funkce | Popis |
| :--- | :--- |
| `run_scene_1()` | Zajišťuje kompletní logiku a běh první scény. |
| `run_scene_2()` | Zajišťuje kompletní logiku a běh druhé scény. |
| `prepare2DGrid()` | Klíčová funkce, která vygeneruje matici políček (`node_matrix`) pro zobrazení mřížky a výpočty algoritmů. |

---

### Ukázka prepare2DGrid() pro scénu 2
```python
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
```

## MenuScene
Tato třída slouží k vytvoření scény hlavního menu aplikace. Používám knihovnu `pygame-menu`.

### Ukázka run_menu()
```python
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
        
        menu.add.button('Scéna 1: Samostatný Algoritmus', lambda: start_level("LEVEL1"))
        menu.add.button('Scéna 2: Porovnání BFS vs A*', lambda: start_level("LEVEL2"))
        
        menu.add.label("-" * 20, font_size=20)
        menu.add.button('Ukončit aplikaci', pygame_menu.events.EXIT)

        menu.mainloop(surface)
        
        return result["next_state"]
```


## Rozcestník
* [Úvod](uvod.md)
* [Uživatelská dokumentace](uzivatelskaPrirucka.md)
* [Ukázky použití](examples.md)
* [Programátorská dokumentace](programatorskaDokumentace.md)
* [Instalace](instalace.md)
