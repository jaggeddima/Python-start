x=0

def setup():
   size(1000,1000)
   frameRate(50)

def draw():
   clear()
   global x
   translate(500,500)
   rotate(radians(x))
   ellipse(0,0,100,100)
   rect(0,0,-500,50)
   rectMode(CENTER)
   rect(0,0,50,500)
   x=x+10
