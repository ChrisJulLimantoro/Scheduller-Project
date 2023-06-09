import json
from flask import jsonify
import main
import algorithm.matkul as mat
import algorithm.algo as algo
import pandas as pd

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
        matkul['jadwal_ujian_mgg'],matkul['jadwal_ujian_hari'],matkul['jadwal_ujian_jam'] = mat.convertIntToJadwal(i.jadwal_ujian,3)
        matkul['sks'] = i.sks
        jadwal.append(matkul)
    return jsonify(jadwal)

def upload_matkul(data):
    response = {}
    response['status'] = 0
    if not data.filename.endswith('.csv'):
        return jsonify(response)
    else:
        data.save('temp.csv')
        df = pd.read_csv('temp.csv')
        for i in range(df.shape[0]):
            nama = df.iloc[i,1]
            sing = df.iloc[i,2]
            par = df.iloc[i,3]
            dos = df.iloc[i,4]
            rua = df.iloc[i,5]
            jk = int(df.iloc[i,6])
            lama = int(df.iloc[i,7])
            ju = int(df.iloc[i,8])
            sks = int(df.iloc[i,9])
            matkul = main.db_matkul(name=nama,singkatan=sing,paralel=par,dosen=dos,ruangan=rua,jadwal_kuliah=jk,lama_kuliah=lama,jadwal_ujian=ju,sks=sks)
            main.db.session.add(matkul)
            main.db.session.commit()
        response['status'] = 1
        return jsonify(response)

def insert_matkul(data:list):
    # for i in data:
    nama = data['nama']
    sing = data['sing']
    par = data['par']
    dos = data['dos']
    rua = data['rua']
    mulai_kuliah = mat.convertJadwalToInt(int(data['hari_kuliah']), int(data['jam_mulai']), int(data['menit_mulai']))
    selesai_kuliah = mat.convertJadwalToInt(int(data['hari_kuliah']), int(data['jam_selesai']), int(data['menit_selesai']))
    jk = mulai_kuliah
    lama = selesai_kuliah - mulai_kuliah
    ju = mat.convertJadwalToInt(int(data['hari_ujian']), int(data['jam_mulai_ujian']), int(data['menit_mulai_ujian']), int(data['minggu_ujian']))
    sks = int(data['sks'])

    insertId = (main.db_matkul.query.count()+1)
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
    for i in range(1):
        best = []
        best = algo.run(listMat,filt['minSKS'],filt['maxSKS'],filt['hariMasuk'],filt['maksJam'],filt['dosen'],filt['matkulFav'],best)

        # states = []
        # states = algo.generateStates(listMat,filt['maxSKS'])
        # best = []
        # best = algo.findBest(listMat,filt['minSKS'],filt['maxSKS'],filt['hariMasuk'],filt['maksJam'],filt['dosen'],filt['matkulFav'],best)

        # return best
        if bestGlobal == []:
            bestGlobal = best
            bestGlobal = sorted(bestGlobal, key=lambda x : x[1], reverse=True)
        else:
            for k in best:
                duplicate = True
                for j in bestGlobal:
                    duplicate = algo.cekKembar(k, j)

                if not duplicate and k[1] > bestGlobal[2][1]:
                    bestGlobal.append(k)
                    duplicates = sorted(bestGlobal, key=lambda x : x[1], reverse=True)
                    bestGlobal.pop(3)
    result = []
    listMatkul2 = []
    # return jsonify(bestGlobal)
    for i in bestGlobal:
        for j in range(i[0].__len__()):
            if i[0][j] == 1:   
                matkul = {}
                matkul['nama'] = listMat[j].nama
                matkul['singkatan'] = listMat[j].singkatan
                matkul['dosen'] = listMat[j].dosen
                matkul['paralel'] = listMat[j].paralel
                matkul['ruangan'] = listMat[j].ruangan
                matkul['jadwal_kuliah'] = listMat[j].jadwalKelas
                matkul['jadwal_kuliah_mgg'],matkul['jadwal_kuliah_hari'],matkul['jadwal_kuliah_jam'] = mat.convertIntToJadwal(listMat[j].jadwalKelas,listMat[j].lamaKelas)
                matkul['lama_kuliah'] = listMat[j].lamaKelas
                matkul['jadwal_ujian'] = listMat[j].jadwalUjian
                matkul['jadwal_ujian_mgg'],matkul['jadwal_ujian_hari'],matkul['jadwal_ujian_jam'] = mat.convertIntToJadwal(listMat[j].jadwalUjian,6)
                matkul['sks'] = listMat[j].sks
                listMatkul2.append(matkul)
        listMatkul2 = sorted(listMatkul2, key=lambda x : x['jadwal_kuliah'])
        result.append([listMatkul2, i[1]])
        listMatkul2 = []
    result = sorted(result, key=lambda x : x[1], reverse=True) 
    return jsonify(result)