import time
start_time = time.time()

#input data outputnya selalu tipe data STRING

data = input("Masukkan Data = ")
print ("Data adalah = ", data, "tipe = ", type(data))


# Casting input Data INT

data_int = int(input("Masukkan Angka :"))
data_int2 = int(input("Masukkan Angka ke 2 :"))
hasil = data_int + data_int2
print ("hasil dari Angka = ", hasil, "Tipe - ", type(hasil))

#untuk type data boolean harus di casting ke data interger
data_boolean = bool(int(input("Masukkan nilai Boolean :")))
print ("Hasil Boollean ", data_boolean, "Tipe =", type(data_boolean))

print ("proses program dijalankan ", time.time() - start_time)
