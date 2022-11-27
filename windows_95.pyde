cmd = "no"
bsod = "no"
bsodyesorno = "no"
paint = "no"

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
    global cmd,bsod,bsodyesorno
    
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
    
    fill (216,232,7)
    rect (10,240,50,50)
    
  
    
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
    if (bsodyesorno == "yes"):
        fill (255)
        rect (150,115,200,100)
        fill (0)
        text ("Really? You wanna bsod?         error 405",155, 130)
        
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
    global bsodyesorno
    if (key == 'b'):
        bsodyesorno = "yes"
        
