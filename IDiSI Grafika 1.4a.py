from drawing import picture
from random import *
from time import *

#ten program wymaga YATPI v 1.5.7 lub wyższej

picture.ChangeSize(300, 300)
picture.Clear('#0080FF')
picture.ChangeScale(300)
picture.RefreshView()

def kwadrat(x,y, kolor):
    picture.ChangePixel(x+1, y, kolor)
    picture.ChangePixel(x, y+1, kolor)
    picture.ChangePixel(x+1, y+1, kolor)
    picture.ChangePixel(x, y, kolor)
seed()
lista = []
licznik = 1
while True:
    sleep(0.5)
    x = randint(0, 300)
    y = randint(0, 300)
    lista.append((x,y))
    kwadrat(x,y, 'clYellow')
    if licznik % 5 == 0:
        ox, oy = lista.pop(0)
        kwadrat(ox, oy, 'clBlue')
    licznik = licznik + 1
print(lista)
    
#1. Przetestuj program przy włączonym Autoodświeżaniu
#   i bez.
#2. Wyłącz komentarz w wierszu 13 i ponów testy
#3. Co się stanie, gdy będziemy zmieniać argument
#   funkcji sleep?
#4*.zapamiętaj współrzędne zapalonych gwiazdek, 
#   na każde 5 zapalonych zgaś jedną z poprzenich 
#3 Program będzie zmieniał szybkość generowania pikesli (im większy argument tym wolniej)

