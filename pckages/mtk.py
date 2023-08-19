def tambah(*args):
    nilai = 0
    for angka in args:
        nilai += angka
    return nilai


def kali(*args):
    nilai = 1
    for angka in args:
        nilai *= angka
    return nilai


def pangkat(n):
    return lambda angka: angka**n


print(pangkat(12))
