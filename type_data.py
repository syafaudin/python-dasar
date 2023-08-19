import time
start_time = time.time()

data_int = 10
print ("data:", data_int, "tipe=", type(data_int))

data_flot = 1.6
print ("data:", data_flot, "tipe=", type(data_flot))

data_string = "saya mencari ikan"
print ("Data = ", data_string, "tipe", type(data_string))

data_bolean = True
print ("data =", data_bolean, "tipe =",type(data_bolean))

data_complex = complex(10,5)
print("Data =", data_complex, "Tipe=",type(data_complex) )

#tipe bahasa C# dari python

from ctypes import c_double
data_c_double = c_double(10.6)
print("data = ", data_c_double, "tipe =",data_c_double )

#Casting Type Data

int = 11 
print ("Data = ", int, " Tipe =", type(int) )

flo = float(int)
STR = str(flo)
boo = bool(STR)

print ("data =", flo, "tipe", type(flo))
print ("data =", STR, "tipe", type(STR))
print ("data =", boo, "tipe", type(boo))


print ("waktu yang di butuhkan =",time.time() - start_time)
