import json
from flask import jsonify
import main

def get_dosen() :
    dosen = []
    x = main.db.session.query(main.db_matkul.dosen).distinct().all()
    for i in x:
        dosen.append(i[0])
    return jsonify(dosen)
    

def get_matkul():
    pass

def insert_matkul(data):
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

def generate(filter : list):
    pass
