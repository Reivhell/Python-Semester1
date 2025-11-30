print('Program Membuat Daftar Harga Bahan Bakar')
print('========================================\n')

print('Menu Bahan Bakar Yang Tersedia : \n' \
'1.Bensin (Rp.4500/l) \n'
'2.Solar (Rp.5000/l) \n'
'3.Pertamax (Rp.7500/l) \n')

pilihan = int(input('Masukan Pilihan 1/2/3 : '))
liter = int(input('Masukan Jumlah Liter : '))
print()

harga = 0

if pilihan == 1:
    harga = 4500
elif pilihan == 2:
    harga = 5000
elif pilihan == 3:
    harga = 7500
else:
    print('Tidak Ada Di Menu')

total = 0

for i in range(liter):
    total = total + harga

print(f'Harga', harga, 'Untuk', liter, 'liter adalah Rp. ', total)