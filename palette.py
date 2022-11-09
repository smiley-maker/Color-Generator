from color import *
import random
from matplotlib.colors import ListedColormap
import seaborn as sns
from matplotlib import pyplot as plt
        

class palette():
    def __init__(self):
        self.pal = []
        c = color()
        self.pal.append(c)
        c2 = color()
        self.pal.append(c2)
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

    def contrast(self):
        lum1 = color.luminance(self.pal[0])
        lum2 = color.luminance(self.pal[1])
        if lum1 > lum2: 
            cr = (lum1 + 0.05)/(lum2 + 0.05)
        else:
            cr = (lum2 + 0.05)/(lum1 + 0.05)
        return cr

    def fitness(self):
        fitness = 0
        ct = self.contrast()
        if ct < 2.8:
            fitness -= 10
        elif ct > 5:
            fitness += 1
        print(fitness)
        return fitness
    
    def palDisplay(self):
        colorPal = []
        indColor = ()
        for col in self.pal:
            indColor = (col.red/255, col.green/255, col.blue/255)
            colorPal.append(indColor)
        #print(colorPal)
        return colorPal
        # sns.set_palette(colorPal)
        # current_palette = sns.color_palette()
        # sns.palplot(current_palette)
        # plt.show()
        #for j in self.pal:
         #   color.display(j)
          #  print("\t")

