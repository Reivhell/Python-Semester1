print("===== Konversi Nilai Angka Ke Huruf ======")

nilai = float(input("Masukan Nilai Angka (0-100) : "))

if nilai >= 85:
    huruf = "A"
    ket = "Sangat Baik"
elif nilai >= 70:
    huruf = "B"
    ket = "Baik"
elif nilai >= 55:
    huruf = "C"
    ket = "Cukup"
elif nilai >= 40:
    huruf = "D"
    ket = "Kurang"
else:
    huruf = "E"
    ket = "Sangat Kurang"

    print(f"Nilai Angka : {nilai}")
    print(f"Nilai Huruf : {huruf}")
    print(f"Keterangan : {ket}")
