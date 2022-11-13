PriNt = 10
number = 300
backgroundSSS = 1
room = 97
door = "This doors but very bad. 100 room and you win"
thanks = "Thanks for play"
roomm = "this room"
skaf = 2
obet = 50
kamot = 1
kavry = 1
shadow = 0

def setup():
    global backgroundSSS,door
    print (door)
    size (600,600)
    if (backgroundSSS == 1):
        background (100)
    fill (108,39,39)
    rect (0,325,1000,1000)
    frameRate (25)
        
    fill (22,24,111)
    rect (number,250,75,100)
    fill (216,176,144)
    rect (number + 10,200,50,50)
    fill (157,216,144)
    rect (number + 10, 350,25,50)
    rect (number + 40, 350,25,50)
def draw ():
    global PriNt,number,backgroundSSS,room,skaf,kamot,kavry,shadow
    
    if keyPressed == True:
        if (PriNt == 10):
            clear()
            if (room < 99):
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
            if (room > 99):
                background (100,100,100)
        
            if (room < 99):
                fill (108,39,39)
                rect (0,325,1000,1000)
            if (room > 99):
                fill (39,39,39)
                rect (0,325,1000,1000)
            
            if (room < 99):
                if (kavry == 4):
                    fill (152,63,34)
                    rect (100,350,400,200)

                
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
            if (room == 60):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 70):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 80):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 90):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
                
            if (room == 73):
                background (91,194,214)
                fill (45,124,15)
                rect (0,325,1000,1000)
                fill (129,79,46)
                rect (0,100,1000,250)
                
            if (room == 50):
                fill (118,68,35)
                rect (100,100,400,230)
            
            if (skaf == 4):
                fill (203,142,62)
                rect (150,200,100,200)
                fill (75,54,22)
                rect (195,205,10,190)
            
            if (kamot == 5):
                fill (178,117,43)
                rect (350,300,15,75)

                translate (100,0)
                rect (350,300,15,75)

                translate (-100,0)

                rect (350,300,115,30)

                fill (245,234,17)
                ellipse (410,315,15,15)

                
            translate (-5, 0,)
            fill (22,24,111)
            rect (number,250,75,100)
            fill (216,176,144)
            rect (number + 10,200,50,50)
            fill (157,216,144)
            rect (number + 10, 350,25,50)
            rect (number + 40, 350,25,50)
            number = number - 20
            
            if (room == 50):
                fill (118,68,35)
                rect (0,350,1000,1000)
                
            
            
            if (number > 150) and (number < 250):
                if (mouseButton == LEFT):
                    if (skaf == 4):
                        if (room < 99):
                            if (backgroundSSS == 1):
                                background (100)
                            if (backgroundSSS == 2):
                                background (149 - obet,47 - obet,47 - obet)
                            if (backgroundSSS == 3):
                                background (81 - obet,137 - obet,51 - obet)
                            if (backgroundSSS == 4):
                                background (53 - obet,115 - obet,139 - obet)
                            if (backgroundSSS == 5):
                                background (139 - obet,53 - obet,105 - obet)
                        if (room > 99):
                            background (100,100,100)
        
                        if (room < 99):
                            fill (108,39,39)
                            rect (0,325,1000,1000)
                        if (room > 99):
                            fill (39,39,39)
                            rect (0,325,1000,1000)
            
                        if (room < 99):
                            if (kavry == 4):
                                fill (152,63,34)
                                rect (100,350,400,200)
                        if (room == 20):
                            fill (37,211,232)
                            rect (100,100,500,200)
                        if (room == 40):
                            fill (37,211,232)
                            rect (100,100,500,200)
                        if (room == 60):
                            fill (37,211,232)
                            rect (100,100,500,200)
                        if (room == 80):
                            fill (37,211,232)
                            rect (100,100,500,200)
                            
                        if (room == 50):
                            fill (129,92,36)
                            rect (100,100,400,300)
                            
                        if (kamot == 5):
                            translate (-200,0)
                            fill (178,117,43)
                            rect (350,300,15,75)

                            translate (100,0)
                            rect (350,300,15,75)

                            translate (-100,0)

                            rect (350,300,115,30)

                            fill (245,234,17)
                            ellipse (410,315,15,15)
                        if (kamot == 5):
                            translate (200,0)
                        fill (67,47,18)
                        rect (0,0,290,600)
                        rect (310,0,300,600)
                        
            if (number > 350) and (number < 475):
                if (mousePressed == LEFT):
                    if (kamot == 5):
                        fill (108,39,39)
                        rect (0,0,1000,1000)

                        fill (245,234,17)
                        ellipse (300,425,100,100)

                        fill (178,117,43)
                        rect (100,0,400,400)

                        fill (178 - obet, 117 - obet, 17)
                        rect (150,0,300,350)
            
    if keyPressed == True:
        if (PriNt == 15):
            clear()
            if (room < 99):
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
                
            if (room > 99):
                background (100,100,100)
        
            if (room < 99):
                fill (108,39,39)
                rect (0,325,1000,1000)
            if (room > 99):
                fill (39,39,39)
                rect (0,325,1000,1000)
            
            if (room < 99):
                if (kavry == 4):
                    fill (152,63,34)
                    rect (100,350,400,200)

            if (kavry == 4):
                fill (152,63,34)
                rect (100,350,400,200)
            
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
            if (room == 60):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 70):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 80):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            if (room == 90):
                fill (37,211,232)
                rect (100,100,100,200)
                rect (400,100,100,200)
            
                
            if (room == 50):
                fill (118,68,35)
                rect (100,100,400,230)
                
            if (room == 73):
                background (91,194,214)
                fill (45,124,15)
                rect (0,325,1000,1000)
                fill (129,79,46)
                rect (0,100,1000,250)
                
            if (skaf == 4):
                fill (203,142,62)
                rect (150,200,100,200)
                fill (75,54,22)
                rect (195,205,10,190)
                
            if (kamot == 5):
                fill (178,117,43)
                rect (350,300,15,75)

                translate (100,0)
                rect (350,300,15,75)

                translate (-100,0)

                rect (350,300,115,30)

                fill (245,234,17)
                ellipse (410,315,15,15)

                

                
            translate (5, 0,)
            fill (22,24,111)
            rect (number,250,75,100)
            fill (216,176,144)
            rect (number + 10,200,50,50)
            fill (157,216,144)
            rect (number + 10, 350,25,50)
            rect (number + 40, 350,25,50)
            number = number + 20
            
            if (room == 50):
                fill (118,68,35)
                rect (0,350,1000,1000)
                
            if (number > 150) and (number < 250):
                if (mouseButton == LEFT):
                    if (skaf == 4):
                        if (backgroundSSS == 1):
                            background (100)
                        if (backgroundSSS == 2):
                            background (149 - obet,47 - obet,47 - obet)
                        if (backgroundSSS == 3):
                            background (81 - obet,137 - obet,51 - obet)
                        if (backgroundSSS == 4):
                            background (53 - obet,115 - obet,139 - obet)
                        if (backgroundSSS == 5):
                            background (139 - obet,53 - obet,105 - obet)
                            
                        if (room < 99):
                            background (100,100,100)
        
                        if (room < 99):
                            fill (108,39,39)
                            rect (0,325,1000,1000)
                        if (room < 99):
                            fill (39,39,39)
                            rect (0,325,1000,1000)
            
                        if (room > 99):
                            if (kavry == 4):
                                fill (152,63,34)
                                rect (100,350,400,200)
                            
                        if (room == 20):
                            fill (37,211,232)
                            rect (100,100,500,200)
                        if (room == 40):
                            fill (37,211,232)
                            rect (100,100,500,200)
                        if (room == 60):
                            fill (37,211,232)
                            rect (100,100,500,200)
                        if (room == 80):
                            fill (37,211,232)
                            rect (100,100,500,200)
                            
                        if (room == 50):
                            fill (129,92,36)
                            rect (100,100,400,300)
                            
                        if (kamot == 5):
                            translate (-100,0)
                            fill (178,117,43)
                            rect (350,300,15,75)

                            translate (100,0)
                            rect (350,300,15,75)

                            translate (-100,0)

                            rect (350,300,115,30)

                            fill (245,234,17)
                            ellipse (410,315,15,15)
                
                            
                        fill (67,47,18)
                        rect (0,0,290,600)
                        rect (310,0,300,600)


            if (number > 350) and (number < 475):
                if (mousePressed == LEFT):
                    if (kamot == 5):
                        fill (108,39,39)
                        rect (0,0,1000,1000)

                        fill (245,234,17)
                        ellipse (300,425,100,100)

                        fill (178,117,43)
                        rect (100,0,400,400)
    
                        fill (178 - obet, 117 - obet, 17)
                        rect (150,0,300,350)
            
            
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
        if (skaf == 2):
            skaf = 1
        if (skaf == 3):
            skaf = 2
        if (skaf == 4):
            skaf = 3
        if (skaf == 1):
            skaf = 4
        
        if (kamot == 2):
            kamot = 1
        if (kamot == 3):
            kamot = 2
        if (kamot == 4):
            kamot = 3
        if (kamot == 5):
            kamot = 4
        if (kamot == 1):
            kamot = 5
            
        if (kavry == 2):
            kavry = 1
        if (kavry == 3):
            kavry = 2
        if (kavry == 4):
            kavry = 3
        if (kavry == 1):
            kavry = 4
        
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
            
        if (skaf == 4):
            skaf = 1
        if (skaf == 3):
            skaf = 4
        if (skaf == 2):
            skaf = 3
        if (skaf == 1): 
            skaf = 2
        
        if (kamot == 5):
            kamot = 1
        if (kamot == 4):
            kamot = 5
        if (kamot == 3):
            kamot = 4
        if (kamot == 2):
            kamot = 3
        if (kamot == 1):
            kamot = 2
            
        if (kavry == 4):
            kavry = 1
        if (kavry == 3):
            kavry = 4
        if (kavry == 2):
            kavry = 3
        if (kavry == 1): 
            kavry = 2
            
        room = room + 1
        print (roomm, room)
        
    if (room == 200):
        shadow = (random (1,2))
        if (shadow == 1):
            print (thanks)
            end
        if (shadow == 2):
            background (152,36,32)
            fill (201,32,26)
            text ("You......", 250,250)
            end
    
        
    if (room == -1):
        end
    
