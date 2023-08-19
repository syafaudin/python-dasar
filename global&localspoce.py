import os

os.system('cls')

# <- ini adalah variable global yang bisa di gunakan di luar fungsi
var_global = "muhammad ilham "


def fungsi():  # <- ini adalah fungsi!
    print(f"perkenalkan nama saya {var_global}")


fungsi()

# cara merubah value varible global


def ubah_var(nama):
    global var_global
    var_global = nama
    print(f"Perkenalkan nama saya {nama}")


ubah_var("syafaudin")

# local scope


def lokal():
    a = "muhammad"
    b = "syafaudin"
    print(f"perkenalkan nama saya {a}{b}")


lokal()
