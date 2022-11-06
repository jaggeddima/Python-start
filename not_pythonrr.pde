int sizes = 50;

void setup () {
  size (600,600);
  background (200);
  
  circle (300,300,sizes);
  
  rect (450, 500,
        100, 50);
  rect (300, 500,
        100, 50);
        
  fill (0);
  text ("size+", 475,525);
  text ("size-", 325,525);
  
}

void draw () {
  if (mouseButton == LEFT) {
        if (mouseX > 450 && mouseX < 550 && mouseY > 500 && mouseY < 550) {
            background (200);
            fill (255);
            sizes = sizes + 10;
  
            circle (300,300,sizes);
  
            rect (450, 500,
                  100, 50);
            rect (300, 500,
                  100, 50);
        
            fill (0);
            text ("size+", 475,525);
            text ("size-", 325,525);
        
    }
  }
  if (mouseButton == LEFT) {
        if (mouseX > 300 && mouseX < 400 && mouseY > 500 && mouseY < 550) {
            background (200);
            fill (255);
            sizes = sizes - 10;
  
            circle (300,300,sizes);
  
            rect (450, 500,
                  100, 50);
            rect (300, 500,
                  100, 50);
        
            fill (0);
            text ("size+", 475,525);
            text ("size-", 325,525);
    }
  }      
}
