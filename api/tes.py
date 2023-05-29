import json
from flask import jsonify
import main
import algorithm.matkul as mat
import algorithm.algo as algo

def get_dosen() :
    dosen = []
    x = main.db.session.query(main.db_matkul.dosen).distinct().all()
    for i in x:
        dosen.append(i[0])
    return jsonify(dosen)
    

def get_matkul():
    matkul = []
    x = main.db.session.query(main.db_matkul.singkatan).distinct().all()
    for i in x:
        matkul.append(i[0])
    return jsonify(matkul)

def get_jadwal():
    jadwal = []
    jad = main.db_matkul.query.all()
    for i in jad:
        matkul = {}
        matkul['id'] = i.id
        matkul['nama'] = i.name
        matkul['singkatan'] = i.singkatan
        matkul['dosen'] = i.dosen
        matkul['paralel'] = i.paralel
        matkul['ruangan'] = i.ruangan
        matkul['jadwal_kuliah'] = i.jadwal_kuliah
        matkul['jadwal_kuliah_mgg'],matkul['jadwal_kuliah_hari'],matkul['jadwal_kuliah_jam'] = mat.convertIntToJadwal(i.jadwal_kuliah,i.lama_kuliah)
        matkul['lama_kuliah'] = i.lama_kuliah
        matkul['jadwal_ujian'] = i.jadwal_ujian
        matkul['jadwal_ujian_mgg'],matkul['jadwal_ujian_hari'],matkul['jadwal_ujian_jam'] = mat.convertIntToJadwal(i.jadwal_ujian,6)
        matkul['sks'] = i.sks
        jadwal.append(matkul)
    return jsonify(jadwal)

def insert_matkul(data:list):
    for i in data:
        nama = data[i]['nama']
        sing = data[i]['singkatan']
        par = data[i]['paralel']
        dos = data[i]['dosen']
        rua = data[i]['ruangan']
        jk = data[i]['jadwal_kuliah']
        lama = data[i]['lama_kuliah']
        ju = data[i]['jadwal_ujian']
        sks = data[i]['sks']
        matkul = main.db_matkul(name=nama,singkatan=sing,paralel=par,dosen=dos,ruangan=rua,jadwal_kuliah=jk,lama_kuliah=lama,jadwal_ujian=ju,sks=sks)
        main.db.session.add(matkul)
    main.db.session.commit()
    return "1"

def generate(active:list,filt:list, iterarion:int) -> list:
    jad = main.db_matkul.query.all()
    listMat = []
    
    for i in jad:
        if i.id in active:
            newMat = mat.Matkul(i.name,i.singkatan,i.paralel,i.ruangan,i.dosen,i.jadwal_kuliah,i.lama_kuliah,i.jadwal_ujian,i.sks)
            listMat.append(newMat)
        else:
            continue

    bestGlobal = []
    for i in range(iterarion):
        best = []
        best = algo.run(listMat,filt['minSKS'],filt['maxSKS'],filt['hariMasuk'],filt['maksJam'],filt['dosen'],filt['matkulFav'],best)

        # states = []
        # states = algo.generateStates(listMat,filt['maxSKS'])
        # best = []
        # best = algo.findBest(listMat,filt['minSKS'],filt['maxSKS'],filt['hariMasuk'],filt['maksJam'],filt['dosen'],filt['matkulFav'],best)

        print(best)
        if bestGlobal == []:
            bestGlobal = best
            sorted(best, key=lambda x : x[1])
        else:
            for k in best:
                if k[1] > bestGlobal[2][1] and not algo.cekKembar(k, bestGlobal) :
                    bestGlobal[2] = k
                    sorted(best, key=lambda x : x[1])
            
    return jsonify(bestGlobal)