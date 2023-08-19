import time
start_time = time.time()
print("List Buku".center(30, "="))

tampung = []
while True:
    a = input("Masukkan Judul\t :")
    b = input("Masukkan Pengarang\t :")
    Listbaru = [a, b]
    tampung.append(Listbaru)
    print("Daftar List".center(30, "="))
    for index, tampil in enumerate(tampung):
        print(f"{index+1}| Judul ->{tampil[0]}|Pengarang ->{tampil[1]}")
    z = input("Lanjutkan y/n?")
    if z == "n" or z == "N":
        break

print("Program telah selesai!")


print(f"Lama program berjalan = {time.time() - start_time}")
