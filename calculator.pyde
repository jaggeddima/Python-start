lpp = 0
spp = 0
lp = lpp
sp = spp
slp = sp + lp
number = 1

def setup ():
    rectMode (CENTER)
    size (600,600)
    rect (150,300,100,50)
    rect (300,300,100,50)
    rect (450,300,100,50)
    frameRate (2)
    
def draw ():
    global lpp
    global spp
    global lp
    global sp
    global slp
    global number
    
    if (mouseX > 100) and (mouseX < 200) and (mouseY < 325) and (mouseY > 275):
        if (mouseButton == LEFT):
            lpp = lpp + 1
            fill (random (0,255),random (0,255),random (0,255))
            rect (150,300,100,50)
            
    if (mouseX > 250) and (mouseX < 350) and (mouseY < 325) and (mouseY > 275):
        if (mouseButton == LEFT):
            spp = spp + 1
            fill (random (0,255),random (0,255),random (0,255))
            rect (300,300,100,50)
    
    if (mouseX > 400) and (mouseX < 500) and (mouseY < 325) and (mouseY > 275):
        if (mouseButton == LEFT):
            slp = lpp + spp
            fill (random (0,255),random (0,255),random (0,255))
            rect (450,300,100,50)
            print(number, slp)
            
    if (mouseButton == RIGHT):
        lpp = 0
        spp = 0
        lp = lpp
        sp = spp
        slp = sp + lp
        number = number + 1
        fill (255)
        rect (150,300,100,50)
        rect (300,300,100,50)
        rect (450,300,100,50)

        
    
        
    
        
    
    
    
