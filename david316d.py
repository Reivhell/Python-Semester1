print('Program Menghitung Gaji Karyawan')
print('********************************\n')

nama = input('Masukan Nama Anda: ')
nik = int(input('Masukan Nik Anda: '))

masaKerja = int(input('Masukan Lama Masa Kerja: '))
statusHub = input('Apakah Sudah Berkeluarga (Sudah Menikah/Belum Menikah) : ')
statusKaryawan = input('Apakah Pegawai Tetap (Tetap/Kontrak) : ')
gajiPokok = int(input('Masukan Gaji Pokok: '))

bonus = 0
tunjangan = 0
uangTransport = 0

if masaKerja > 5:
    bonus = 0.15 * gajiPokok
    print('Selamat Anda Mendapatkan Bonus Sebesar : Rp. ', bonus)
else:
    print('Anda Tidak Mendapatkan Bonus')

if statusHub.lower() == "sudah menikah":
    tunjangan = 0.1 * gajiPokok
    print('Anda Mendapatkan Tunjangan Sebesar: Rp. ', tunjangan)
else:
    print('Anda Tidak Mendapat Tunjangan')

if statusKaryawan.lower() == "tetap":
    uangTransport = 50000
    print('Anda Mendapatkan Uang Transport Sebesar: Rp. ', uangTransport)
else:
    print('Anda Tidak Mendapatkan Uang Transport')

gajiBersih = gajiPokok + bonus + tunjangan + uangTransport

print('\n========= Rincian Gaji Karyawan =============')
print(f'Nama Karyawan        : {nama}')
print(f'Nik Karyawan         : {nik}')
print(f'Masa Kerja Anda      : {masaKerja} Tahun')
print(f'Status Hubungan      : {statusHub}')
print(f'Status Karyawan      : {statusKaryawan}')
print(f'Gaji Pokok           : Rp. {gajiPokok}')
print(f'Gaji Bersih          : Rp. {gajiBersih}')

