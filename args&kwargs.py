from ast import Return, arg


def jumlah(*angka):  # <- (*angka) adalah *args yang bisa input semua
    a = 0
    for i in angka:
        a += i
    return a


hasil = jumlah(5, 5)
print(hasil)


def fungsi(**kwargs):  # <- ini adalah key Word Args digunakan untuk data dict dan input tanpa batas
    print(kwargs)


fungsi(nama="muhammad", umur=99, kelamin="laki-laki")

# study kasus


def math(*args, **kwargs):
    output = 0
    if kwargs["pilih"] == "jumlah":
        for i in args:
            output += i
    elif kwargs["pilih"] == "pengurangan":
        output = 0
        for a in args:
            output -= a
    return output


tampil = math(5, 5, 5, pilih="jumlah")
print(tampil)
