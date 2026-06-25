print("Masukan 10 Bilangan Bulat")
bilangan = []

for i in range(10):
    angka = int(input(f"Masukan Bilangann Ke-{i + 1} : "))
    bilangan.append(angka)
    if angka is float:
        print("Angka Tidak Valid")
        break

rata = sum(bilangan) / len(bilangan)

print("Tampilan Semua Bilangan Di List : ")
print(bilangan)
print()
print(f"Nilai Terkecil : {min(bilangan)}")
print(f"Nilai Terbesar : {max(bilangan)}")
print(f"Jumlah Seluruh Bilangan : {sum(bilangan)}")
print(f"Nilai Rata-rata : {rata}")
