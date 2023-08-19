import time
start_time = time.time()

a = 6

while a > 5:
    a += 1
    print(f"angka ->{a}")

    if a == 12:
        print(f"angka {a}")

        print("tes ")

print("program kelar")

print(f"lama Program = {time.time() - start_time}")
