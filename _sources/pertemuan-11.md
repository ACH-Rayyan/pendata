# Pertemuan 11

## Decision Tree

## 1. Pengertian Decision Tree

Decision Tree atau pohon keputusan merupakan salah satu metode klasifikasi yang digunakan untuk menentukan keputusan dengan cara memecah data berdasarkan atribut-atribut tertentu sampai diperoleh hasil akhir. Model ini memiliki bentuk seperti pohon yang tersusun dari node akar, cabang, serta node daun.

Dalam Decision Tree, setiap node berfungsi untuk menguji suatu atribut. Cabang menunjukkan kemungkinan hasil dari pengujian atribut tersebut, sedangkan leaf node atau daun menunjukkan keputusan akhir atau kelas yang diprediksi. Algoritma ini termasuk mudah dipahami karena alur pengambilan keputusannya dapat digambarkan secara visual.

Pada proyek ini, algoritma Decision Tree diterapkan untuk mengklasifikasikan dataset **Play Tennis**. Kolom yang menjadi target adalah `Play Tennis`, yaitu kolom yang menunjukkan apakah permainan tenis dapat dilakukan atau tidak berdasarkan kondisi cuaca yang tersedia.

## 2. Konsep Dasar Decision Tree

Decision Tree bekerja dengan membagi data menjadi beberapa kelompok berdasarkan atribut yang paling berpengaruh terhadap kelas target. Penentuan atribut terbaik dilakukan menggunakan ukuran kualitas tertentu, misalnya **Gini Index** atau **Gain Ratio**.

Dalam proyek ini, ukuran kualitas yang digunakan adalah **Gain Ratio**. Gain Ratio dipakai untuk memilih atribut paling tepat yang akan dijadikan pemisah utama atau root pada pohon keputusan.

### Rumus Gain Ratio

Gain Ratio diperoleh dengan membandingkan nilai **Information Gain** dengan **Split Information**. Rumusnya dapat dituliskan sebagai berikut:

```text
Gain Ratio(S, A) = Gain(S, A) / SplitInfo(S, A)
```

Sebelum menghitung Gain Ratio, perlu dihitung terlebih dahulu nilai **Entropy** dan **Information Gain**.

Rumus Entropy:

```text
Entropy(S) = - Σ pi log2(pi)
```

Rumus Information Gain:

```text
Gain(S, A) = Entropy(S) - Σ (|Sv| / |S|) x Entropy(Sv)
```

Rumus Split Information:

```text
SplitInfo(S, A) = - Σ (|Sv| / |S|) log2(|Sv| / |S|)
```

Keterangan:

- **S**: keseluruhan data yang digunakan.
- **A**: atribut yang diuji untuk memisahkan data.
- **Sv**: bagian data yang terbentuk berdasarkan nilai tertentu dari atribut A.
- **pi**: proporsi data pada kelas ke-i.
- **|Sv| / |S|**: rasio jumlah data pada subset terhadap jumlah seluruh data.

Atribut dengan nilai **Gain Ratio** paling tinggi akan dipilih sebagai atribut terbaik untuk membentuk percabangan pada Decision Tree.

## 3. Struktur Decision Tree

Komponen utama pada Decision Tree terdiri dari:

1. **Root Node**  
   Node awal atau akar dari pohon keputusan. Root node berisi atribut pertama yang digunakan untuk memisahkan data.

2. **Internal Node**  
   Node yang berada di bagian tengah pohon dan berfungsi untuk menguji atribut berikutnya.

3. **Branch**  
   Cabang yang menggambarkan hasil dari pengujian suatu atribut.

4. **Leaf Node**  
   Node terakhir yang menampilkan keputusan akhir atau kelas hasil prediksi.

## 4. Kelebihan Decision Tree

Beberapa keunggulan algoritma Decision Tree yaitu:

- Mudah dipahami serta mudah divisualisasikan.
- Dapat diterapkan pada data numerik maupun data kategorikal.
- Alur pengambilan keputusan dapat diamati dengan jelas.
- Tidak memerlukan proses normalisasi data.
- Sesuai digunakan untuk menjelaskan pola keputusan dari suatu dataset.

---

# TUGAS

## Laporan Proyek: Klasifikasi Decision Tree Menggunakan KNIME

## 5. Deskripsi Proyek

Proyek ini bertujuan membuat model klasifikasi dengan algoritma **Decision Tree** menggunakan platform **KNIME**. Dataset yang digunakan adalah dataset **Play Tennis**, yaitu dataset yang memuat beberapa kondisi cuaca untuk menentukan apakah seseorang dapat bermain tenis atau tidak.

