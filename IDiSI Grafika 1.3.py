from drawing import picture

picture.ChangeSize(150, 150)
picture.Clear('clWhite')
picture.ChangeScale(1600)

for x in range(10,51):
    picture.ChangePixel(x, 14, 'clGreen')
    
x = 10
while x < 51:
    picture.ChangePixel(x, 16, 'clLightGreen')
    x = x + 1  
  
    
for x in range(10,51,2):
    picture.ChangePixel(x, 18, 'clGreen')
    
x = 10
while x < 51:
    if x%2 == 0:
        picture.ChangePixel(x, 20, 'clLightGreen')
    x = x + 1
    
for x in range(10,51,2):
    picture.ChangePixel(x, 22, 'clBlue')
for x in range(11,51,2):
    picture.ChangePixel(x, 22, 'clCrimson')  
    
x = 10
while x < 51:
    if x%2 == 0:
        picture.ChangePixel(x, 24, 'clBlue')
    else:
        picture.ChangePixel(x, 24, 'clCrimson')   
    x = x + 1
    
#1. operator % daje resztę z dzielenia, jeżeli
#   reszta z dzielenia przez 2 jest zero, to liczba
#   parzysta
#2. w pętli while musi się zmieniać warunek
#   co się stanie, gdy zapomnimy zwiększyć x?
#   Zgadnij, a potem zrób eksperyment ;)
#   Podpowiedź: bezpiecznie jest eksperymentować
#   przez 'wykonaj krokowo'
#3. narysuj kwadrat którego boki będą miały
#   różne kolory zmieniające się w połowie długości
#   łącznie 4 kolory, w każdym rogu inny
#   użyj jak najmniej pętli i instrukcji 'if'
#   
#2 Program będzie działał w nieskończoność
x = 20
while x < 40:
    picture.ChangePixel(x, 30, 'clBlue')
    picture.ChangePixel(x, 49, 'clYellow')
    picture.ChangePixel(20, x+10, 'clRed')
    picture.ChangePixel(40, x+10, 'clGreen')
    x = x + 1

y = 30
while y < 40:
    picture.ChangePixel(y-10, 30, 'clRed')
    picture.ChangePixel(40, y, 'clBlue')
    picture.ChangePixel(20, y+10, 'clYellow')
    picture.ChangePixel(y, 49, 'clGreen')
    y = y + 1

