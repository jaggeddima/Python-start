def setup():
    size (600,600)
    background (0)
    
def draw():
    if (mouseButton == LEFT):
        fill(random(0,255),random(0,255),random(0,255))
        ellipse (mouseX,mouseY,10,10)
    if (mouseButton == RIGHT):
        clear()
