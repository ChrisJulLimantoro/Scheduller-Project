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

            child = crossover(best[0][p1], states[p2])
            scoreChild = cekFitness(child)
            percentage = 0.02
            if scoreChild <= 0:
                percentage = 0.02 * abs(scoreChild)/100
            if (random.random() <= percentage):
                    mutate(child)
            newStates.append(child)

        states = newStates
        best.sort()
        count += 1
        if (count > 1000):
            return best

def crossover(p1:list, p2:list) -> list:
    result = []
    if(random.random() <= 0.167):
        result = algoCross1(p1,p2)
    elif(random.randint(0,5) <= 0.334):
        result = algoCross1(p2,p1)
    elif(random.randint(0,5) <= 0.501):
        result = algoCross2(p1,p2)
    elif(random.randint(0,5) <= 0.667):
        result = algoCross2(p2,p1)
    elif(random.randint(0,5) <= 0.834):
        result = algoCross3(p1,p2)
    else:
        result = algoCross3(p2,p1)
    return result
    
    
def algoCross1(p1:list,p2:list):
    # crossover 2 titik
    result = [0 for i in range(p1.__len__())]
    for i in range(result.__len__()):
        if i < int(p1.__len__()/2):
            result[i] = p1[i]
        else:
            result[i] = p2[i]
    return result

def algoCross2(p1:list,p2:list):
    # crossover 3 titik
    result = [0 for i in range(p1.__len__())]
    for i in range(p1.__len__()):
        if i < int(p1.__len__()/3):
            result[i] = p1[i]
        elif i < int(p1.__len__()*2/3):
            result[i] = p2[i]
        else :
            result[i] = p1[i]
    return result

def algoCross3(p1:list,p2:list):
    # crossover 4 titik
    result = [0 for i in range(p1.__len__())]
    for i in range(p1.__len__()):
        if i < int(p1.__len__()/4):
            result[i] = p1[i]
        elif i < int(p1.__len__()/2):
            result[i] = p2[i]
        elif i < int(p1.__len__()*3/4):
            result[i] = p1[i]
        else :
            result[i] = p2[i]
    return result

def mutate(gene:list):
    # semi random mutate tidak merubah jumlah angka 1 yang digunakan karena ingin mempertahankan best
    score = cekFitness(gene)
    mutator = 0
    if score < 0:
        for i in range(1+ (abs(score)/100)):
            mutator.append(random.randint(0,gene.__len__()-1))
    else:
        mutator.append(random.randint(0,gene.__len__()-1))
    
    for i in range(gene.__len__()):
        # mutasi berdasarkan fitness jika fitness jelek lebih banyak bit yg di flip
        if i in mutator:
            if gene[i] == 0:
                gene[i] = 1
            else:
                gene[i] = 0
    

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
