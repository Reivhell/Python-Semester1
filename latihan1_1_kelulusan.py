print("===== Program Cek Kelulusan =====")

nama = input("Masukan Nama Mahasiswa : ")
nilai = float(input("Masukan Nilai Akhir : "))

if nilai >= 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print("-" * 35)
print(f"Nama : {nama}")
print(f"Nilai : {nilai}")
print(f"Status : {status}")
