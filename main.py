import random
from population import *
from palette import *
import copy

def runGA(populationSize, crossoverRate, mutationRate):
    popl = population(populationSize)
    for j in range(400):
        newPop = []
        for i in range(int(populationSize/2)):
            popl.sortByFitness()
#            print(popl)
            pair1, pair2 = popl.selectPair()
            while pair1 == pair2 :
                pair1, pair2 = popl.selectPair()
            pair1 , pair2 = pair1.copy() , pair2.copy()
            if random.random() < crossoverRate:
                pair1.pal, pair2.pal = popl.crossover(pair1, pair2)
            pair1.pal = pair1.mutate(mutationRate)
            pair2.pal = pair2.mutate(mutationRate)
            newPop.append(pair1.copy())
            newPop.append(pair2.copy())
        popl.pop = newPop
        if j%100 == 0:
            print(j)
        
    popl.displays()

runGA(60, 0.8, 0.2)