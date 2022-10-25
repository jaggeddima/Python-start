PriNt = 10
number = 300
backgroundSSS = 1
room = 0
door = "This doors but very bad. 50 room and you win"
thanks = "Thanks for play"
roomm = "this room"

def setup():
    global backgroundSSS
    global door
    print (door)
    size (600,600)
    if (backgroundSSS == 1):
        background (100)
    fill (108,39,39)
    rect (0,325,1000,1000)
    frameRate (10)
        
    fill (22,24,111)
    rect (number,250,75,100)
    fill (216,176,144)
    rect (number + 10,200,50,50)
    fill (157,216,144)
    rect (number + 10, 350,25,50)
    rect (number + 40, 350,25,50)
def draw ():
    global PriNt
    global number
    global backgroundSSS
    global room
    
    
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
                
            fill (108,39,39)
            rect (0,325,1000,1000)

                
            if (room == 10):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 20):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 30):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 40):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            translate (-5, 0,)
            fill (22,24,111)
            rect (number,250,75,100)
            fill (216,176,144)
            rect (number + 10,200,50,50)
            fill (157,216,144)
            rect (number + 10, 350,25,50)
            rect (number + 40, 350,25,50)
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
                
            fill (108,39,39)
            rect (0,325,1000,1000)
                
            if (room == 10):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 20):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 30):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 40):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
                
            fill (108,39,39)
            rect (0,325,1000,1000)
            translate (5, 0)
            fill (22,24,111)
            rect (number,250,75,100)
            fill (216,176,144)
            rect (number + 10,200,50,50)
            fill (157,216,144)
            rect (number + 10, 350,25,50)
            rect (number + 40, 350,25,50)
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
            
        room = room - 1
        print (roomm, room)
        
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
            
        room = room + 1
        print (roomm, room)
        
    if (room == 50):
        print (thanks)
        end
        
    if (room == -1):
        end

        
        
