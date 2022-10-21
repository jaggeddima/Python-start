
def setup ():
    size (700,600)
    rectMode (CENTER)
    background (100)
    rect (300,300,100,50)
    rect (300,400,100,50)
    rect (300,200,100,50)
    rect (150,200,100,50)
    rect (150,300,100,50)
    rect (150,400,100,50)
    rect (450,400,100,50)
    rect (450,300,100,50)
    rect (450,200,100,50)
    rect (225,500,250,50)
    
def draw ():
    if (mouseX > 250) and (mouseX < 350) and (mouseY < 325) and (mouseY > 275):
          if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (300,300,100,50)
            
    if (mouseX > 250) and (mouseX < 350) and (mouseY < 425) and (mouseY > 375):
        if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (300,400,100,50)
            
    if (mouseX > 250) and (mouseX < 350) and (mouseY < 225) and (mouseY > 175):
         if (mouseButton == LEFT):
             fill (random(0,255),random(0,255),random(0,255))
             rect (300,200,100,50)

    if (mouseX > 100) and (mouseX < 200) and (mouseY < 225) and (mouseY > 175):
        if (mouseButton == LEFT):
             fill (random (0,255),random (0,255),random (0,255))
             rect (150,200,100,50)
             
    if (mouseX > 100) and (mouseX < 200) and (mouseY < 325) and (mouseY > 275):
        if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (150,300,100,50)
            
    if (mouseX > 100) and (mouseX < 200) and (mouseY < 425) and (mouseY > 375):
        if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (150,400,100,50)
            
    if (mouseX > 400) and (mouseX < 500) and (mouseY < 425) and (mouseY > 375):
        if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (450,400,100,50)
            
    if (mouseX > 400) and (mouseX < 500) and (mouseY < 325) and (mouseY > 275):
        if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (450,300,100,50)
            
    if (mouseX > 400) and (mouseX < 500) and (mouseY < 225) and (mouseY > 175):
        if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (450,200,100,50)
            
    if (mouseX > 112.5) and (mouseX < 337.5) and (mouseY < 525) and (mouseY > 475):
        if (mouseButton == LEFT):
            fill (random (0,255),random (0,255),random (0,255))
            rect (225,500,250,50)
            
    if (mouseButton == RIGHT):
        clear()
        background (100)
        fill (255)
        rect (300,300,100,50)
        rect (300,400,100,50)
        rect (300,200,100,50)
        rect (150,200,100,50)
        rect (150,300,100,50)
        rect (150,400,100,50)
        rect (450,400,100,50)
        rect (450,300,100,50)
        rect (450,200,100,50)
        rect (225,500,250,50)
