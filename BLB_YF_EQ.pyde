pos = 640
pos2 = 360
sise = 50

def setup ():
    global pos,sise,pos2
    size (1280,720)
    background (155)
    frameRate (10)
    
    rect (100,620,100,50)
    rect (250,620,100,50)
    rect (400,620,100,50)
    rect (550,620,100,50)
    
    square (pos,pos2,sise)
    
def draw ():
    global pos,pos2,sise
    
    if (mouseX < 200) and (mouseX > 100) and (mouseY > 620) and (mouseY < 670):
        if (mouseButton == LEFT):
            clear()
            background (155)
            rect (100,620,100,50)
            rect (250,620,100,50)
            rect (400,620,100,50)
            rect (550,620,100,50)
            
            pos = pos + 10
    
            square (pos,pos2,sise)
            
    if (mouseX < 400) and (mouseX > 250) and (mouseY > 620) and (mouseY < 670):
        if (mouseButton == LEFT):
            clear()
            background (155)
            rect (100,620,100,50)
            rect (250,620,100,50)
            rect (400,620,100,50)
            rect (550,620,100,50)
            
            pos2 = pos2 - 10
    
            square (pos,pos2,sise)
            
    if (mouseX < 200) and (mouseX > 100) and (mouseY > 620) and (mouseY < 670):
        if (mouseButton == RIGHT):
            clear()
            background (155)
            rect (100,620,100,50)
            rect (250,620,100,50)
            rect (400,620,100,50)
            rect (550,620,100,50)
            
            pos = pos - 10
    
            square (pos,pos2,sise)
            
    if (mouseX < 400) and (mouseX > 250) and (mouseY > 620) and (mouseY < 670):
        if (mouseButton == RIGHT):
            clear()
            background (155)
            rect (100,620,100,50)
            rect (250,620,100,50)
            rect (400,620,100,50)
            rect (550,620,100,50)
            
            pos2 = pos2 + 10
    
            square (pos,pos2,sise)
            
    if (mouseX < 550) and (mouseX > 450) and (mouseY > 620) and (mouseY < 670):
        if (mouseButton == LEFT):
            clear()
            background (155)
            rect (100,620,100,50)
            rect (250,620,100,50)
            rect (400,620,100,50)
            rect (550,620,100,50)
            
            sise = sise + 10
    
            square (pos,pos2,sise)
            
    if (mouseX < 750) and (mouseX > 600) and (mouseY > 620) and (mouseY < 670):
        if (mouseButton == LEFT):
            if (sise > 0):
                clear()
                background (155)
                rect (100,620,100,50)
                rect (250,620,100,50)
                rect (400,620,100,50)
                rect (550,620,100,50)
            
                sise = sise - 10
            
                square (pos,pos2,sise)
            
    
            