Kolom target pada proyek ini adalah:

- `Play Tennis`

Kolom `Play Tennis` memiliki kelas keputusan, yaitu:

- `Yes`
- `No`

Tujuan dari proyek ini adalah membangun model Decision Tree yang dapat menghasilkan aturan keputusan berdasarkan data yang tersedia. Model tersebut kemudian ditampilkan dalam bentuk pohon agar proses pengambilan keputusan dapat diamati secara jelas.

## 6. Visualisasi Workflow

![Workflow Decision Tree](images/pertemuan11/01-workflow-decision-tree.png)

 Gambar 1. Workflow klasifikasi Decision Tree menggunakan KNIME.

---

# Langkah-Langkah Pembuatan Workflow

## 7. Membaca Data Menggunakan CSV Reader

**Node:** CSV Reader

**Fungsi:**  
Node CSV Reader berfungsi untuk memasukkan dataset dari file CSV ke dalam workspace KNIME. Dataset yang digunakan berisi data kondisi cuaca serta kolom target `Play Tennis`.

**Konfigurasi:**  
File dataset dipilih dari penyimpanan lokal komputer. Setelah proses pembacaan berhasil, data akan masuk ke KNIME dan siap digunakan pada tahap berikutnya.

---

## 8. Membagi Data Menggunakan Table Partitioner

**Node:** Table Partitioner

**Fungsi:**  
Node Table Partitioner digunakan untuk membagi dataset menjadi dua bagian. Pada workflow ini, pembagian data dilakukan sebelum data diteruskan ke node Decision Tree Learner.

**Konfigurasi:**

- First partition type: **Relative (%)**
- Relative size: **90**
- Sampling strategy: **Stratified**
- Group column: **Play Tennis**
- Fixed random seed: **0**

Dengan konfigurasi tersebut, **90% data** ditempatkan pada partisi pertama. Strategi sampling yang digunakan adalah **Stratified** dengan kolom `Play Tennis` sebagai group column. Strategi ini membuat pembagian data tetap mempertahankan proporsi kelas pada kolom target.

Penggunaan **Fixed random seed** bernilai 0 bertujuan agar hasil pembagian data tetap sama ketika workflow dijalankan kembali.

![Konfigurasi Table Partitioner](images/pertemuan11/02-table-partitioner.png)

Gambar 2. Konfigurasi Table Partitioner dengan pembagian data 90% dan sampling Stratified berdasarkan kolom `Play Tennis`.

---

## 9. Membuat Model Menggunakan Decision Tree Learner

**Node:** Decision Tree Learner

**Fungsi:**  
Node Decision Tree Learner digunakan untuk membentuk model klasifikasi Decision Tree dari data hasil Table Partitioner. Node ini mempelajari pola pada atribut-atribut dataset untuk memprediksi kelas pada kolom target.

**Konfigurasi:**

- Class column: **Play Tennis**
- Quality measure: **Gain ratio**
- Pruning method: **No pruning**
- Reduced error pruning: **Aktif**
- Minimum number of records per node: **2**
- Number of records to store for view: **10000**
- Average split point: **Aktif**
- Number threads: **12**
- Skip nominal columns without domain information: **Aktif**

Kolom `Play Tennis` dipilih sebagai class column karena kolom tersebut merupakan target prediksi. Quality measure yang digunakan adalah **Gain ratio**, sehingga atribut pada pohon keputusan dipilih berdasarkan nilai gain ratio terbaik.

Minimum number of records per node diatur menjadi 2. Artinya, sebuah node setidaknya harus memiliki 2 data agar dapat diproses. Pengaturan ini membantu menghasilkan pohon keputusan yang sederhana dan mudah dibaca.

![Konfigurasi Decision Tree Learner](images/pertemuan11/03-decision-tree-learner.png)

Gambar 3. Konfigurasi Decision Tree Learner dengan class column `Play Tennis`.

---

## 10. Menyimpan Model Menggunakan Model Writer

**Node:** Model Writer

**Fungsi:**  
Node Model Writer berfungsi untuk menyimpan model Decision Tree yang telah dibuat oleh node Decision Tree Learner. Melalui node ini, model dapat disimpan sehingga bisa digunakan kembali pada proses lain tanpa perlu melakukan pelatihan ulang.

**Konfigurasi:**  
Model Writer menerima input model dari output node Decision Tree Learner. Pada workflow ini, node tersebut digunakan sebagai media penyimpanan model hasil pelatihan.

---

## 11. Mengatur Tampilan Decision Tree Menggunakan Decision Tree View

**Node:** Decision Tree View

