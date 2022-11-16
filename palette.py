from color import *
import random
from matplotlib.colors import ListedColormap 
import seaborn as sns
from matplotlib import pyplot as plt

class palette():
    def __init__(self):
        self.pal = []
        for i in range(5):
            self.pal.append(color())
#        c = color()
 #       self.pal.append(c)
  #      c2 = color()
   #     self.pal.append(c2)
#        for i in range(1):
 #           c = color()
  #          self.pal.append(c)
    
    def mutate(self, mutationRate):
        newPalette = []
        randNum = 0
        for col in self.pal:
            randNum = random.random()
            if randNum < mutationRate:
                col.randomize()
            newPalette.append(col)
        return newPalette

    def contrast(self):
        contrastList = []
        for i in range(len(self.pal)-1):
            lum1 = color.luminance(self.pal[i])
            lum2 = color.luminance(self.pal[i+1])
            if lum1 > lum2:
                cr = (lum1 + 0.05)/(lum2 + 0.05)
            else:
                cr = (lum2 + 0.05)/(lum1 + 0.05)
            contrastList.append(cr)
        return contrastList

    def copy(self):
        p = palette()
        p.pal = []
        for i in self.pal:
            p.pal.append(i.copy())
        return p

    def fitness(self):
        fitness = 0
        cl = self.contrast()
        for c in range(len(self.pal)-1):
            if cl[c] < 2.8:
                fitness -= 450
            elif cl[c] > 5:
                fitness += 350
            if abs(self.pal[c].red - self.pal[c+1].red) == 10:
                fitness += 20
            elif abs(self.pal[c].red - self.pal[c+1].red) != 10:
                fitness -= 30
        return fitness
    
    def palDisplay(self):
        colorPal = []
        indColor = ()
        for col in self.pal: 
            indColor = (col.red/255, col.green/255, col.blue/255)
            colorPal.append(indColor)
        return colorPal