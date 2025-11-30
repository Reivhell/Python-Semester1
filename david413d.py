print('Program Menghitung Luas')
print('************************\n')
print('\n')

print('Pilih Menu : \n')
print(
'1.Luas Lingkaran\n' \
'2.Luas Persegi\n' \
'3.Luas Segitiga\n')


Pilihan = int(input('Masukan Pilihan Anda : '))
print('\n')

match Pilihan:
    case 1:
        print('Program Penghitung Luas Lingkaran')
        print('*********************************\n')

        jari = int(input('Masukan Jari-Jari Lingkaran : '))
        luas = 3.14 * jari * jari
        print('Luas Lingkaran Adalah : ', luas)

    case 2:
        print('Program Penghitung Luas Persegi')
        print('*******************************\n')

        p = int(input('Masukan Panjang Persegi : '))
        l = int(input('Masukan lebar Persegi : '))
        luas = p * l
        print('Luas Persegi Adalah : ', luas)

    case 3:
        print('Program Penghitung Luas Segitiga')
        print('********************************\n')

        a = int(input('Masukan Alas Segitiga : '))
        t = int(input('Masukan Tinggi Segitiga : '))

        luas = 0.5 * a * t
        print('Luas Segitiga Adalah : ', luas)

    case _:
        print('Pilihan Menu Tidak Ada')
