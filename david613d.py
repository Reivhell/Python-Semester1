hasil = 0

while True:
    print()
    print('Program Perhitungan Menggunakan Perulangan')
    print('=' * 50)
    print()

    b1 = int(input('Masukkan Bilangan Pertama: '))
    b2 = int(input('Masukkan Bilangan Kedua: '))

    if b1 >= b2:
        b1 = b1 - b2
        hasil = hasil + 1
        print('Hasil Perhitungan = ', hasil)
        print()

    ulang = input('Mau Ulang Program Tekan [Y] / Keluar [T] : ')

    if ulang == 'T':
        break