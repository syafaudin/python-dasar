import time
from turtle import st
start_time = time.time()

# menyambung String (concatenate)

a = "hello"
b = "wolrd"
c = "teman-teman"
final = a + " " + b + c
print(final)

# menghintung panjang String

hitung = len(final)
print("jumlah hitung String = ", final)

# operator /u String
# cek apakah ada komponen char atau String di String

d = "h"
cek = d in final
print("cek jika ada karakter H = ", cek)


d = "h"
cek = d not in final
print("cek jika tidak ada karakter H = ", cek)

# ulang String
print("hello" * 5)
print(5*"hello")

# indexing
print("index ke - 0 = " + final[0])
print("index ke - 6 = " + final[6])
print("index range 0-3 adalah : " + final[0:3])
print("index range 0,2,4,6,8 adalah : " + final[0:10:2])

# literasi paling kecil
# hasilnya adalah spaci karena di python termasuk karakter paling awal dari varialbel final
print("Items paling kecil = " + min(final))
print("Items paling besar = " + max(final))

ascii_code = ord("a")
print(" hasil ASCII Code adalah = " + str(ascii_code))

# operator dalam betuk methode

data = "contoh jumlah karakter"
jumlah = data.count("o")
print("jumlah O pada data = " + str(jumlah))

# operator pakai Methods

# merubah case dari String
# merubah semua ke upper case

g = "jet!"
print("pesawat =" + g)
huruf_besar = g.upper()
huruf_kecil = g.lower()
print("Upper = " + huruf_besar)
print("lower = " + huruf_kecil)

# cek isX method
print("=======lower&upper case======")
huruf = " hello world"
cek_lower = huruf.islower()  # hasilnya boollean
print("hasil dari loower = " + str(cek_lower))


'''
-> isalpha()  = u/ cek semua huruf alphabet
-> isalnum() = u/ huruf dan angka
-> isdecimal() = u/ untuk angka saja
-> isspace () = u/ spaci, tab, newline,
-> istitle () = u/ semua dimulai dari huruf besar

'''
# cek komponen startswith()
demo = "Hellow World".startswith("Hellow")
print("cek variabel demo = "+str(demo))

# penggabungan komponen join(), split()
pisah = ['saya', 'ibu', 'ayah']
jadi_satu = ','.join(pisah)
print(pisah)
print(jadi_satu)

barang = "barangshampobaranghpbarangsabun"
print(barang.split('barang'))

# alokasi karakter rjust() ljust() center()
rata_kanan = "hellowWorld".rjust(20)
print(rata_kanan)

rata_kanan = "hellow World".ljust(20)
print(rata_kanan)

rata_kanan = "hellow World".center(20, "=")
print(rata_kanan)

print("syafaudin".center(20, "+"))

# kebalikannya -> Strip()


print("proses lama ", time.time() - start_time)
