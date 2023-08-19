import time
start_time = time.time()

'''
1. String menggunakan Single Quote / '-'
2. String menggunakan Double Qoute / "-"
3.
'''
print ('ini adalah single Qouta')
print ("ini adalah single Qouta")

'''
# 2. menggunakan tanda \
jika ada karakter string ' maka tambahkan \ untuk menampilkan print tanda '
'''
print('ayo sholat jum\'at')

'''
#backlash
jika \ masuk ke string maka tambahkan backlash sampai double (\\)
'''
print('C:\\pc\\document\\newfolder')

'''
#tab memberikan tab pada string menggunakan \t
'''
print("ini adalah tab \t\t\t jadi menjauh")

'''
#backspace membuat berdekatan dari kata perkata
'''
print('pertama \bkedua')

'''
#newline membuat baris baru 
'''
print('baris pertama \n baris kedua \n baris ketiga')#LF -> line feed -> Unix, MacOS, Linux
print('====')
print('baris pertama \r baris kedua \r baris ketiga')#CR -> carriage return -> acorn, lips, commodore
print('===')
print('baris pertama \r\n baris kedua \r\n baris ketiga')#CRLF -> line feed carriage return -> windows

'''
# String Literal atau raw
semua akan jadi String tak terkecuali
'''
print(r'semua hanya menjadi alat/ benda / membantu')

'''
#Multiline literal String
semua menjadi String
'''
print("""
nama : saya
kelas : 3
guru : kita
""")
print ("Lama Jalannya program", time.time() - start_time)