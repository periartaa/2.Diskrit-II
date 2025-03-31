import numpy as np

# Fungsi untuk memasukkan matriks dari pengguna
def masukkan_matriks(baris, kolom):
    matriks = []
    print(f"Masukkan elemen matriks {baris}x{kolom}:")
    for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            elemen = int(input(f"Elemen [{i+1},{j+1}]: "))  # Memasukkan angka dari pengguna
            baris_matriks.append(elemen)
        matriks.append(baris_matriks)
    return np.array(matriks)

# Meminta jumlah baris dan kolom dari pengguna
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Memasukkan matriks dari pengguna
matriks = masukkan_matriks(baris, kolom)

# Menampilkan matriks yang dimasukkan
print("\nMatriks yang Anda masukkan:")
print(matriks)