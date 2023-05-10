from fitness import *
import random
# import numpy as np

# generate random states
def generateStates(listMatkul:list, maksSks:int) -> list:
    states = []
    titikAwal = int(maksSks / 3)
    for i in range(50):
        state = np.array([1 for i in range(titikAwal)])
        state = np.append(state, [0 for i in range(listMatkul.__len__() - titikAwal)])
        np.random.shuffle(state)
        states.append(state)
    # print(states)
    return states
    # return [[random.randint(0, 1) for i in range(len(listMatkul))] for j in range(50)]

# find best fitness among all states
def findBest(listMatkul:list, minSks:int, maksSks:int, hariMasuk:list, maksJam:list, dosenFav:list, matkulFav:list, best:list) -> None:
    count = 0
    global states

    while(count <= 200):
        fitness = []
        # itung fitness dari tiap states
        for i in range(states.__len__()):
            fitness.append(cekFitness(states[i], listMatkul, minSks, maksSks, hariMasuk, maksJam, dosenFav, matkulFav))

            if len(best) == 0:
                best.append([states[i], fitness[i]])

            elif len(best) < 3:
                kembar = False
                for j in best:
                    kembar = cekStateKembar(j, states[i],fitness[i])
                    if kembar:
                        break
                if not kembar:
                    best.append([states[i], fitness[i]])
                    best = sorted(best, key=lambda x : x[1])

            elif fitness[i] > best[0][1]:
                kembar = False
                for j in best:
                    kembar = cekStateKembar(j, states[i], fitness[i])
                    if kembar:
                        break
                if not kembar:
                    best = sorted(best, key=lambda x : x[1])
                    best.pop(0)
                    best.append([states[i], fitness[i]])
                    best = sorted(best, key = lambda x : x[1])

        newStates = []
        print(best)

        for i in range(len(states)):
            p1 = best.__len__()-1
            p2 = randomSelect(fitness)

            child = crossover(best[p1][0], states[p2])
            scoreChild = cekFitness(child, listMatkul, minSks, maksSks, hariMasuk, maksJam, dosenFav, matkulFav)
            percentage = 0.002
            # print(child)
            if scoreChild <= 0:
                percentage = 0.02 * abs(scoreChild)/1000
            if (random.random() <= percentage):
                # print('Before mutation:', child)
                mutate(child, listMatkul, minSks, maksSks, hariMasuk, maksJam, dosenFav, matkulFav)
                # print('After mutation:', child)
            newStates.append(child)

            if scoreChild > best[0][1]:
                kembar = False
                for j in best:
                    kembar = cekStateKembar(j, child, scoreChild)
                    if kembar:
                        break
                if not kembar:
                    best = sorted(best, key=lambda x : x[1])
                    best.pop(0)
                    best.append([child, scoreChild])
                    best = sorted(best, key = lambda x : x[1])

        states.clear()
        states = newStates
        count += 1

    return best

def cekStateKembar(state1, state2, fitness) -> bool:
    if state1[1] == fitness:
        return True
    
    for i in range(len(state1[0])):
        if state1[0][i] != state2[i]:
            return False
    
    return True

def crossover(p1:list, p2:list) -> list:
    result = []
    # titikPotong = random.randint(1, p1.__len__())
    # result = [0 for i in range(p1.__len__())]
    # for i in range(result.__len__()):
    #     if i < int(p1.__len__()/titikPotong):
    #         result[i] = p1[i]
    #     else:
    #         result[i] = p2[i]
    # return result
    randoman = random.random()
    if(randoman <= 0.167):
        result = algoCross1(p1,p2)
    elif(randoman <= 0.334):
        result = algoCross1(p2,p1)
    elif(randoman <= 0.501):
        result = algoCross2(p1,p2)
    elif(randoman <= 0.667):
        result = algoCross2(p2,p1)
    elif(randoman <= 0.834):
        result = algoCross3(p1,p2)
    else:
        result = algoCross3(p2,p1)
    return result
    
    
def algoCross1(p1:list,p2:list):
    # crossover 2 titik
    titikPotong = random.randint(1,p1.__len__()-1)
    result = [0 for i in range(p1.__len__())]
    for i in range(result.__len__()):
        if i < int(p1.__len__()/titikPotong):
            result[i] = p1[i]
        else:
            result[i] = p2[i]
    return result

def algoCross2(p1:list,p2:list):
    # print(p2)
    # crossover 3 titik
    titikPotong1 = random.randint(1,p1.__len__()-1)
    titikPotong2 = random.randint(1,p1.__len__()-1)
    while(titikPotong2 == titikPotong1):
        titikPotong2 = random.randint(1,p1.__len__()-1)
    result = [0 for i in range(p1.__len__())]
    for i in range(p1.__len__()):
        if i < int(p1.__len__()/min(titikPotong1,titikPotong2)):
            result[i] = p1[i]
        elif i < int(p1.__len__()/max(titikPotong1,titikPotong2)):
            result[i] = p2[i]
        else :
            result[i] = p1[i]
    return result

def algoCross3(p1:list,p2:list):
    # crossover 4 titik
    titikPotong1 = random.randint(1,p1.__len__()-1)
    titikPotong2 = random.randint(1,p1.__len__()-1)
    while(titikPotong2 == titikPotong1):
        titikPotong2 = random.randint(1,p1.__len__()-1)
    titikPotong3 = random.randint(1,p1.__len__()-1)
    while(titikPotong3 == titikPotong1 or titikPotong3 == titikPotong2):
        titikPotong3 = random.randint(1,p1.__len__()-1)
    result = [0 for i in range(p1.__len__())]
    for i in range(p1.__len__()):
        if i < int(p1.__len__()/min(titikPotong1,titikPotong2,titikPotong3)):
            result[i] = p1[i]
        elif i < int(p1.__len__()/np.median(np.array([titikPotong1,titikPotong2,titikPotong3]))):
            result[i] = p2[i]
        elif i < int(p1.__len__()/max(titikPotong1,titikPotong2,titikPotong3)):
            result[i] = p1[i]
        else :
            result[i] = p2[i]
    return result

