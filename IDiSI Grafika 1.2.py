from drawing import picture

picture.ChangeSize(150, 150)
picture.Clear('clWhite')
picture.ChangeScale(1600)

for x in range(10,51):
    picture.ChangePixel(x, 14, 'clOrange')

for x in range(10,51,2):
    picture.ChangePixel(x, 18, 'clGreen')
    
for x in range(10,51,2):
    picture.ChangePixel(x, 22, 'clBlue')
for x in range(11,51,2):
    picture.ChangePixel(x, 22, 'clCrimson')  
    
#1. zbadaj, co robi 3 argument w range? 
#   co się dzieje, gdy jest on większy niż 2?
#2. narysuj kwadrat dwukolorową linią o wzorze 
#   kreska-kropka: ##O##O##O##O##O##O##O##
#   podpowiedź: można dwa razy narysować coś
#   w tym samym miejscu -  to co rysowane drugie
#   będzie 'na wierzchu'
    
#1 pozwala on robić tzw. "step", czyli krok
#2

#Góra i dół
for x in range (15,40):
    picture.ChangePixel(x, 30, 'clRed')
for x in range (15,40):
    picture.ChangePixel(x, 54, 'clRed')

#Boki
for y in range (30,54):
    picture.ChangePixel(15 ,y , 'clRed')
for y in range (30,54):
    picture.ChangePixel(39 ,y , 'clRed')

#Krawędź górna   
for x in range (15,40,2):
    picture.ChangePixel(x, 30, 'clBlue')
    
#Krawędzie boczne
for y in range (30,53,2):
    picture.ChangePixel(15 ,y , 'clBlue')
for y in range (30,53,2):
    picture.ChangePixel(39 ,y , 'clBlue')

#Krawędź dolna
for x in range (15,40,2):
    picture.ChangePixel(x, 54, 'clBlue')




