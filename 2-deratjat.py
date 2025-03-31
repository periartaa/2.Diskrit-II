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

# Fungsi untuk mengecek apakah matriks simetris (graf tidak berarah)
def is_symmetric(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:  # Bandingkan elemen dengan transposenya
                return False
    return True

# Fungsi untuk menghitung derajat vertex
def hitung_derajat(matrix, n, berarah):
    if berarah:
        in_degree = np.sum(matrix, axis=0)  # Jumlah kolom (derajat masuk)
        out_degree = np.sum(matrix, axis=1) # Jumlah baris (derajat keluar)
        for i in range(n):
            print(f"Vertex {i+1}: In-degree = {in_degree[i]}, Out-degree = {out_degree[i]}")
    else:
        degree = np.sum(matrix, axis=1)  # Jumlah baris (karena simetris, baris dan kolom sama)
        for i in range(n):
            print(f"Vertex {i+1}: Degree = {degree[i]}")

# Meminta jumlah baris dan kolom dari pengguna
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Memasukkan matriks dari pengguna
matriks = masukkan_matriks(baris, kolom)

# Jika input valid, tampilkan matriks dan cek jenis graf
if matriks is not None:
    print("\nMatriks yang Anda masukkan:")
    print(matriks)

    # Cek apakah graf berarah atau tidak
    if is_symmetric(matriks, baris):
        print("\nGraf adalah GRAF TIDAK BERARAH.")
        hitung_derajat(matriks, baris, berarah=False)
    else:
        print("\nGraf adalah GRAF BERARAH.")
        hitung_derajat(matriks, baris, berarah=True)