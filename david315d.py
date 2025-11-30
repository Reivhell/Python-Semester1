print('Program Menentukan Nilai Terkecil Dari 3 Bilangan')
print('***************************************\n')

b1 = int(input('Masukan Bilangan Pertama: '))
b2 = int(input('Masukan Bilangan Kedua: '))
b3 = int(input('Masukan Bilangan Ketiga: '))

if b1 < b2 and b1 < b3:
    print('Nilai Bilangan Terkecil Adalah Bilangan Pertama Dan Nilainya Adalah', b1)
elif b2 < b1 and b2 < b3:
    print('Nilai Bilangan Terkecil Adalah Bilangan Kedua Dan Nilainya Adalah', b2)
elif b3 < b1 and b3 < b2:
    print('Nilai Bilangan Terkecil Adalah Bilangan Ketiga Dan Nilainya Adalah :' ,b3)
else:
    print('Semua Bilangan Nilainya Sama')