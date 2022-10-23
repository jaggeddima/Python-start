sizEl = 20

def setup ():
    rectMode (CENTER)
    size (600,600)
    background (155)
    frameRate (10)
    rect (500, 550, 100, 50)
    rect (350, 550, 100, 50)
    ellipse (300,300,sizEl,sizEl)
    
def draw():
    global sizEl
    
    if (mouseButton == LEFT):
        if (mouseX < 550) and (mouseX > 450) and (mouseY > 525) and (mouseY < 575):
            sizEl = sizEl + 10
            
            clear()
            background (155)
            rect (500, 550, 100, 50)
            rect (350, 550, 100, 50)
            ellipse (300,300,sizEl,sizEl)
            
    if (mouseButton == LEFT):
        if (mouseX > 300) and (mouseX < 400) and (mouseY > 525) and (mouseY < 575):
            sizEl = sizEl - 10
            
            clear()
            background (155)
            rect (500, 550, 100, 50)
            rect (350, 550, 100, 50)
            ellipse (300,300,sizEl,sizEl)
            
    
            
    

        
    
