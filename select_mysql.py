import mysql.connector as sql

konek = sql.connect(
    host='localhost',
    user='root',
    database='analisa_harga',
    password=''
)

a = konek.cursor()
b = "select * from data_bulanan "
a.execute(b)
tampilkan = a.fetchall()

for i in tampilkan:
    print(i)
