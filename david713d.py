def A_pangkat_N_positif(A,N):
    hasil = A**N
    return hasil

def pangkatPositf(A,N):
    hasil = A_pangkat_N_positif(A,N)
    return hasil

def pangkatNegatif(A,N):
    return A_pangkat_N_positif(A,N)

def masukanData():
    A = float(input('Masukan Nilai A : '))
    N = float(input('Masukan Nilai N : '))

    if N < 0:
        print('A pangkat N (Negatif) = ', pangkatNegatif(A, N))
    else:
        print('A pangkat N = ', pangkatPositf(A, N))

print('Menghitung A pangkat N dengan A rill & N integer')
print('A dan N boleh bilangan negatif')
print(' ++++++++++++++++++++++++++++ ')
print()

masukanData()
