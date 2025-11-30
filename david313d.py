print('Program Seleksi Bilangan Ganjil Atau Genap')
print('-------------------------------------------\n')

bil  = int(input('Masukan Bilangan : '))
print("\n")

if bil % 2 == 1:
    print(bil, 'Adalah Bilangan Ganjil')
else:
    print(bil, 'Adalah Bilangan Genap')