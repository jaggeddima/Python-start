PriNt = 10
number = 300
backgroundSSS = 1


def setup():
    global backgroundSSS
    size (600,600)
    if (backgroundSSS == 1):
        background (100)
        
    rect (number,300,100,50)
    
def draw ():
    global PriNt
    global number
    global backgroundSSS
    
    
    if keyPressed == True:
        if (PriNt == 10):
            clear()
            if (backgroundSSS == 1):
                background (100)
            if (backgroundSSS == 2):
                background (149,47,47)
            if (backgroundSSS == 3):
                background (81,137,51)
            if (backgroundSSS == 4):
                background (53,115,139)
            if (backgroundSSS == 5):
                background (139,53,105)
            translate (-20, 0,)
            rect (number,300,100,50)
            number = number - 20
            
    if keyPressed == True:
        if (PriNt == 15):
            clear()
            if (backgroundSSS == 1):
                background (100)
            if (backgroundSSS == 2):
                background (149,47,47)
            if (backgroundSSS == 3):
                background (81,137,51)
            if (backgroundSSS == 4):
                background (53,115,139)
            if (backgroundSSS == 5):
                background (139,53,105)
            translate (20, 0)
            rect (number,300,100,50)
            number = number + 20
            
    if (mouseButton == LEFT):
        PriNt = 10
    
    if (mouseButton == RIGHT):
        PriNt = 15
    
    if (number <= -100):
        number = 599  
        if (backgroundSSS == 2):
            backgroundSSS = 1
        if (backgroundSSS == 3):
            backgroundSSS = 2
        if (backgroundSSS == 4):
            backgroundSSS = 3
        if (backgroundSSS == 5):
            backgroundSSS = 4
        if (backgroundSSS == 1):
            backgroundSSS = 5
        
    if (number >= 600):
        number = -99  
        if (backgroundSSS == 5):
            backgroundSSS = 1
        if (backgroundSSS == 4):
            backgroundSSS = 5
        if (backgroundSSS == 3):
            backgroundSSS = 4
        if (backgroundSSS == 2):
            backgroundSSS = 3
        if (backgroundSSS == 1):
            backgroundSSS = 2
        

            
        
