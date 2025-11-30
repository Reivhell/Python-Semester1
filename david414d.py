print('Kalkulator Sederhana Dengan MATCH CASE')
print('======================================\n')

print('Pilih Operasi Yang Ingin Anda Gunakan : \n')
print(
'1. Penjumlahan\n' \
'2. Pengurangan\n' \
'3. Perkalian\n' \
'4. Pembagian\n')

Pilihan = int(input('Masukan Pilihan Anda : '))

match Pilihan:
    case 1:
        print('Program Penjumlahan')
        print('===================\n')

        a1 = int(input('Masukan Angka Pertama : '))
        a2 = int(input('Masukan Angka Kedua : '))

        add = a1 + a2
        print('Hasil Penjumlahan Dari ',a1, '+' ,a2, 'Adalah = ', add)

    case 2:
        print('Program Pengurangan')
        print('===================\n')

        a1 = int(input('Masukan Angka Pertama : '))
        a2 = int(input('Masukan Angka Kedua : '))

        substract = a1 - a2
        print('Hasil Pengurangan Dari ',a1, '-' ,a2, 'Adalah = ', substract)

    case 3:
        print('Program Perkalian')
        print('===================\n')

        a1 = int(input('Masukan Angka Pertama : '))
        a2 = int(input('Masukan Angka Kedua : '))

        multiply = a1 * a2
        print('Hasil Perkalian Dari ',a1, 'x' ,a2, 'Adalah = ', multiply)

    case 4:
        print('Program Pembagian')
        print('===================\n')

        a1 = int(input('Masukan Angka Pertama : '))
        a2 = int(input('Masukan Angka Kedua : '))

        divide = a1 / a2
        print('Hasil Pembagian Dari ',a1, '÷' ,a2, 'Adalah = ', divide)


    case _:
        print('Tidak Ada Operasi Yang Sesuai')