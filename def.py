import os

os.system('cls')


def intro(nama):
    print(f"perkenalkan nama saya {nama}")


intro("udin")


def perkenalan(daftar):
    data_daftar = daftar.copy()
    for a in data_daftar:
        print(F"Perkenalkan Nama saya {a}")


nama_nama = ["muhammad", "ilham", "syafaudin",
             "birul", "amrillah", "al", "hadi"]
perkenalan(nama_nama)
