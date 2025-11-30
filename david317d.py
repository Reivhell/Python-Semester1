print('Kalkulator Sederhana')
print('********************\n')

print('Masukan Operasi Yang Ingin Dilakukan :\n'
    '1.Penjumlahan\n'
    '2.Pengurangan\n'
    '3.Perkalian\n'
    '4.Pembagian\n'
)

operasi = input('Masukan Operasi (1/2/3/4) : ')

a1 = int(input('Masukan Angka Pertama : '))
a2 = int(input('Masukan Angka Kedua : '))

if operasi == '1':
    tambah = a1 + a2
    print(f'Hasil Penjumlahan {a1} + {a2} = {tambah}')

elif operasi == '2':
    kurang = a1 - a2
    print(f'Hasil Pengurangan {a1} - {a2} = {kurang}')

elif operasi == '3':
    kali = a1 * a2
    print(f'Hasil Perkalian {a1} * {a2} = {kali}')

elif operasi == '4':
    bagi = a1 / a2
    a1 != 0
    print(f'Hasil Pembagian {a1} ÷ {a2} = {bagi}')

else:
    print('Tidak Ada Operasi Yang Tersedia')