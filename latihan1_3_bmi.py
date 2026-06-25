print('====== Kalkulator BMI =======')

berat = float(input('Masukan Berat Badan (kg) : '))
tinggi = float(input('Masukan Tinggi Badan (m) :  '))

bmi = berat / (tinggi ** 2)

if bmi < 18.5:
    kategori = 'Kurus'
elif bmi < 25:
    kategori = 'Normal'
elif bmi < 30:
    kategori = 'Gemuk'
else:
    kategori  = 'Obesitas'

print('-' * 30)
print(f'Nilai BMI Anda : {bmi :.2f}')
print(f'Kategori : {kategori}')