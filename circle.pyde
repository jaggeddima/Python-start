
def setup():
    size (600,600)
    background (150)
    frameRate (10)

def draw():
    clear()
    stroke (random(0,255),random(0,255),random(0,255))
    strokeWeight (random(50,100))
    point (300,300)
