import time
start_time = time.time()

a = [1, 2, 4, 57, 8, 6, 8, 5]
# b = list(("saya", "bukan", "udin"))#list konstruktor
# print(a[0:5])#menampilkan nilai index sesuai urutan yang di inginkan
# print(a[:3])# menampikan index dari 0
# print(a[3:])# menapilkan di awal index mulai dari 3
# salin = a.copy() untuk mencopy list
# a[1] = 12 #merubah list sesuai index yang di tentukan
# a.remove(2)#menghapus list sesuai index
# a.pop()#menghapus list di akhir list
# a.sort()#mengururtkan list dari kecil ke besar
# a.reverse()#membalikkan list, kalau ingin dari besar ke kecil di sort terlebih dahulu
# a.insert(2, 12)#mengubah list sesuai index 2 adalah index 12 adalah yang nilai yang di ubah
# a.append(12)  # menambahkan list index yang paling akhir
# a.clear()  # menghapus semua list pada varible
# print(a[2])#menampilkan list sesuai index
print(a)

# dictionary (dict) -> assosiative array

z = {
    "org1": "ilham",
    "orag2": "syafaudin",
    "org3": "birul"

}
print(z)  # menampilkan semua value
# panjang = len(z) # menghitung banyak data
# print(z["org1"])#menampilkan data sesuai key
# key = "org1"  # cek data sesuai key
#checking = key in z#
#print(checking)#
# print(z.get("org5","Tidak dapat di temukan"))#cek value pakai get, ke 2 untuk pesan
# z.update({"ilham": "hadi"})mengubah value jika tidak ada maka akan di tambahkan
del z["org3"]
print(z)
# arry tupple
# sifatnya konstan tidak bisa di ubah
x = (1, 2, 3, 5, 6, 8)
print(x)
print(f"Proses Program {time.time() - start_time} detik")
