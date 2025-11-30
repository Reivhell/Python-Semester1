import random

print('Program Angka Acak')
print('*' * 30)
print()

b = "N"

while (b == 'N'):
    angkaAcak = (random.randrange(1000))
    print('Angka Sekarang : ', angkaAcak)
    print()
    print('Tekan Sembarang Tombol Untuk Mengacak')
    print('Tekan [Y] Untuk Berhenti')
    print()

    x = input()

    if x == 'Y':
        break

    print('Pengacakan Berhenti')