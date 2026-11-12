from drawing import picture

picture.ChangeSize(50, 50)
picture.Clear('#FFFFFF')
picture.ChangeScale(1850)

picture.ChangePixel(10, 10, '#000000')
picture.ChangePixel(11, 11, '#211332')
picture.ChangePixel(40, 10, '#FF0000')
picture.ChangePixel(41, 11, '#FF3039')
picture.ChangePixel(10, 40, '#00ff00')
picture.ChangePixel(11, 41, '#13ff90')
picture.ChangePixel(40, 40, '#0000ff')
picture.ChangePixel(41, 41, '#4500ff')
print("Oto obrazek z 4 punktami kontrolnymi")

#tutaj zadania i uwagi do programu, których nie ma w wersji testowej:
#możesz zgadywać, ale potem sprawdź dokładnie!!! ;)
#0. dopasuj skalę (1600) do parametrów swojego monitora,
#   zobacz jak wygląda obrazek w skali 100 :)
#1. kolor ma format #rrggbb, wartości 0-255 ale zapisane
#   szestnastkowo. Użyj kalkulatora, żeby je przeliczać.
#2. w którym rogu jest początek układu współrzędnych?
#3. w którą stronę rosną wartości na osiach pionowej i poziomej?
#4. jaka jest najmniejsza wartość x i y którą można wpisać, 
#   żeby punkt był widoczny?
#5. jaka jest największa wartość x i y którą można wpisać, 
#   żeby punkt był widoczny?
#6. dołóż kilka punktów w dowolnych miejscach, poeksperymentuj z ich kolorami

#1 0,0,0 - Czarny 255,0,0 - czerwony  0,255,0 - Zielony, 0,0,255 - Niebieski
#2 Lewy górny
#3 X rosną w prawo, Y rosną w dół
#4 Najmniejsze (x = 0, y = 0)
#5 Najwuększe (x = 49, y = 49)



