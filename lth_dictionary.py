import time
import datetime
import os
import random
import string

start_time = time.time()
datas_mhs = {}
while True:
    os.system("cls")

    ex_mhs = {
        "nim": 0000000000,
        "nama": "nama",
        "fakultas": "fakultas",
        "jurusan": "jurusan",
        "wkt_msk": datetime.datetime(1111, 11, 11)
    }

    print("="*30)
    print("DATA INPUT MAHASISWA".center(30, "="))
    print("="*30)
    mhs = dict.fromkeys(ex_mhs.keys())
    mhs['nim'] = input("Masukkan NIM ->")
    mhs['nama'] = input("Masukkan Nama ->")
    mhs['fakultas'] = input("Masukkan Fakultas ->")
    mhs['jurusan'] = input("Masukkan Jurusan ->")
    tahun = int(input("Masukkan Tahun (YYYY) ->"))
    bulan = int(input("Masukkan Bulan (BB)->"))
    tanggal = int(input("Masukkan Tanggal (TT) ->"))
    mhs['wkt_msk'] = datetime.datetime(tahun, bulan, tanggal)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    datas_mhs.update({KEY: mhs})
    for mahasiswa in datas_mhs:
        KEY = mahasiswa
        NIM = datas_mhs[KEY]['nim']
        NAMA = datas_mhs[KEY]['nama']
        FAKULTAS = datas_mhs[KEY]['fakultas']
        JURUSAN = datas_mhs[KEY]['jurusan']
        WAKTU_MASUK = datas_mhs[KEY]['wkt_msk'].strftime("%x")
        print(
            f"{KEY:<6}  {NIM:<8} {NAMA:<25} {FAKULTAS:<8} {JURUSAN:<11} {WAKTU_MASUK:<9}")
    a = input("Lanjutkan y/n ?")
    if a == "n" or a == "N":
        break
print("Program Selesai !")
print(f"Proses Program {time.time() - start_time}")
