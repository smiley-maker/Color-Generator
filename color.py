import random

class color:
    def __init__(self, red=None, green=None, blue=None):
        if red != None:
            self.red = red
        else:
            self.red = random.randint(0, 255)
        if green != None:
            self.green = green
        else:
            self.green = random.randint(0, 255)
        if blue != None:
            self.blue = blue
        else:
            self.blue = random.randint(0, 255)
    
    def randomize(self):
        self.red = random.randint(0,255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
    
    def display(self):
        print("(%f, %f, %f)" % (self.red, self.green, self.blue))
    
    def luminance(self):
        R = self.red/255
        G = self.green/255
        B = self.blue/255
        lum = 0.2126*R + 0.7152*G + 0.0722*B
        return lum