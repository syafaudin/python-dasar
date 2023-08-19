#gerbang program
#__name___ = "__main__"

from unicodedata import name


print(__name__)


#contoh penggunaan __main__

#deklarasi
def tambah(a:int,b:int)->int:
    return a+b

if __name__== "__main__":
    angka_1 = 5
    angka_2 =10
    hasil = tambah(angka_1,angka_2)
    print(f"Hasilnya adalah = {hasil}")
else:
    print("Program Selesai !")