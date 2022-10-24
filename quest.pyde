sylka = "This mormal youtube video (russia) https://www.youtube.com/watch?v=qfzjbzh5iZw"
Normal = "Okay this very many buttons. Click center button, and read story"
story = "One person cut down 10 trees in 6 minutes. His friend cut down 18 trees in 6 minutes. How many will they cut down 28 trees together?"
Quest = "Answer: (1 button) 38, (2 button) 28, (3 button) sylka"
otbet = "Well done! The theater has 500 seats. How many half were occupied by idiots (50% of them)    Answer: (1 button) 250, (2 button) 350."
okay = ":/ . You a normal? Vach this kid https://www.youtube.com/channel/UC_8PAD0Qmi6_gpe77S1Atgg"
Wow = "Wow toy real very good. What video funny? 1) https://www.youtube.com/watch?v=oC4q3lA3Dbc 2) https://www.youtube.com/watch?v=tQrNJTDSqB8"
thanks = "Okay thanls vach this :)"

nukna = 1

no = "no, you dumb :). Okay, copy this https://www.youtube.com/watch?v=EYSdmbrPc24"

def setup ():
    global normal
    size (600,600)
    rectMode (CENTER)
    print (Normal)
    rect (300,300,150,75)
    frameRate (3)
    
def draw ():
    global sylka
    global Normal
    global story
    global nukna
    global no
    global otbet
    
    
    if (mouseX > 225) and (mouseX < 375) and (mouseY > 262.5) and (mouseY < 337.5):
        if (mouseButton == LEFT):
            if (nukna == 1):
                print (story)
                print (Quest)
                clear ()
                background (200)
                rect (100,300,150,75)
                rect (300,500,150,75)
                rect (500,300,150,75)
                nukna = nukna + 1
            
    if (mouseX > 25) and (mouseX < 175) and (mouseY > 262.5) and (mouseY < 337.5):
            if (mouseButton == LEFT):
                if (nukna == 2):
                    frameRate (60)
                    print (no)
                        
                        
    if (mouseX > 425) and (mouseX < 575) and (mouseY > 262.5) and (mouseY < 337.5):
        if (mouseButton == LEFT):
            if (nukna == 2):
                frameRate (60)
                print (sylka)
                
    if (mouseX > 225) and (mouseX < 375) and (mouseY > 462.5) and (mouseY < 537.5):
            if (mouseButton == LEFT):
                if (nukna == 2):
                    print (otbet)
                    clear ()
                    background (200)
                    rect (100,300,150,75)
                    rect (500,300,150,75)
                    frameRate (3)
                    nukna = 3
                    
    if (mouseX > 25) and (mouseX < 175) and (mouseY > 262.5) and (mouseY < 337.5):
        if (mouseButton == LEFT):
            if (nukna == 3):
                frameRate (3)
                print (thanks)
                clear ()
                background (200)
                nunka = 4
                        
                        
    if (mouseX > 425) and (mouseX < 575) and (mouseY > 262.5) and (mouseY < 337.5):
        if (mouseButton == LEFT):
            if (nukna == 3):
                frameRate (3)
                print (okay)
                
                
    
                    
    

            
        
