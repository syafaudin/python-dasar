import time
start_time = time.time()
daftar = []
while True:
    a = input("Masukkan data \t=")
    b = int(input("Masukkan Nilai \t="))

    ab = [a, b]
    daftar.append(ab)
    for index, tampil in enumerate(daftar):
        print(f"{index+1}| Nama ->{tampil[0]} | Nilai ->{tampil[1]}")
    lanjut = input("Lanjutkan y/n?")
    if lanjut == "n" or lanjut == "N":
        break
    elif lanjut == "y" or lanjut == "Y":
        continue
    else:
        print("Perintah Salah !")
        break
print("Program Telah selesai")
print(f"Proses Program ={time.time() - start_time}")
