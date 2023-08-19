import time
import os
start_time = time.time()


def header():
    os.system('cls')
    print("="*50)
    print(f"Program Perhitunga".center(50, "="))
    print("="*50)


def footer():
    print("Program Selesai!")
    print(f"Proses {time.time() - end_time}")


def input_nilai():
    panjang = int(input("Masukkan Panjang ->"))
    lebar = int(input("Masukkan Lebar ->"))
    return panjang, lebar


def hitung_luas(panjang, lebar):
    hasil = panjang * lebar
    return hasil


def hitung_keliling(panjang, lebar):
    return 2*(panjang+lebar)


while True:
    header()
    print("""
    Pilih No untuk Perhitungan!
    1 -> Menghitung Luas
    2 -> Menghitung Keliling
    3 -> Menghitung Semua!
    """)
    pilih = int(input("Masukkan pilihan ->"))
    if pilih == 1:
        Lebar, Panjang = input_nilai()
        aa = hitung_luas(Lebar, Panjang)
        print(f"Hasil Perhitungan Luas -> {aa}")
    elif pilih == 2:
        Lebar, Panjang = input_nilai()
        ab = hitung_keliling(Panjang, Lebar)
        print(f"Hasil Perhitungan Keliling ->{ab}")
    elif pilih == 3:
        Lebar, Panjang = input_nilai()
        x = hitung_keliling(Panjang, Lebar)
        y = hitung_luas(Panjang, Lebar)
        print(f"Hasil Perhitungan Luas ->{y}")
        print(f"Hasil Perhitungan Keliling ->{x}")

    a = input("Lanjutkan y/n ?")
    if a == "n" or a == "N":
        break

end_time = time.time()
footer()