def mutate(gene:list, listMatkul:list, minSks:int, maksSks:int, hariMasuk:list, maksJam:list, dosenFav:list, matkulFav:list):
    # semi random mutate tidak merubah jumlah angka 1 yang digunakan karena ingin mempertahankan best
    score = cekFitness(gene, listMatkul, minSks, maksSks, hariMasuk, maksJam, dosenFav, matkulFav)
    mutator = []
    if score < -10000:
        for i in range(1+ ((int)(abs(score)/10000))):
            mutator.append(random.randint(0,gene.__len__()-1))
    elif score < 0:
        for i in range(1+ ((int)(abs(score)/1000))):
            mutator.append(random.randint(0,gene.__len__()-1))
    else:
        mutator.append(random.randint(0,gene.__len__()-1))
    # print(mutator)
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

    if total == 0:
        return 0

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
    minimum = min(np.array(best, dtype=object)[0::,1])
    # print(best)
    # print(minimum)
    # for i in range(best.__len__()):
    #     if best[i][1] <= minimum:
    #         minimum = best[i][1]
    
    for i in best:
        if minimum < 0:
            total += i[1]-minimum
        else:
            total += i[1]

    if total == 0:
        return 0
    
    cek = random.random()
    now = 0
    for i in range(best.__len__()):
        if minimum < 0:
            now += (best[i][1]-minimum)/total
        else:
            now += best[i][1]/total
        if now >= cek :
            return i

# Senin = 0
# Selasa = 27
# Rabu = 54
# Kamis = 81
# Jumat = 108
# Sabtu = 135 
# [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
listMat = [
    Matkul("Cyber Ops", "Cops", "B", "P 502", "Andreas", 0, 6, 2, 3),
    Matkul("Cyber Ops", "Cops", "A", "P 502", "Leo", 27, 6, 2, 3),
    Matkul("Cyber Ops", "Cops", "C", "P 502", "Agus", 27, 6, 2, 3),
    Matkul("Sistem Operasi", "SO", "A", "P 502", "Rudi", 2, 4, 6, 3),
    Matkul("Sistem Operasi", "SO", "C", "P 502", "Agus", 76, 4, 6, 3),
    Matkul("Sistem Operasi", "SO", "B", "P 502", "Rudi", 141, 3, 6, 3),
    Matkul("Grafika Komputer", "Grafkom", "A", "P 502", "Liliana", 2, 6, 10, 3),
    Matkul("Grafika Komputer", "Grafkom", "B", "P 502", "Liliana", 12, 6, 10, 3),
    Matkul("Analisa Desain Sistem Informasi", "ADSI", "C", "P 502", "Lily", 12, 6, 14, 3),
    Matkul("Analisa Desain Sistem Informasi", "ADSI", "D", "P 502", "Alex", 60, 6, 14, 3),
    Matkul("Analisa Desain Sistem Informasi", "ADSI", "B", "P 502", "Silvia", 66, 6, 14, 3),
    Matkul("Analisa Desain Sistem Informasi", "ADSI", "A", "P 502", "Yulia", 93, 6, 14, 3),
    Matkul("Komunikasi Interpersonal", "Komal", "B", "P 502", "Stephanus", 12, 6, 18, 3),
    Matkul("Komunikasi Interpersonal", "Komal", "A", "P 502", "Stephanus", 41, 6, 18, 3),
    Matkul("Komunikasi Interpersonal", "Komal", "C", "P 502", "Stephanus", 40, 6, 18, 3),
    Matkul("Komunikasi Interpersonal", "Komal", "D", "P 502", "Stephanus", 92, 6, 18, 3),
    Matkul("Kecerdasan Buatan", "KB", "C", "P 502", "Alvin", 35, 6, 22, 3),
    Matkul("Kecerdasan Buatan", "KB", "B", "P 502", "Greg", 66, 6, 22, 3),
    Matkul("Kecerdasan Buatan", "KB", "A", "P 502", "Hans", 35, 6, 22, 3),
    Matkul("Interaksi Manusia Komputer", "IMK", "C", "P 502", "Adi", 54, 6, 26, 3),
    Matkul("Interaksi Manusia Komputer", "IMK", "A", "P 502", "Andreas", 72, 6, 26, 3),
    Matkul("Interaksi Manusia Komputer", "IMK", "B", "P 502", "Krisna", 108, 6, 26, 3),
    Matkul("Metode Numerik", "Metnum", "A", "P 502", "Leo", 60, 4, 30, 3),
    Matkul("Metode Numerik", "Metnum", "B", "P 502", "Stephanus", 87, 4, 30, 3),
    Matkul("Metode Numerik", "Metnum", "C", "P 502", "Stephanus", 93, 4, 30, 3),
    Matkul("Statistika Terapan", "ST", "A", "P 502", "Stephanus", 81, 6, 34, 3),
    Matkul("Data Mining", "Datmin", "A", "P 502", "Stephanus", 87, 6, 38, 3),
    Matkul("Analisa Proses Bisnis", "APB", "A", "P 502", "Krisna", 93, 6, 42, 3),
]
# np.random.shuffle(np.array(listMat))
best = []
states = []
states = generateStates(listMat, 24)
best = findBest(listMat, 18, 24, [1,1,1,1,1,0], [12,12,12,12,12,0], ['Rudi','Krisna'], ['APB','IMK'], [])
print(best)

