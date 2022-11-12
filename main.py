import random
from population import *
from palette import *

def runGA(populationSize, crossoverRate, mutationRate):
    popl = population(populationSize)
    newPop = population(populationSize)
    for i in range(int(populationSize/2)):
        popl.sortByFitness()
        print(popl)
        pair1, pair2 = popl.selectPair()
        if random.random() < crossoverRate:
            popl.crossover(pair1, pair2)
        pair1.mutate(mutationRate)
        pair2.mutate(mutationRate)
        newPop.addPalette(pair1)
        newPop.addPalette(pair2)
        popl = newPop
        popl.displays()

runGA(6, 0.7, 0.02)