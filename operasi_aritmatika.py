import time

start_time = time.time()

# Operator Bilangan Eksponen
#angka1 = int(input("Masukkan Angka ="))
#angka2 = int(input("Masukkan Angka ke 2 ="))
#hasil = angka1 ** angka2
#print("Hasil dari Bilangan Pangkat adalah = ", hasil)

print("====Modulus====")
# Modulus Hasil dari sisa Pembagian
angka3 = int(input("Masukkan Angka ="))
angka4 = int(input("Masukkan Angka ke 2 ="))
hasil1 = angka3 % angka4
print("Hasil dari Bilangan Pangkat adalah = ", hasil1)

print("====Floor Division====")

# pembagian yang di bulatkan ke bawah
#angka3 = int(input("Masukkan Angka ="))
#angka4 = int(input("Masukkan Angka ke 2 ="))
#hasil1 = angka3 // angka4
#print("Hasil dari Bilangan Pangkat adalah = ", hasil1)

print("waktu Proses program jalan", time.time() - start_time)
