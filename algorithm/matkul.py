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
        
    def print(self):
        print("Nama Matkul : ",self.nama," ",self.paralel)
        print("Jadwal      : ",convertIntToJadwal(self.jadwalKelas,self.lamaKelas))
        print("Nama Dosen  : ",self.dosen)
        print("sks         : ",self.sks)
    
def convertJadwalToInt(hari,jam,menit,minggu=0):
    # sistem penjadwalan kuubah ke angka dengan peraturan sebagai berikut
    # hari hanya ada senin - sabtu (0-5)
    # 1 hari pasti dari 7.30 sampe 20.30 dengan perlompatan tiap 30 menit (27 jadwal)
    # contoh jika senin 8.30 maka di convert menjadi 2
    return (int)(minggu*5*27 + hari*27 + (jam-7)*2 + (menit/30) - 1)
    # hasil convert dalam bentuk 0 hingga sekian mengikuti  

def convertIntToJadwal(convJadwal,lama):
    convJadwal = convJadwal + 1
    minggu = convJadwal/(5*27)
    hari = convJadwal%(5*27)/27
    jam = ((convJadwal%(5*27))%27) + 7
    menit = (((convJadwal%(5*27))%27)%2)*30
    result = ""
    if hari == 0:
        result = 'Senin'
    elif hari == 1:
        result = 'Selasa'
    elif hari == 2:
        result = 'Rabu'
    elif hari == 3:
        result = 'Kamis'
    elif hari == 4:
        result = 'Jumat'
    else:
        result = 'Sabtu'
    jamAkhir = int(jam+lama/2)
    menitAkhir = 0
    if lama%2 == 1 and menit == 30:
        jamAkhir += 1
        menitAkhir = 0
    elif lama%2 == 1 and menit == 0:
        menitAkhir = 30
        
    result += ',' +str(jam) + ':' + str(menit) + '-' + str(jamAkhir) + ':' +str(menitAkhir)
    return result

matkul = Matkul("APB","A","P 502","Krisna Wahyudi",31,6,5,3)
matkul.print()