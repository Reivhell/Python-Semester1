def Hitung_panjang(nama):
    n = len(nama)
    print(n, 'Karakter')

print()
print('Program Hitung Huruf Nama')
print('+++++++++++++++++++++++++')
print()

nama = input('Siapakah Nama Lengkap Anda : ')
print('Panjang nama anda adalah : ', end='')
Hitung_panjang(nama)
print('Catatan :')
print('Spasi dalam nama dianggap Satu Karakter')
