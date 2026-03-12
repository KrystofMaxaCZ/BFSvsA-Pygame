# Menu
![Menu](./images/imageMenu.png)
Takto vypadá hlavní menu. Zde si uživatel vybere scénu, kterou otevře.

# Scéna 1
![Scena 1](./images/imageScena1.png)
Scénu 1 tvoří mřížka, tedy náš labyrint. Kliknutím na políčko se změní jeho role (viz uživatelská příručka). Napravo jsou tlačítka na ovládání mřížky. První dvě slouží ke zvolení algoritmu, zvolený algoritmus svítí zelenou barvou. Tlačítko Spustit poté spustí algoritmus a zobrazí se nejkratší cesta. Tlačítko Reset pak resetuje celou mřížku a reset_alg pouze vymaže nalezenou cestu, aby uživatel nemusel znovu vytvářet zdi.

Tlačítko SETUP START/END slouží k nastavení startovního políčka a cílového políčka. Uživatel klikne na tlačítko, tlačítko změní barvu, prvním kliknutím nastaví startovní políčko, druhým kliknutím nastaví cílové políčko. 

Tlačítko SCENE 2 nás přesune na scénu s porovnáním algoritmů.

## Scéna 1 - nastavení mřížky
![Scene11](./images/imageScene11.png)
Takto vypadá mřížka po nastavení zdí.
## Scéna 1 - zobrazení nejkratší cesty
![Scene12](./images/imageScene12.png)
Takto po nalezení nejkratší cesty pomocí algoritmu A*.

# Scéna 2
![Scene2](./images/imageScene2.png)
Scénu 2 tvoří tentokrát dvě mřížky, které jsou rozeznatelné pomocí horního nadpisu. Tato scéna slouží k porovnání, jak jednotlivé algoritmy mřížkou prochází a jak se liší. Tlačítka fungují stejně jako ve scéně 1.

## Scéna 2 - nastavení mřížky
![Scene21](./images/imageScena21.png)

## Scéna 2 - zobrazení porovnání
![Scene22](./images/imageScena22.png)
Zde vidíme, jak mřížka vypadá pro porovnání algoritmů. Modrá cesta značí nejkratší cestu. Číslo na políčku značí, jak daleko je od startovního políčka. Každé políčko, které má na sobě číslo, bylo navštíveno. Takto názorně vidíme, která políčka algoritmus A* nenavštíví, na rozdíl od algoritmu BFS.
Pod mřížkou je zobrazen počet navštívených políček pro každý z algoritmů.

## Scéna 2 - mřížka bez zdí
![Scene23](./images/imageScena23.png)
Příklad, kdy v mřížce není žádná zeď.
## Scéna 2 - počty průchodů BFS a A* jsou shodné?!
![Scene26](./images/imageScena26.png)
Případ, kdy A* není rychlejší než BFS.
## Scéna 2 - čím víc zdí, tím méně průchodů
![Scene24](./images/imageScena24.png)
Zajímavým poznatkem (ačkoliv docela logickým) je, že přidáním zdí vlastně zmenšujeme počet potenciálně možných políček k průchodu, tedy přidáním zdí urychlujeme výpočet, což dává smysl, jelikož na to lze pohlížet jako na nějaké omezování vyhledávacího stromu.

## Scéna 2 - další zajímavý případ
![Scene25](./images/imageScena25.png)

## Rozcestník
* [Úvod](uvod.md)
* [Uživatelská dokumentace](uzivatelskaPrirucka.md)
* [Ukázky použití](examples.md)
* [Programátorská dokumentace](programatorskaDokumentace.md)
* [Instalace](instalace.md)
