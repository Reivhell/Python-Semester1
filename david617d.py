print('MENGHITUNG JUMLAH & RATA-RATA SEJUMLAH DATA NILAI')
print('CACAH DATA TIDAK DIKETAHUI DENGAN PASTI')
print("PEMBACAAN DATA DIHENTIKAN DENGAN DATA SENTINEL")
print("DATA SENTINEL BERUPA SEMBARANG BILANGAN NEGATIF")
print("\n")

total = 0
jumlah = 0

while True:
    data = int(input("Masukan Data Nilainya : "))
    
    if data < 0:
        break

    total = total + data
    jumlah = jumlah + 1

    
if total > 0:
    rata_rata = total / jumlah
    print()
    print("JUMLAH DATA     = ", total)
    print("NILAI RATA-RATA = ", rata_rata)
else:
    print('TIDAK ADA DATA')