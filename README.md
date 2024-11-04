# Diagonal Magic Cube Project

## Deskripsi Singkat
Diagonal magic cube adalah kubus yang tersusun dari angka 1 hingga n^3 tanpa pengulangan, dengan n sebagai panjang sisi kubus tersebut. Angka-angka dalam kubus diatur sedemikian rupa agar memenuhi properti-properti berikut:
- Terdapat satu angka yang merupakan magic number dari kubus (magic number tidak harus termasuk dalam rentang 1 hingga n^3 dan bukan bagian dari angka yang dimasukkan ke dalam kubus).
- Jumlah angka-angka untuk setiap baris sama dengan magic number.
- Jumlah angka-angka untuk setiap kolom sama dengan magic number.
- Jumlah angka-angka untuk setiap tiang sama dengan magic number.
- Jumlah angka-angka untuk seluruh diagonal ruang pada kubus sama dengan magic number.
- Jumlah angka-angka untuk seluruh diagonal pada potongan bidang kubus sama dengan magic number.

Tim kami sebagai pengembang telah mengembangkan enam algoritma untuk menyelesaikan masalah diagonal magic cube ini:
1. Steepest Ascent
2. Stochastic
3. Random Restart
4. Sideways Move
5. Genetic Algorithm
6. Simulated Annealing

Dari eksperimen yang dilakukan, algoritma Steepest Ascent terbukti menjadi yang terbaik dalam hal konsistensi, ketepatan, dan durasi eksekusi.

Proyek ini dikembangkan menggunakan bahasa Python, dengan matplotlib untuk visualisasi dan numpy sebagai library perhitungan.

## Cara Setup dan Menjalankan Program
1. Clone repository ini ke dalam komputer Anda:
   ```bash
   git clone https://github.com/NovaRoomsid/Guesthouse_BE.git
   ```
2. Navigasikan ke folder `src`:
   ```bash
   cd src
   ```
3. Jalankan program utama:
   ```bash
   python main.py
   ```
4. Program akan menampilkan CLI untuk memilih algoritma yang digunakan dalam menyelesaikan masalah diagonal magic cube 5x5x5.

## Dokumentasi
Di dalam folder `doc`, terdapat dokumentasi yang menjelaskan detail dari setiap algoritma, hasil eksperimen, dan analisis yang telah dilakukan. Dokumentasi ini mencakup pembahasan mengenai hipotesis, hasil eksperimen yang mendukung atau menentang hipotesis tersebut, serta algoritma yang dianggap terbaik oleh penulis.

## Pembagian Tugas
| Name          | Student Number | Task                          |
|---------------|----------------|--------------------------------|
| Wilson Yusda  | 13522019       | Genetic Algorithm              |
| Filbert       | 13522021       | Simulated Annealing            |
| Elbert Chailes| 13522045       | Steepest Ascent Hill Climbing, Sideways Move Hill Climbing |
| Benardo       | 13522055       | Random Restart Hill Climbing, Stochastic Hill Climbing      |

Silakan isi tabel pembagian tugas ini sesuai dengan anggota kelompok Anda.

