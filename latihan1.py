import time
start_time = time.time()
print("==== perhitungan dalam TEMPERATUR ===")

data_input = float(input("Masukkan Data Celcius : "))

rearmur = (4/5)*data_input
print ("Hasil Rearmur =", rearmur, "tipe", type(rearmur))

fahrenheit = ((9/5)*data_input)+32
print ("Hasil Fahrenheit =", fahrenheit, "tipe", type(fahrenheit))

kelvin = data_input + 273
print("data Kelvin = ", kelvin, "Tipe", type(kelvin))

print("Proses Program jalan = ", time.time() - start_time, "Detik")