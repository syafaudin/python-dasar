a = ["muhammad", 25, "islam"]
b = ["syafaudin", 20, "islam"]
c = ["hadi", 23, "islam"]

jn = [a, b, c]
print(jn)

for jadisatu in jn:
    print(f"Nama \t->{jadisatu[0]}")
    print(f"umur \t->{jadisatu[1]}")
    print(f"Agama \t->{jadisatu[2]} \n")

    ab = [1, 4]
    ac = [5, 2]

    aw = [ab, ac]
    print(aw)

    ad = aw.copy()
    print(hex(id(aw)))
    print(hex(id(ad)))

    print(f"per satuan data cek addres")
    print("hasil addres data ->", hex(id(aw[0])))
    print(f"Hasil Addres data ->", hex(id(ad[0])))

    from copy import deepcopy
    deepcopi = deepcopy(aw)
    print(f"Hasil dari addres setelah deepcopy", hex(id(deepcopi[0])))
    print(f"Hasil dari addres setelah copy", hex(id(aw[0])))
