from palette import *
import random
import numpy as np
from matplotlib.colors import ListedColormap
import seaborn as sns
from matplotlib import pyplot as plt
import copy

class population:
    def __init__(self, popSize):
        self.popSize = popSize
        self.pop = []
        for i in range(self.popSize):
            p = palette()
            self.pop.append(p)
    
    def sortByFitness(self):
        tuples = [(pal.fitness(), pal) for pal in self.pop]
#        print(tuples)
        tuples.sort(key=lambda x: x[0])
        sortedFitnessValues = [f for (f,g) in tuples]
        sortedPalettes = [g for (f, g) in tuples]
        return sortedPalettes, sortedFitnessValues
    
    def selectPair(self):
        weight = list(range(len(self.pop)))
        total = sum(weight)
        cost = [w/total for w in weight]
        choiceOne = np.random.choice(self.pop, p = cost)
        choiceTwo = np.random.choice(self.pop, p = cost)
#        newPop = self.sortByFitness()
        return (choiceOne, choiceTwo)
    
    def crossover(self, pal1, pal2):
        crossoverPoint = random.randint(1,len(pal1.pal)-1)
        newpal1 = pal1.pal[0:crossoverPoint] + pal2.pal[crossoverPoint:]
        newpal2 = pal2.pal[0:crossoverPoint] + pal1.pal[crossoverPoint:]
        return newpal1.copy(), newpal2.copy()

    def addPalette(self, pal):
        self.pop.append(pal)
    
    def copy(self):
        newPop = population()
        for i in self.pop:
            newPop.pop.append(i.copy())
    
    def displays(self):
        for i in range(int(len(self.pop))):
            currentPal = self.pop[i].palDisplay()
            sns.set_palette(currentPal)
            current_palette = sns.color_palette()
            sns.palplot(current_palette)
            plt.savefig('palettes/palette'+str(i)+'.png', dpi=300, bbox_inches='tight')
            plt.close()
        plt.close()