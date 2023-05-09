from matkul import Matkul
import numpy as np 
import random

def cekFitness(state:list,listMat:list,minSks:int=15,maksSks:int=24,hariMasuk:list=[1,1,1,1,1,1],maksJam:list=[20,20,20,20,20,20],dosenFav:list=[],matkulFav:list=[]) -> int:
    countSks = 0
    countJam = [0,0,0,0,0,0]
    fitness = 0
    active=[]
    # algo
    for i in range(state.__len__()):
        if state[i] == 0:
            continue
        else :
            # array kelas
            # print(state)
            # print(len(listMat))
            # print(len(state))
            # print(listMat)
            active.append(listMat[i].singkatan)
            # print(len(active))
            
            # print('cek Collision : ',i,fitness)
            # cek jumlah sks
            countSks+=listMat[i].sks
            
            # cek jam
            jadwal=listMat[i].jadwalKelas
            countJam[int(jadwal/27)]+=listMat[i].lamaKelas
            
            # algo cek dosen fav
            if listMat[i].dosen in dosenFav:
                fitness += 30
                
            # algo cek matkul fav
            if listMat[i].nama in matkulFav:
                fitness += 80
    # print(countJam)
    # perhitungan fitness
    fitness += cekCollision(state, listMat)
    fitness += cekSks(countSks,minSks,maksSks) # cek SKS
    # print('cekSKs : ',fitness)
    fitness += cekJam(countJam,maksJam) # cek Jumlah Jam
    # print('cekJam : ',fitness)
    fitness += cekHari(countJam,hariMasuk) # cek hari masuk
    # print('cekHari : ',fitness)
    fitness += cekKembar(active) # cek kembar
    return fitness

def cekCollision(state:list, listMat:list) -> int:
    result = 0
    for i in range(len(state)):
        # cek Collision jadwal kelas
        for j in range(i+1,state.__len__()):
            if state[j] == 1:
                if listMat[j].jadwalKelas >= listMat[i].jadwalKelas and listMat[j].jadwalKelas < (listMat[i].jadwalKelas + listMat[i].lamaKelas):
                    result -= 10000
                elif listMat[i].jadwalKelas >= listMat[j].jadwalKelas and listMat[i].jadwalKelas < (listMat[j].jadwalKelas + listMat[j].lamaKelas):
                    result -= 10000

        # cek Collision jadwal ujian
        for j in range(i+1,state.__len__()):
            if state[j] == 1:
                if listMat[j].jadwalUjian >= listMat[i].jadwalUjian and listMat[j].jadwalUjian < (listMat[i].jadwalUjian + 3):
                    result -= 2000
                elif listMat[i].jadwalUjian >= listMat[j].jadwalUjian and listMat[i].jadwalUjian < (listMat[j].jadwalUjian + 3):
                    result -= 2000

    return result

# function u/ cek kembar
def cekKembar(active:list) -> int:
    result = 0
    a,b = np.unique(active,return_counts=True)
    for i in b:
        if i>1:
            result -= 50000*(i-1)
    return result

# function u/ cek fitness SKS
def cekSks(count:int,minSks:int,maksSks:int) -> int:
    if count > maksSks:
        return -10000
    elif count < minSks :
        return -10000*(minSks - count)
    else:
        return 200-(maksSks-count)*20

# function u/ cek fitness Jam
def cekJam(count:list,maksJam:list) -> int:
    result = 0
    for i in range(count.__len__()):
        if count[i] > maksJam[i]:
            result -= 2*(count[i]-maksJam[i])
        else:
            result += 2*(maksJam[i]-count[i])
    return result

# function u/ cek fitness hari masuk & libur
def cekHari(count:list,hariMasuk:list) -> int:
    result = 0
    for i in range(count.__len__()):
        if count[i] == 0 and hariMasuk[i] == 0:
            result += 50
        elif count[i] > 0 and hariMasuk[i] == 0:
            result -= 50
        elif count[i] >= 0 and hariMasuk[i] == 1:
            result += 2
    return result
        


fit = [random.randint(0,1) for i in range(12)]
# fit = [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0]      
listMat = [Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",15,6,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",30,6,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",4,6,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",45,4,12,2),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",13,6,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",33,6,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",60,4,12,2),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",88,6,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",105,4,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",88,4,12,2),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",66,6,12,3),
    Matkul("Analisis Proses Bisnis","APB","A","P 502","Krisna Wahyudi",10,6,12,3)]
# print(fit)
# print('Fitness:',cekFitness(fit,listMat))