**Fungsi:**  
Node Decision Tree View digunakan untuk menampilkan model Decision Tree dalam bentuk visual pohon. Melalui tampilan ini, struktur keputusan yang dibentuk oleh model dapat dilihat secara langsung.

**Konfigurasi:**

- Title: **Decision Tree**
- Initial expanded levels: **2**
- Generate image: **Tidak aktif**

Judul visualisasi pohon diatur menjadi **Decision Tree**. Nilai Initial expanded levels diatur menjadi 2, sehingga dua level awal pada pohon keputusan akan terbuka saat ditampilkan.

![Konfigurasi Decision Tree View](images/pertemuan11/04-decision-tree-view-config.png)

Gambar 4. Konfigurasi Decision Tree View untuk menampilkan pohon keputusan.

---

## 12. Hasil Visualisasi Decision Tree

Output dari node Decision Tree View memperlihatkan bentuk pohon keputusan yang dihasilkan dari dataset Play Tennis. Pada hasil visualisasi tersebut, atribut **Outlook** menjadi node utama atau root node.

Dari root node **Outlook**, data dipisahkan ke dalam beberapa cabang, yaitu:

- `Sunny`
- `Overcast`
- `Rain`

Pada cabang `Sunny`, keputusan masih dilanjutkan dengan melihat atribut **Humidity**. Jika nilai Humidity adalah `High`, maka keputusan akhirnya adalah `No`. Jika nilai Humidity adalah `Normal`, maka keputusan akhirnya adalah `Yes`.

Pada cabang `Overcast`, hasil keputusan yang diperoleh adalah `Yes`. Sementara itu, pada cabang `Rain`, keputusan yang paling dominan juga mengarah ke `Yes`.

![Hasil Decision Tree](images/pertemuan11/05-decision-tree-result.png)

Gambar 5. Hasil visualisasi pohon keputusan pada dataset Play Tennis.

---

# 13. Hasil dan Pembahasan

Berdasarkan workflow yang telah dibuat, proses klasifikasi dengan algoritma Decision Tree berhasil dijalankan pada KNIME. Tahapan dimulai dari membaca dataset menggunakan node CSV Reader, kemudian data dibagi menggunakan node Table Partitioner.

Pada proyek ini, Table Partitioner menerapkan pembagian data sebesar **90%** dengan strategi **Stratified** berdasarkan kolom `Play Tennis`. Strategi tersebut membuat distribusi kelas `Yes` dan `No` tetap diperhatikan dalam proses pembagian data.

Model Decision Tree dibangun menggunakan node Decision Tree Learner. Kolom `Play Tennis` digunakan sebagai class column karena kolom tersebut menjadi target klasifikasi. Quality measure yang digunakan adalah **Gain ratio**, sehingga pemilihan atribut sebagai pemisah dilakukan berdasarkan nilai gain ratio.

Hasil visualisasi Decision Tree menunjukkan bahwa atribut **Outlook** menjadi root node atau node utama. Atribut ini menjadi dasar awal dalam proses pengambilan keputusan. Jika Outlook bernilai `Sunny`, model akan memeriksa atribut **Humidity** untuk menentukan hasil akhir. Jika Outlook bernilai `Overcast`, keputusan langsung menuju `Yes`. Jika Outlook bernilai `Rain`, keputusan mayoritas juga menuju `Yes`.

Berdasarkan hasil tersebut, dapat disimpulkan bahwa model Decision Tree mampu membentuk aturan keputusan yang mudah dipahami. Visualisasi pohon membantu pengguna memahami cara model menghasilkan klasifikasi berdasarkan atribut yang tersedia.

---

# 14. Kesimpulan

Berdasarkan proyek yang telah dilakukan, algoritma **Decision Tree** dapat digunakan untuk melakukan klasifikasi pada dataset **Play Tennis** melalui platform **KNIME**. Workflow yang dibuat mencakup beberapa tahap, yaitu membaca data, membagi data, membangun model Decision Tree, menyimpan model, serta menampilkan hasil pohon keputusan.

Node Decision Tree Learner berhasil menghasilkan model dengan kolom target `Play Tennis`. Hasil pohon keputusan menunjukkan bahwa atribut `Outlook` menjadi faktor utama dalam proses klasifikasi. Selanjutnya, atribut lain seperti `Humidity` digunakan untuk memperjelas keputusan pada cabang tertentu.

Secara keseluruhan, Decision Tree merupakan algoritma yang mudah dipahami karena model yang dihasilkan dapat divisualisasikan dalam bentuk pohon keputusan. Dengan demikian, pengguna dapat melihat aturan klasifikasi yang terbentuk dari data secara lebih jelas.
