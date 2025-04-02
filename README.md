# PEWARNAAN GRAF
Pewarnaan graf merupakan pemetaan warna-warna pada unsur graf

##  Algoritma Pewarnaan Welch-Powell
Algoritma Pewarnaan Welch-Powell adalah algoritma untuk menyelesaikan masalah pewarnaan graf yang bertujuan untuk memberikan warna pada simpul-simpul dalam graf dengan jumlah warna minimum sehingga tidak ada dua simpul yang terhubung dengan sisi yang memiliki warna yang sama. Algoritma ini termasuk dalam kategori algoritma heuristik dan umumnya digunakan untuk graf yang tidak memiliki struktur khusus (misalnya, graf acak).

### Langkah-langkah dalam algoritma Welch-Powell:
1. Urutkan simpul berdasarkan derajatnya:

   Langkah pertama adalah mengurutkan semua simpul dalam graf berdasarkan derajatnya (jumlah sisi yang terhubung dengan simpul tersebut). Simpul dengan derajat tertinggi diurutkan terlebih dahulu.

2. Pewarnaan simpul:

   Setelah simpul diurutkan, algoritma mewarnai simpul satu per satu. Setiap simpul akan diberi warna yang pertama kali tersedia, yang berarti warna yang tidak digunakan oleh simpul-simpul yang sudah terhubung dengannya.

3. Pilih warna yang valid:

   Untuk setiap simpul, pilih warna yang tidak digunakan oleh tetangga-tetangganya yang sudah diberi warna. Jika semua warna yang ada telah digunakan oleh tetangga, tambahkan warna baru.

4. Lanjutkan ke simpul berikutnya:

   Proses ini diulang untuk setiap simpul dalam urutan yang telah ditentukan, sampai semua simpul memiliki warna.

### Ciri khas algoritma Welch-Powell:
a. Greedy: Algoritma ini bekerja secara greedy, yang berarti ia berusaha membuat pilihan yang optimal pada setiap langkah lokal dengan harapan menghasilkan solusi yang baik secara keseluruhan.

b. Heuristik: Algoritma ini memberikan solusi yang baik, tetapi tidak selalu solusi optimal dalam hal jumlah warna. Ini adalah solusi yang diharapkan cukup dekat dengan solusi optimal, tetapi bukan jaminan pasti.


## Cara Penggunaan 
1. Pastikan Anda telah menginstal Python di sistem Anda.
2. Klon repositori ini ke komputer Anda:
   ``` Bash
   https://github.com/periartaa/2.Diskrit-II.git
   ```
3. Jalankan Program Python
