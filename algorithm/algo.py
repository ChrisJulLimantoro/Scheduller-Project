from fitness import *
import random

best = []
states = []

# generate random states
def generateStates(listMatkul:list) -> list:
    states = [[random.randint(0, 1) for i in range(len(listMatkul))] for j in range(1000)]

# find best fitness among all states
def findBest(listMatkul:list, minSks:int, maksSks:int, hariMasuk:list, maksJam:list, dosenFav:list, matkulFav:list) -> None:
    for i in range(len(states)):
        # crossover()
        # mutate()
        fitness = cekFitness(states[i], listMatkul, minSks, maksSks, hariMasuk, maksJam, dosenFav, matkulFav)
        if fitness > min(best):
            best.remove(min(best))
            best.append(fitness)
    
    best.sort()
    return best

def crossover():
    pass

def mutate():
    pass