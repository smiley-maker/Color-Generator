import random
import numpy as np
import copy

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
        rate = 30
        mod = random.randint(-rate, rate)
        while not 0 <= self.red + mod <= 255:
            mod = random.randint(-rate, rate)
        self.red += mod
        mod = random.randint(-rate, rate)
        while not 0 <= self.green + mod <= 255:
            mod = random.randint(-rate, rate)
        self.green += mod
        mod = random.randint(-rate, rate)
        while not 0 <= self.blue + mod <= 255:
            mod = random.randint(-rate, rate)
        self.blue += mod


#        print(random.sample([random.randint(0, 10), -1*(random.randint(0, 10)%abs(1-self.red))], 1))
#        self.red += random.sample([random.randint(0, 10)%abs(256-self.red), -1*(random.randint(0, 10)%abs(self.red+1))], 1)[0]
 #       self.green += random.sample([random.randint(0, 10)%abs(256-self.green), -1*(random.randint(0, 10)%abs(1+self.green))], 1)[0]
  #      self.blue += random.sample([random.randint(0, 10)%abs(256-self.blue), -1*(random.randint(0, 10)%abs(1+self.blue))], 1)[0]
    
    def display(self):
        print("(%f, %f, %f)" % (self.red, self.green, self.blue))
    
    def luminance(self):
        R = self.red/255
        G = self.green/255
        B = self.blue/255
        lum = 0.2126*R + 0.7152*G + 0.0722*B
        return lum
    
    def copy(self):
        return copy.copy(self)