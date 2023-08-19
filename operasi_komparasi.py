import time
start_time = time.time()

a= 6
b= 7

selesai = a < 7
print("Hasil dari =", selesai)

#is sebagai object komparasi idenity
#is not jika beda

c = 5
y = 5
print("Nilai C =", c, "ID =", hex(id(c)))
print("Nilai y =", y, "ID =", hex(id(y)))
hasil = c is y
print("Hasil = ",hasil)

print("Lama Proses Program", time.time() - start_time)