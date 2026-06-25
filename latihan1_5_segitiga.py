print("====== Penentu Jenis Segitiga ======")

a = float(input("Masukan Sisi a : "))
b = float(input("Masukan Sisi b : "))
c = float(input("Masukan Sisi c : "))

# Validasi Segitiga

if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print("Ketiga Sisi Segitiga Tidak Membentuk Segitiga")
else:
    if a == b == c:
        jenis = "Segitiga Sama Sisi"
    elif a == b or b == c or c == a:
        jenis = "Segitiga Sama Kaki"
    else:
        jenis = "Segitiga Sembarang"

print("-" * 30)
print(f"Jenis Segitiga : {jenis}")
