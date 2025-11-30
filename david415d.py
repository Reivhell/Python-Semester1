print('Toko Segar Manis')
print('==================================\n')

print('Menu Buah Yang Tersedia')
print('=======================')
print('=======================> 1.Kiwi =')
print('                         2.Mangga =')
print('                         3.Alpukat =')
print('                         4.Apel =')
print('====================================')

buah = int(input('Pilih Menu = '))
print()

k = 13000
m = 10000
al = 14000
a = 12000


match buah:
    case 1:
        kg = int(input('Input Jumlah Kg = '))
        if kg > 20:
            harga = kg * k
            diskon = (0.05 + 0.07) * harga
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 5% + 7% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
        elif kg > 5:
            harga = kg * k
            diskon = harga * 0.05
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 5% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
        else:
            harga = kg * k
            print('=================================')
            print('Jumlah yang dibayar = ', harga)
            print('=================================')


    case 2:
        kg = int(input('Input Jumlah Kg = '))
        if kg > 20:
            harga = kg * m
            diskon = (0.025 + 0.07) * harga
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 2.5% + 7% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
        elif kg > 5:
            harga = kg * m
            diskon = harga * 0.025
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 2.5% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
        else:
            harga = kg * m
            print('=================================')
            print('Jumlah yang dibayar = ', harga)
            print('=================================')

    case 3:
        kg = int(input('Input Jumlah Kg = '))
        if kg > 10:
            harga = kg * al
            diskon = 0.07 * harga
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 7% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
        elif kg > 5:
            harga = kg * al
            diskon = 0.07 * harga
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 0.07% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
        else:
            harga = kg * al
            print('=================================')
            print('Jumlah yang dibayar = ', harga)
            print('=================================')

    case 4:
        kg = int(input('Input Jumlah Kg = '))
        if kg > 15:
            harga = kg * a
            diskon = 0.10 * harga
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 10% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
            print('SELAMAT ANDA MENDAPATKAN HADIAH TAS !!!!')
        elif kg > 5:
            harga = kg * a
            diskon = harga * 0.10
            total = harga - diskon
            print('Harga Sebelum Diskon = ', harga)
            print('Potongan Harga 0.10% = ', diskon)
            print('=================================')
            print('Jumlah yang dibayar = ', total)
            print('=================================')
            
        else:
            print('=================================')
            print('*>*')
            print('=================================')
    
    case _:
        print('Pilihan Menu Tidak Ada')