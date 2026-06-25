print("==== Loket Tiket Bioskop =====")

harga_normal = 50000
umur = int(input("Masukan Umur : "))
pelajar = input("Apakah Pelajar (Y/T) : ").upper()

if umur < 12 or umur > 60:
    diskon = 0.5
    ket = "Diskon Anak/Lansia (50%)"
elif pelajar == "Y":
    diskon = 0.2
    ket = "Diskon Pelajar (20%)"
else:
    diskon = 0
    ket = "Harga Normal"

potongan = harga_normal * diskon
bayar = harga_normal - potongan

print("-" * 35)
print(f"Harga Normal : Rp {harga_normal:,}")
print(f"Keterangan : {ket}")
print(f"Potongan : Rp {int(potongan):,}")
print(f"Total Bayar : Rp {int(bayar):,}")
