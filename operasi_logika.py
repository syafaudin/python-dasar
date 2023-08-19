from operator import truediv
import time
start_time = time.time()

#operasi Logika / Boolean
#not, or, and, xor

a = True
b = False

print ("==NOT==")
#jika hasil sesuai maka False
hasil = not b
print("hasil dari =", hasil)
print("==OR==")
#jika salah satu true maka akan true
a = False
b = False
hasil = a or b
print("hasil dari = ", hasil) 
a = True
b = False
hasil = a or b
print("hasil dari = ", hasil) 
a = False
b = True
hasil = a or b
print("hasil dari = ", hasil) 
a = True
b = True
hasil = a or b
print("hasil dari = ", hasil) 

print("==Flase==")
#jika salah satu false maka akan false
a = False
b = False
hasil = a and b
print("hasil dari = ", hasil) 
a = True
b = False
hasil = a and b
print("hasil dari = ", hasil) 
a = False
b = True
hasil = a and b
print("hasil dari = ", hasil) 
a = True
b = True
hasil = a and b
print("hasil dari = ", hasil) 

print("==XOR==")
#jika salah satu saja yang True maka akan true, sisanya Flase 
a = False
b = False
hasil = a ^ b
print("hasil dari = ", hasil) 
a = True
b = False
hasil = a ^ b
print("hasil dari = ", hasil) 
a = False
b = True
hasil = a ^ b
print("hasil dari = ", hasil) 
a = True
b = True
hasil = a ^ b
print("hasil dari = ", hasil) 
print("Proses Program", time.time() - start_time)
