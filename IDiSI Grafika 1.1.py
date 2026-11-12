from drawing import picture

picture.ChangeSize(150, 150)
picture.Clear('clWhite')
picture.ChangeScale(1600)

picture.ChangePixel(10, 10, 'clBlack')
picture.ChangePixel(11, 10, 'clBlack')
picture.ChangePixel(12, 10, 'clBlack')
picture.ChangePixel(13, 10, 'clBlack')
picture.ChangePixel(14, 10, 'clBlack')
picture.ChangePixel(15, 10, 'clBlack')
picture.ChangePixel(16, 10, 'clBlack')

for x in range(10,17):
    picture.ChangePixel(x, 12, 'clRed')
    
for x in range(10,17):
    picture.ChangePixel(x, 14, 'clGreen')
    
#1. kolor jest opisany słownie: clAngielskaNazwaKoloru
#   taki kolor działa tylko w YATPI i jego 'picture' ;)
#2. zamiast pisać wiele razy tą samą instrukcję
#   używamy pętli: for zmienna_sterująca in zakres
#3. zakres definiujemy za pomocą range(od,do)
#4. popatrz na wynik działania programu i powiedz, 
#   czy zakres uwzględnia wartość równą 'do'?
#5. wykonaj program krokowo, podglądając wartość x
#6. narysuj linię pionową w kolorze zielonym

#4 Nie uwzględnia wartości do
