print("Program Menentukan Bilangan yang Terbesar")
print("-----------------------------------------")

a = int(input('Masukan Bilangan  Pertama: '))
b = int(input('Masukan Bilangan  Kedua: '))
c = int(input('Masukan Bilangan  Ketiga: '))

if (a > b) and (a > c):
    print('Bilangan Pertama Adalah yang terbesar')
elif (b > a) and (b > c):
    print("Bilangan Kedua Adalah yang terbesar")
elif (c > a) and (c > b):
    print('Bilangan Ketiga Adalah yang terbesar') 
else:
    print('Ada dua atau tiga masukan yang sama besar')