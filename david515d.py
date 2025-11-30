print('Program Membalik Kata Dari Belakang')
print('===================================\n')

kata = input('Masukan Kata Yang Ingin DiBalik : ')

balik = ''

for i in kata:
    balik = i + balik
    
print('Hasilnya :', balik)