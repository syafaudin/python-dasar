from re import A
import time
import datetime as dt

start_time = time.time()
# pakai variabel Hari
hari = dt.date.today()
print(hari)
# String Format date time
print(f"hari ini adalah = {dt.date.today()}")
print(f"hari ini adalah = {hari:%A}")
print(f"Bulan ini adalah = {hari:%B}")
print(f"tahun ini adalah = {hari:%Y}")

print("Latihan".center(20, "="))

tanggal = int(input("Masukkan Tanggal :"))
bulan = int(input("Masukkan Bulan :"))
tahun = int(input("Masukkan Tahun :"))

# tahun di dahulukan lalu bulan lalu tanggal
x = dt.date(tahun, bulan, tanggal)
y = (dt.date.today() - x) // 360
print(f"Umur anda = {y} Tahun")
print("proses waktu program ", time.time() - start_time)
