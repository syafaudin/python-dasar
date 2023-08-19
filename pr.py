import time
start_time = time.time()
#----0+++5---8++++11--
masuk = float(input("Masukkan Nilai ="))
a = masuk > 0
b = masuk < 5
c = masuk > 8
d = masuk < 11
e = (a and b ) or (c and d)

print(" hasil = ", e)

print (" jalannya program", time.time() - start_time)