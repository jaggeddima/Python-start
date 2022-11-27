cmd = "no"
bsod = "no"
bsodyesorno = "no"
pusk = "no"
google = "no"

def setup () :
    size (720,480)
    
    noStroke ()
    background (11,219,189)
    fill (155)
    rect (0,0,720,35)
    fill (0)
    text ("World, Operation sistem windows 95", 10,20)
    fill (200)
    rect (0,430,720,480-430)
    frameRate (10)
    
def draw ():
    global cmd,bsod,bsodyesorno,pusk,img,google
    img = loadImage ("pusk.jpg")
    print (mouseX,mouseY)
    clear ()
    background (11,219,189)
    fill (155)
    rect (0,0,720,35)
    fill (0)
    text ("World, Operation sistem windows 95", 10,20)
    fill (200)
    rect (0,430,720,480-430)
    
    fill (0)
    rect (10,300,50,50)
    
    image (img,0,480-35,35,35)
    
    if (pusk == "yes"):
        fill (200)
        rect (0,200,150,480-200-35)
    
    if (mouseX >= 0) and (mouseX <= 35) and (mouseY >= 480-35) and (mouseY <= 480):
         if (mouseButton == LEFT):
            pusk = "yes"
         if (mouseButton == RIGHT):
            pusk = "no"
  
    
    if (mouseX >= 10) and (mouseX <= 60) and (mouseY >= 300) and (mouseY <= 350):
        if (mouseButton == LEFT):
            cmd = "yes"
    if (cmd == "yes"):
        fill (0)
        rect (200,100,300,150)
        fill (255)
        rect (200,75,300,25)
        fill (255,0,0)
        rect (475,75,25,25)
        if (bsodyesorno == "yes"):
            fill (255)
            text ("Bsod",360,125)
        if (mouseX >= 475) and (mouseX <= 500) and (mouseY >= 75) and (mouseY <= 100):
            if (mouseButton == LEFT):
                cmd = "no"
                bsodyesorno = "no"
        fill (255)
        text ("BIOS Commands. Pleas write :",205,125)
    if (google == "open"):
        fill (200)
        rect (165,212,300,200)
        fill (255)
        rect (165,212,300,25)
        fill (150)
        ellipse (315,245,250,10)
        
        fill (255,0,0)
        rect (165+300-25,212,25,25)
        if (mouseX >= 165+300-25) and (mouseX <= 165+300) and (mouseY >= 212) and (mouseY <= 237):
            if (mouseButton == LEFT):
                google = "no"
    if (bsodyesorno == "yes"):
        fill (255)
        rect (150,115,200,100)
        fill (0)
        text ("Really? You wanna bsod? error 405",155, 130)
        
        fill (200)
        rect (200,200,25,10)
        fill (0)
        text ("no", 205,208)
        
        translate (50,0)
        fill (200)
        rect (200,200,25,10)
        fill (0)
        text ("yes", 205,208)
        translate (-50,0)
        
        if (mouseButton == LEFT):
            if (mouseX >= 200) and (mouseX <= 220) and (mouseY >= 200) and (mouseY <= 210):
                cmd = "no"
                bsodyesorno = "no"
            elif (mouseX >= 250) and (mouseX <= 270) and (mouseY >= 200) and (mouseY <= 210):
                bsod = "yes"
        if (bsod == "yes"):
            fill (73,172,232)
            rect (0,35,1000,1000)
            fill (255)
            rect (20,60,500,30)
            rect (20,100,450,30)
            rect (20,140,289,30)
            rect (20,180,597,30)
            translate (0,160)
            rect (20,60,500,30)
            rect (20,100,450,30)
            rect (20,140,289,30)
            rect (20,180,597,30)
def keyPressed ():
    global bsodyesorno,google
    if (key == "b"):
        bsodyesorno = "yes"
    if (key == "g"):
        google = "open"
    
        
