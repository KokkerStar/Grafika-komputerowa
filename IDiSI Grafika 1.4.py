from drawing import picture
from random import *

picture.ChangeSize(300, 300)
picture.Clear('clBlue')
picture.ChangeScale(400)

def Gwiazdka1(x,y):
    picture.ChangePixel(x, y, 'clYellow')
    picture.ChangePixel(x+1, y, 'clYellow')
    picture.ChangePixel(x+1, y+1, 'clYellow')
    picture.ChangePixel(x+2, y+1, 'clYellow')
def Gwiazdka2(x,y):
    picture.ChangePixel(x, y, 'clYellow')
    picture.ChangePixel(x, y+1, 'clYellow')
    picture.ChangePixel(x+1, y+1, 'clYellow')
    picture.ChangePixel(x-1, y+1, 'clYellow')
    picture.ChangePixel(x, y+2, 'clYellow')
def Gwiazdka3(x,y):
    picture.ChangePixel(x, y, 'clOrange')
    picture.ChangePixel(x+2, y, 'clOrange')
    picture.ChangePixel(x+1, y+1, 'clOrange')
    picture.ChangePixel(x, y+2, 'clOrange')
    picture.ChangePixel(x+2, y+2, 'clOrange')
def Gwiazdka4(x,y):
    picture.ChangePixel(x, y, 'clOrange')
    picture.ChangePixel(x+1, y, 'clOrange')
    picture.ChangePixel(x+2, y, 'clOrange')
    picture.ChangePixel(x, y+1, 'clOrange')
    picture.ChangePixel(x+1, y+1, 'clOrange')
    picture.ChangePixel(x+2, y+1, 'clOrange')
    picture.ChangePixel(x, y+2, 'clOrange')
    picture.ChangePixel(x+1, y+2, 'clOrange')
    picture.ChangePixel(x+2, y+2, 'clOrange')
seed(103)
i = 0
while i < 900:
    #if random()<0.5:
    if i % 2 == 0:
        x = randint(0, 300)
        y = randint(0, 300)
        Gwiazdka1(x,y)
        Gwiazdka2(x,y+5)
    else:
        x = randint(0, 300)
        y = randint(0, 300)
        Gwiazdka4(x,y)
        Gwiazdka3(x+10,y+5)
    i = i + 1


#1. zwiększ liczbę gwiazdek
#2. zmień kolory, żeby efekt bardziej przypominał niebo
#3. usuń 101 z wywołania seed. Co się zmieniło? Czy wartość
#   101 miała jakieś znaczenie?
#4. czy i jest potrzebne w pętli for? Co się stanie,
#   gdy zastąpisz je znakiem _ (podkreślnik)?
#5. dodaj gwiazdki w innym kolorze, użyj pętli while
#6. wiedząc, że random() generuje liczby losowe
#   z zakresu <0,1) napisz kod, który wygeneruje
#   gwiazdki 2 kolorów równo rozłożone na niebie ;)
#   Czy w ogóle trzeba do tego używać random() ?
#7. zrób niebo z gwiazdami różnej wielkości i kształtu, np.
# 
#   oo    o    o o   ooo
#   oo   ooo    o    ooo
#         o    o o   ooo
#3 Zmienia sie sekwencja (ustawienie gwaizd)
#4 Jest potrzebne żeby pętla się urochomiła jednak i możemy zastąpić innym obojętnym znakiem
#5 Można użyć funkcji if i % 2 == 0.

