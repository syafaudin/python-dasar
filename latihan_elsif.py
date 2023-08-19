import time
start_time = time.time()

print("Latihan Membuat Kalkulator".center(40, "="))

a = float(input("Masuukan Angka Pertama = "))
b = float(input("Masuukan Angka kedua = "))
operasi = input("masuukan Operator =")

if operasi == "+":
    print(f"Hasil Penjumlahan Adalah : {a + b}")
elif operasi == "-":
    print(f"Hasil dari penguruangan adalah : {a - b}")
elif operasi == "*" or operasi == "x":
    print(f"Hasil dari perkalian adalah = {a * b}")
elif operasi == "/":
    print(f"Hasil dari pembagian adalah = {a / b}")
else:
    print("Operasi yang anda masukkan salah :(")

print(f"Lama Program dijalankan = {time.time() - start_time} detik")
