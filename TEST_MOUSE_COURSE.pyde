
def setup ():
    size (400,400)

def draw ():
    background (0) #black
    if (mouseX <= 200) and (mouseY <= 200):
        rect (0,0,200,200)
    
    elif (mouseX <= 400) and (mouseY <= 200):
        rect (200,0,200,200)
    
    elif (mouseX <= 200) and (mouseY > 200):
          rect (0,200,200,200)
    
    elif (mouseX > 200) and (mouseY > 200):
          rect (200,200,200,200)
    
    if (mouseButton == RIGHT):
        fill (random(0,255),random(0,255),random(0,255))
    
