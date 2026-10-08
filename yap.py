from drawing import picture

picture.ChangeSize(150, 150)
picture.Clear('clWhite')
picture.ChangeScale(1600)


i = 1
dx = 1
dy = 0
x = 10
y = 10
b = 40
while i < 40:
    ib = 1
    while ib < b:
        picture.ChangePixel(x, y, 'clBlue')
        x = x + dx
        y = y + dy
        ib = ib+1
    if dy == 0 and dx == 1:
        dy = 1
        dx = 0
    else:
        if dy == 1 and dx == 0:
            dy = 0
            dx = -1
        else:    
            if (dy == 0) and (dx == -1):
                dx = 0
                dy = -1
            else:    
                if (dy == -1) and (dx == 0):
                    dx = 1
                    dy = 0
    b = b - 1
                    
    i = i+1
        
#1. operatory logiczne: and=>i/oraz or=>lub not=>zaprzeczenie
#   nie jesteœ pewien kolejnoœci - sprawdŸ w dokumentacji:
#   https://www.w3schools.com/python/python_operators_precedence.asp
#   albo u¿ywaj nawiasów () ;)
#2. zamieñ w programie pêtle while na pêtle for
#3. napisz program rysuj¹cy spiralê 'w drug¹ stronê'
    
        