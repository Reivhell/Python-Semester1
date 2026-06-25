kalimat = input("Masukan Sebuah Kalimat : ")

print("\== Hasil Analisa ====")
print("Jumlah Karakter : ", len(kalimat))
print("Huruf Pertama : ", kalimat[0])
print("Huruf Terakhir : ", kalimat[-3])
print("5 Karakter Huruf Pertama : ", kalimat[:5])
print("5 Karakter Terahir : ", kalimat[-5:])

if "Python" in kalimat:
    print("Kalimat Mengandung Kata Python")
else:
    print("Kalimat Tidak Mengandung Kata Pyhton")
