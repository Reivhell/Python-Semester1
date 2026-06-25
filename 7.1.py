print("====== Program Menghitung Huruf Hidup ======")
print()

kalimat = input("Masukan Kalimat : ").lower()

kata = kalimat.strip()
huruf = kata.split()

huruf_hidup = ["a", "i", "u", "e", "o"]

for each in huruf:
    jumlah = 0

    for huruf in each:
        if huruf in huruf_hidup:
            jumlah += 1

    print("Kata : ", each)
    print("Jumlah Huruf Hidup : ", jumlah)
