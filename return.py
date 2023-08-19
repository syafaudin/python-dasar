import time
start_times = time.time()

print("Return".center(20, "="))
"""
-> def nama)fungsi(argument):
-> body funcition
-> return output
"""


def nilai_awal(a, b):
    f = a + b
    return f


def nilai_kedua(a):
    j = a**2
    return j


a = int(input("Masukkan Nilai A = "))
b = int(input("Masukkan Nilai B = "))

d = nilai_awal(a, b) - 12
print(d)

g = nilai_awal(a, b) * 2
print(g)

h = nilai_kedua(a) + 2
print(h)


print("Jalannya Program", time.time() - start_times, "detik")
