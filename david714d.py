def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b

while True:
    print()
    print('Program Perhitungan Menggunakan Function')
    print('++++++++++++++++++++++++++++++++++++++++')
    print()

    b1 = int(input('Masukkan Bilangan Pertama : '))
    b2 = int(input('Masukkan Bilangan Kedua : '))

    print(b1, '+', b2, '=', tambah(b1, b2))
    print(b1, 'x', b2, '=', '%.2f' % kali(b1, b2))
    print()

    ulang = input('Mau Ulang Program Tekan [Y] / Keluar [T] : ')

    if ulang == 'T':
        break
