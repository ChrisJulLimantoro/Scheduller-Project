class Matkul:
    def __init__(self, nama, singkatan, paralel, ruangan, dosen, jadwalKelas, lamaKelas, jadwalUjian, sks):
        self.nama = nama
        self.singkatan = singkatan
        self.paralel = str.upper(paralel)
        self.ruangan = str.upper(ruangan)
        self.dosen = str.title(dosen)
        self.jadwalKelas = jadwalKelas
        self.lamaKelas = lamaKelas
        self.jadwalUjian = jadwalUjian
        self.sks = sks
    
def convertJadwalToInt(hari,jam,menit,minggu=0):
    # sistem penjadwalan kuubah ke angka dengan peraturan sebagai berikut
    # hari hanya ada senin - sabtu (0-5)
    # 1 hari pasti dari 7.30 sampe 20.30 dengan perlompatan tiap 30 menit (27 jadwal)
    # contoh jika senin 8.30 maka di convert menjadi 2

    return (int)(minggu*6*27 + hari*27 + (jam-7)*2 + (menit/30) - 1)
    # hasil convert dalam bentuk 0 hingga sekian mengikuti  

def convertIntToJadwal(convJadwal,lama):
    convJadwal = convJadwal + 1
    minggu = (int)(convJadwal/(6*27))+1
    hari = (int)(convJadwal%(6*27)/27)
    jam = (int)(((convJadwal%(6*27))%27)/2 + 7)
    menit = (int)((((convJadwal%(6*27))%27)%2)*30)
    res_jam = ""
    res_hari = ""
    if hari == 0:
        res_hari = 'Senin'
    elif hari == 1:
        res_hari = 'Selasa'
    elif hari == 2:
        res_hari = 'Rabu'
    elif hari == 3:
        res_hari = 'Kamis'
    elif hari == 4:
        res_hari = 'Jumat'
    else:
        res_hari = 'Sabtu'
    jamAkhir = int(jam+lama/2)
    menitAwal = ''
    if menit == 0:
        menitAwal = '00'
    else:
        menitAwal = '30'
    menitAkhir = '00'
    if lama%2 == 1 and menit == 30:
        jamAkhir += 1
        menitAkhir = '00'
    elif lama%2 == 1 and menit == 0:
        menitAkhir = '30'
    elif lama%2 == 0 :
        menitAkhir = menitAwal
    res_jam +=  str(jam) + ':' + menitAwal + '-' + str(jamAkhir) + ':' + menitAkhir
    return minggu,res_hari,res_jam