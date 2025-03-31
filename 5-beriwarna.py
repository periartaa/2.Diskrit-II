import numpy as np

def masukkan_matriks(baris, kolom):
    """
    Fungsi untuk memasukkan elemen matriks dari pengguna.
    :param baris: Jumlah baris pada matriks
    :param kolom: Jumlah kolom pada matriks
    :return: Matriks dalam bentuk array NumPy
    """
    matriks = []
    print(f"Masukkan elemen matriks {baris}x{kolom}:")
    for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            elemen = int(input(f"Elemen [{i+1},{j+1}]: "))  # Meminta input elemen dari pengguna
            baris_matriks.append(elemen)
        matriks.append(baris_matriks)
    return np.array(matriks)

def is_symmetric(matrix, n):
    """
    Fungsi untuk memeriksa apakah matriks adalah matriks simetris (graf tidak berarah).
    :param matrix: Matriks adjacency
    :param n: Ukuran matriks (jumlah vertex)
    :return: True jika matriks simetris, False jika tidak
    """
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def hitung_derajat(matrix, n):
    """
    Fungsi untuk menghitung derajat setiap vertex dalam graf.
    :param matrix: Matriks adjacency
    :param n: Jumlah vertex
    :return: Daftar tuple (vertex, derajat) yang diurutkan dari terbesar ke terkecil
    """
    degree = np.sum(matrix, axis=1)  # Menghitung jumlah setiap baris sebagai derajat
    degrees = [(i + 1, degree[i]) for i in range(n)]
    degrees.sort(key=lambda x: x[1], reverse=True)  # Mengurutkan berdasarkan derajat (descending)
    return degrees

def pewarnaan_welch_powell(matrix, n):
    """
    Algoritma pewarnaan graf Welch-Powell untuk pewarnaan vertex.
    :param matrix: Matriks adjacency
    :param n: Jumlah vertex
    """
    derajat = hitung_derajat(matrix, n)
    print("\nDerajat setiap vertex:")
    for vertex, deg in derajat:
        print(f"Vertex {vertex}: Degree = {deg}")
    
    warna = [-1] * n  # Inisialisasi array warna dengan -1 (belum diwarnai)
    warna_tersedia = 0  # Indeks warna dimulai dari 0
    
    for i, _ in derajat:
        if warna[i - 1] == -1:  # Jika vertex belum diwarnai
            warna_tersedia += 1  # Gunakan warna baru
            warna[i - 1] = warna_tersedia
            
            # Tandai semua simpul yang tidak bertetangga dengannya
            for j, _ in derajat:
                if warna[j - 1] == -1 and all(matrix[j - 1][k] == 0 or warna[k] != warna_tersedia for k in range(n)):
                    warna[j - 1] = warna_tersedia
    
    print("\nPewarnaan vertex:")
    for vertex, _ in derajat:
        print(f"Vertex {vertex} diberi warna {warna[vertex - 1]}")

def main():
    """
    Fungsi utama program untuk menerima input, memproses graf, dan menerapkan algoritma pewarnaan jika memungkinkan.
    """
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    matriks = masukkan_matriks(baris, kolom)
    
    print("\nMatriks yang Anda masukkan:")
    print(matriks)
    
    if is_symmetric(matriks, baris):
        print("\nGraf adalah GRAF TIDAK BERARAH.")
        pewarnaan_welch_powell(matriks, baris)  # Jalankan pewarnaan jika graf tidak berarah
    else:
        print("\nGraf adalah GRAF BERARAH. Pewarnaan hanya untuk graf tidak berarah.")

if __name__ == "__main__":
    main()
