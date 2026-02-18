# Uživatelská příručka

## Rozdělení aplikace
Aplikace je rozdělena do tří hlavních částí a to Menu, Scene1 a Scene2

### 1. Hlavní menu
Jako první se uživateli zobrazi hlavni menu. Yde si uyviatel vybere jakou scenu otevre prvni. Na vyber ma mezi scenou 1 a scenou 2.
* **Tlačítko Scéna 1:** Přepne uživatele do Scény 1 na samostatný algoritmus.
* **Tlačítko Scéna 2:** Přepne uživatele do Scény 2 na porovnání algoritmů BFS a A*.
* **Ukončit:** Ukončí aplikaci.

### 2. Scéna 1: Samostatný algoritmus
#### Popis sceny
V této scéně je mřížka, která slouží k interaktivní vizualizaci algoritmu. Uživatel si může pole upravit podle sebe, tzn. vytvořit vlastní bludiště. Vlastní bludiště vytvoří tím, že zvolí startovní políčko a cílové políčko, mezi kterými algoritmus najde nejkratší cestu. Dále může přidávat zdi, ty fungují jako v normálním bludišti, které známe, tedy přes zeď nelze projít. Pole má černé ohraničení.

Na pravé straně jsou tlačítka na ovládání aplikace. Prvně si uživatel vybere, jaký algoritmus chce použít, má na výběr mezi BFS (odkaz na stránku s algoritmy) a A* (odkaz na stránku s algoritmy). Poté tlačítko spustit spustí funkci, která najde a vyznačí nejkratší cestu od startovního políčka do cílového políčka pomocí zvoleného algoritmu. Uživatel poté může celé pole resetovat, tzn. vymaže veškeré zvolené zdi a nalezenou cestu. Pokud by ovšem chtěl nějaké zdi přidat či odebrat, tak klikne na tlačítko reset Algoritmus, který vymaže nalezenou cestu a dovolí uživateli znovu upravit pole.

#### Ovládání scény 1
* **Levé kliknutí myší na políčko:** Kliknutím na políčko uživatel mění jeho stav. Pokud je zelené (volné), změní se na červenou zeď. Pokud uživatel klikne na červenou zeď, změní se políčko zpátky na volné.
* **Tlačítka pro výběr algoritmu:** Jsou zde dvě tlačítka, jedno s nápisem **BFS** a druhé s **A***. Těmito tlačítky uživatel zvolí, jaký algoritmus se použije pro výpočet cesty.
* **Tlačítko SPUSTIT:** Tímto tlačítkem uživatel spustí funkci, která najde nejkratší cestu mezi startovním a cílovým políčkem pomocí zvoleného algoritmu a barevně ji v mřížce zobrazí.
* **Tlačítko RESET:** Uživateli resetuje úplně celé pole – vymaže se nalezená cesta i všechny postavené zdi a mřížka se vrátí do původního stavu.
* **Tlačítko RESET_ALG:** Toto tlačítko uživateli vymaže pouze nalezenou cestu z mřížky, ale postavené zdi nechá na místě. To dovoluje uživateli znovu upravit pole nebo zkusit jiný algoritmus na stejném bludišti.
* **SCENE 2** Slouží uživateli k přesunu na druhou scénu (Scene 2).
* **Klávesa ESC:** Slouží pro návrat uživatele zpět do hlavního menu.


### 3. Scéna 2: Porovnání BFS vs A*

#### Popis scény
Tato scéna slouží ke srovnání dvou algoritmů na stejném bludišti. Uživatel vidí dvě mřížky vedle sebe – vlevo pro algoritmus BFS a vpravo pro A*. Mřížky jsou synchronizovány, což znamená, že jakákoliv úprava zdi, kterou uživatel provede v jedné mřížce, se okamžitě projeví i v mřížce druhé. Obě pole mají černé ohraničení a stejné startovní i cílové pozice.

Po kliknutí na tlačítko ,,SPUSTIT" se spustí oba algoritmy. Aplikace v obou mřížkách vyznačí výslednou nejkratší cestu, ale především ukáže proces, jakým algoritmy pole prohledávaly.

#### Znázornění rozdílů procesu prohledání
Znázornění rozdílů je jednoduché. Každé pole, které algoritmus musel během hledání navštívit, je označeno číslem, které představuje vzdálenost daného políčka od startu. Tedy pole bez čísla nebylo navšíveno.
Pod každou mřížkou se zobrazuje text s celkovým počtem navštívených uzlů. Díky tomu uživatel přesně vidí, o kolik méně kroků udělá algoritmus A*. 

#### Ovládání scény 2
* **Levé kliknutí myší do mřížky:** Stejná funkce jako ve scéně 1. Díky synchronizaci mřížek stačí kliknout pouze do jedné z nich.
* **Tlačítko SPUSTIT:** Tímto tlačítkem se spustí oba algoritmy najednou. V mřížkách se zobrazí cesty, čísla vzdáleností a pod mřížkami se zobrazí počty průchodů.
* **Tlačítko SETUP START/END** Nastavení startovního a cílového políčka. 
* **Tlačítko Reset:** Uživateli resetuje obě mřížky, podobně jak ve scéně 1.
* **Klávesa ESC:** Slouží pro návrat uživatele zpět do hlavního menu.
* **Klávesa 1:** Přesun uživatele zpět na Scénu 1.


## Rozcestník
* [Úvod](uvod.md)
* [Uživatelská dokumentace](uzivatelskaPrirucka.md)
* [Ukázky použití](examples.md)
* [Programátorská dokumentace](programatorskaDokumentace.md)
* [Instalace](instalace.md)
