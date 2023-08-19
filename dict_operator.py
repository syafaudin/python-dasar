import time
start_time = time.time()

a = {
    "nim": 2983928,
    "nama": "syafaudin",
    "kelas": 8
}

for data, data1 in a.items():  # mulai bisa values, keys
    print(f" Key ->{data} values->{data1}")

b = a.copy()
print(b)

c = a.pop("nama")
print(c)
print(a)  # maka key= nama tidak ada

d = a.popitem()
print(d)
print(a)
print(f"Proses Program ={time.time() - start_time}")
