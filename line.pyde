def setup ():
    size (600,600)
    background (100)

def draw ():
    if (mouseButton == LEFT):
        line (mouseX,mouseY,200,1)
    if (mouseButton == RIGHT):
        clear()
        background (100)
