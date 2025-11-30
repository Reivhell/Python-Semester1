print('Program Hitung')
print('==============\n')

b1 = int(input('Masukan Bilangan Pertama : '))
b2 = int(input('Masukan Bilangan Kedua : '))

hasil = 0 

for i in range(b1):
    hasil = hasil + b2

b2 = b2 - 1

for i in range(b2):
    print(b1, ' + ', end=' ')

print(b1, ' = ', hasil)