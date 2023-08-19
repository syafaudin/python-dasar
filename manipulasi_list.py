import imp


import time
start_time = time.time()

a = [2, 3, 5, 6, 8, 9, 9, 4, 2, 12, 43, 56, 86, 32, 56]
print(a)

# menghitung data yang sama

hitung = a.count(2)
print(f"berapa Angka 2 ->{hitung}")

cari = a.index(6)  # mulai hitung list 2->0, 3->1 dst
print(f"di temukan data ada di ->{cari}")

# mengururtkan data
a.sort()
print(a)

# mengurutkan mulai dari yang besar terlebih dahulu
a.reverse()
print(a)


print(f"Proses Program {time.time() - start_time}")
