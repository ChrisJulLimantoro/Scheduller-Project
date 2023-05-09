from fitness import *
import random

best = [[],[],[]]
states = []

# generate random states
def generateStates(listMatkul:list) -> list:
    states = [[random.randint(0, 1) for i in range(len(listMatkul))] for j in range(5000)]

# find best fitness among all states
def findBest(listMatkul:list, minSks:int, maksSks:int, hariMasuk:list, maksJam:list, dosenFav:list, matkulFav:list) -> None:
    count = 0
    while(True):
        fitness = []
        # itung fitness dari tiap states
        for i in range(states.__len__()):
            fitness.append(cekFitness(states[i]))
        
        newStates = []

        for i in range(len(states)):
            p1 = randomSelect(best)
            p2 = randomSelect(fitness)

            child = crossover(best[p1], states[p2])
            if (random.random() <= 0.005):
                mutate(child)

            newStates.append(child)

        states = newStates
        best.sort()
        count += 1
        if (count > 1000):
            return best

def crossover(p1:list, p2:list) -> list:
    pass

def mutate():
    pass

def randomSelect(fitness:list) -> int:
    total = 0
    minimum = min(fitness)
    for i in fitness:
        if minimum < 0:
            total += (i - minimum)
        else:
            total += i
    cek = random.random()
    now = 0
    for i in range(fitness.__len__()):
        if minimum < 0:
            now += (fitness[i]-minimum)/total
        else:
            now += fitness[i]/total
        if now >= cek :
            return i
        
def randomSelectBest(best:list) -> int:
    total = 0
    minimum = 10000000
    for i in range(best.__len__()):
        if best[i][1] <= minimum:
            minimum = best[i][1]
    
    for i in best:
        if minimum < 0:
            total += i[1]-minimum
        else:
            total += i[1]
    
    cek = random.random()
    now = 0
    for i in range(best.__len__()):
        if minimum < 0:
            now += (best[i][1]-minimum)/total
        else:
            now += best[i][1]/total
        if now >= cek :
            return i

list = [[[1,0,0,0,1,1,1,0],1500],[[1,0,1,0,1,1,1,0],-50],[[1,0,0,0,0,1,1,1],100]]
print(randomSelectBest(list))