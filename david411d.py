print('Program Memeriksa Hari Dalam Bulan November 2025')
print('*************************************************\n')

tanggal = int(input('Masukkan Tanggal: '))

match tanggal:
    case 3 | 10 | 17 | 24:
        print('Hari Senin')
    case 4 | 11 | 18 | 25:
        print('Hari Selasa')
    case 5 | 12 | 19 | 26:
        print('Hari Rabu')
    case 6 | 13 | 20 | 27:
        print('Hari Kamis')
    case 7 | 14 | 21 | 28:
        print('Hari Jumat')
    case 1 | 8 | 15 | 29:
        print('Hari Sabtu')
    case 2 | 9 | 16 | 23 | 30:
        print('Hari Minggu')
    case _:
        print('Maaf, Tidak Ada Tanggal Tersebut')
