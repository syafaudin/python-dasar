import time
start_time = time.time()

print('Contoh Generic'.center(20, "="))
# tipe data String
sebutan = "Syafaudin"
format_str = f"Nama Saya {sebutan}"
print(format_str)
# tipe data INT
a = 200.6
format_str = f"ini adalah angka = {a,type(a)}"
print(format_str)

# tipe data Boolean

boolean = True
print(f" hasil dari Booleam {boolean, type(boolean)}")

angka = 200000
print(f"Hasil dari bilangan variabel angka = {angka:,}", type(angka))

b = 2000.7687232
# maksut dari {b:.2f} ambil angka di belakang koma dan f adalah float
print(f"angka variabel B = {b:.2f}")
# menampilkan leading zero
# akan menjorok ke belakang sebenarnya adalah nilai
print(f"tampilkan Leading Zero :{b:10.1f}")
# jika di tambah angka di depannya akan menambah angka tersebut dan wajib 0
print(f"tampilkan Leading Zero :{b:010.1f}")
print("lama program di jalankan : ", time.time() - start_time)
presentase = 0.00564
print(f"Hasil angka persen {presentase:%} ")
print(f"Hasil angka persen {presentase:.1%} ")

harga = 1000
jumlah = 10
print(f"Total harga =RP{harga*jumlah:,}")

# format angka hexdecimal, binary,octal

nilai = 200
print(f"Angka Biner = {bin(nilai), type(nilai)}")
print(f"Angka Biner = {hex(nilai), type(nilai)}")
print(f"Angka Biner = {oct(nilai), type(nilai)}")
