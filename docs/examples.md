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
<!-- # Menu
![Menu](./images/imageMenu.png)
Takto vypada hlavni menu. Zde si uzivatel vybere scenu, kterou otevre.

# Scena 1
![Scena 1](./images/imageScena1.png)
Scenu 1 tvori mrizka, tedy nas labyriny. Kliknutim na policko se zmeni jeho role viz. uzivatelska prirucka. Napravo jsou tlacitka na ovladani mrizky. Prvni dve slouzi ke zvoleni algoritmu, zvoleny algoritmus sviti zelenou barvou. Tlacitko spustit pote spusti algoritmus a zobrazi se nejkratsi cesta. Tlacitko reset pak resetuje celou mrizku a reset_alg pouze vymaze nalezenou cestu,  aby uzivatel nemusel znovu vytvaret zdi.

Tlacitko SETUP START/END slouzi k nastaveni startovniho policka a ciloveho policka. Uzivatel klikne na tlacitko, tlacitko zmeni barvu, prvnim kliknutim nastavi startovni policko, druhym kliknutim nastavi cilove policko. 

Tlacitko SCENE 2 nas presune na scenu s porovnanim algoritmu.

## Scena 1 - nastaveni mrizky
![Scene11](./images/imageScene11.png)
Takto vypada mrizka po nastaveni zdi.
## Scena 1 - zobrazeni nejkratsi cesty
![Scene12](./images/imageScene12.png)
Takto po nalezeni nejrkatsi cesty pomoci algoritmu A*.

# Scena 2
![Scene2](./images/imageScene2.png)
Scenu 2 tvori tentokrat dve mrizky, ktere jsou rozeznatelne pomoci horniho nadpisu. Tato scena slouzi k porovnani, jak jednotlive algoritmy mrizky prochazi a jak se lisi. Tlacitka funguji stejne jako ve scene 1.

## Scena 2 - nastaveni mrizky
![Scene21](./images/imageScena21.png)

## Scena 2 - zobrazeni porovnani
![Scene22](./images/imageScena22.png)
Zde vidime jak mrizka vypada pro porovnani algoritmu. Modra cesta znaci nejkratsi cestu. Cislo na policku znaci jak daleko je od startovniho policka. Kazde policko, ktere ma na sobe cislo bylo navstiveno. Takto nazorvne vidime, ktera policka algoritmus A* nenavstivi, narozdil od algoritmu BFS.
Pod mrizkou je zobrazen pocet navstivenych policek pro kazdy z algoritmu.

## Scena 2 - mrizka bez zdi
![Scene23](./images/imageScena23.png)
Priklad kdy v mrizce neni zadna zed.
## Scena 2 - pocty pruchodu BFS a A* jsou shodne ?!
![Scene26](./images/imageScena26.png)
Pripad, kdy A* neni rychlejsi nez BFS
## Scena 2 - cim vic zdi, tim mene pruchodu
![Scene24](./images/imageScena24.png)
Zajimavym poznatkem (ackoliv docela logickym) je, ze pridanim zdi vlastne zmensujeme pocet potencialnuch moznych policek k pruchodu, tedy pridanim zdi urychlujeme vypocet, coz dava smysl, jelikoz na to lze poglizet jako na nejake omezovani vyhledavaciho stromu.

## Scena 2 - dalsi zajimavy pripad
![Scene25](./images/imageScena25.png)


 -->


## Rozcestník
* [Úvod](uvod.md)
* [Uživatelská dokumentace](uzivatelskaPrirucka.md)
* [Ukázky použití](examples.md)
* [Programátorská dokumentace](programatorskaDokumentace.md)
* [Instalace](instalace.md)
