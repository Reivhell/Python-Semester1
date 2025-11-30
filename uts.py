print('Program Menghitung Gaji Karyawan')
print('================================\n')

#Section Input

nama = input('Masukan Nama Karyawan : ')
nik = int(input('Masukan Nik Karyawan : '))
masaKerja = int(input('Lama Masa Kerja : '))

#Format 
statusKaryawan = input('Karyawan Tetap / Kontrak : ')
statusHub = input('Status Hubungan Sudah Menikah/Belum Menikah : ')
gajiPokok = int(input('Masukan Gaji Pokok : '))

if masaKerja > 5:
    bonus = 0.15 * gajiPokok
else:
    bonus = 0
if statusKaryawan.capitalize == 'Tetap':
    uangTransport = 50000
else:
    uangTransport = 0
if statusHub.capitalize == 'Sudah menikah':
    tunjangan = 0.10 * gajiPokok
else:
    tunjangan = 0

gajiBersih = (gajiPokok + bonus + uangTransport + tunjangan)

print()
print('----------------------- Rincian Gaji Karyawan -----------------------')
print('=====================================================================')
print