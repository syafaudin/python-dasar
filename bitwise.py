import time
start_time = time.time()

# OR operasi bitwise | 
print("==OR==")
a = 9
b = 5
c = a | b
print("hasil Bitwise OR =", c, 'binary= ',format(c,'08b') )

#AND Operasi Bitwise &
print('==AND==')
d = a & b
print('Hasil Bitwise AND =', d, 'Binary', format(d,'08b'))

# XOR Operasi bitwise ^
print('==XOR==')
e = a ^ b
print('Hasil dari Bitwise =',e, 'Binary =', format(e,'08b'))

# NOT Operasi bitwise ~ 
#mirroring kebalikan dan maju 1 langka
print('==NOT==')
f = ~a
print('Hasil dari Bitwise =',f, 'Binary =', format(f,'08b'))
#Shift right >>
#geser ke kanan 
g = a >>3
print('Nilai a =', a, format(a, '08b'))
print('Nilai a =', g, format(g, '08b'))


print("Jalannya Program", time.time() - start_time)