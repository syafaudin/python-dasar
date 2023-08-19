import time
start_time = time.time()

list_angka = [1, 2, 3, 4, 5, 6, ]
print(list_angka)

list_huruf = ["saya", "kamu", "dia"]
print(list_huruf)

list_boolleam = [True, False, True]
print(list_boolleam)

list_mix = [1, "saya", True]
print(list_mix)

a = range(0, 12, 2)  # range (start, stop, step)
print(a)
b = list(a)
print(b)

x = [i**2 for i in range(2, 10)]
print(x)

j = [a for a in range(2, 20) if a % 2 == 0]
print(j)

# tampilak data 1 saja
nama = ["saya", "aku", "dia", "mas"]  # di mulai dari 0= saya, 1 = aku dst
tamp = nama[2]
print(f"tampilakn nama = {tamp}")

# menampilkan pajnag data
panj = len(nama)
print(f"banyak data adalah = {panj}")

nama.insert(2, "kita")  # bisa menambahkan tipe data yang lain
print(nama)

# menambahkan di akhir list
nama.append("mereka")
print(nama)

# yang di remove harus sama karena python senseitive case
nama.remove("mereka")
print(nama)

# menggabungkan List
nama2 = ["udin", "syafaudin", "ilham"]
# saat di print harus objecy yang di menggunakan fungsi tersebut
nama.extend(nama2)
print(nama)

# edit list
nama[3] = "adek"
print(nama)

nama.pop()
print(nama)
print(f"lama program {time.time() - start_time}")
