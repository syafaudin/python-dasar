import time
start_time = time.time()

print(f"Perulangan FOR".center(30, "="))
for a in range(1, 10):
    print(a)

for b in range(10):
    print(f"saya tidak akan mengulangi perbuatan saya lagi")

print(f"Perulangan While".center(30, "="))

x = 0
while x < 4:
    x += 1
    print(f"ini adalah angka {x}")

print(f"Lama Program di proses adalah {time.time() - start_time} detik")
