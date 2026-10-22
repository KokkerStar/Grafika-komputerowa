from drawing import picture
from random import *

picture.ChangeSize(300, 300)
picture.Clear('#FFFFFF')
picture.ChangeScale(400)


Color1 = ['clRed', 'clGreen', 'clBlue', 'clBlack', 'clPink', 'clYellow', 'clOrange',]
Color2 = ['clLightred', 'clGLightgreen', 'clBLightblue', 'clGrey', 'clLightpink', 'clLightyellow', 'clLightorange',]


for j in range (0,11):
    r1 = randint(0, len(Color1)-1)
    r2 = randint(0, len(Color2)-1) 
    wysokosc = randint(10,50)
    szerokosc = randint(10,50)    
    for i in range(0,200):
        startx = randint(0,200)
        starty = randint(0,200)
    for k in range (0,szerokosc):
        picture.ChangePixel(startx + k, starty, Color1[r1])
    for w in range(1,wysokosc):
        picture.ChangePixel(startx, w+starty, Color1[r1])
        for k in range (1,szerokosc):
            picture.ChangePixel(startx + k, starty + w, Color1[r2])
        picture.ChangePixel(startx+szerokosc-1, w+starty, Color1[r1])   
    for k in range (0,szerokosc):
        picture.ChangePixel(startx + k, starty+wysokosc-1, Color1[r1]) 
    


#1. wylosuj rozmiar i po³o¿enie prostok¹ta
#2. zadbaj aby ca³y prostok¹t zmieœci³ siê na obrazku
#3. utwórz w pêtli 10 prostok¹tów o ró¿nych (wylosowanych)
#   rozmiarach i po³o¿eniach. Prostok¹ty mog¹ siê nak³adaæ na siebie
#4. zadbaj, aby prostok¹ty by³y kolorowane ró¿nymi zestawami kolorów