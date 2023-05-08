from fitness import *
import random

best = []
states = [None for i in range(1500)]

# generate random states
def generateStates(listMatkul:list) -> list:
    states = [[random.randint(0, 1) for i in range(len(listMatkul))] for j in range(5000)]

# find best fitness among all states
def findBest(listMatkul:list, minSks:int, maksSks:int, hariMasuk:list, maksJam:list, dosenFav:list, matkulFav:list) -> None:
    while(true):
        newStates = []

        for i in range(len(states)):
            p1 = randomSelect(newStates)
            p2 = randomSelect(newStates)

            child = crossover(p1, p2)
            if (random.random() <= 0.005):
                mutate(child)

            newStates.append(child)

        states = newStates
        best.sort()

        if (len(best) <= 3):
            return best

def crossover(p1:list, p2:list) -> list:
    pass

def mutate():
    pass

def randomSelect(states:list, best:list):
    newBest = []

    for i in range(len(states)):
        fitness = cekFitness(states[i], listMatkul, minSks, maksSks, hariMasuk, maksJam, dosenFav, matkulFav)

        if len(newBest) < len(best) / 2:
            newBest.append(states[i])
        elif fitness > min(best):
            newBest.remove(states[i])
            newBest.append(states[i])
    
    best = newBest