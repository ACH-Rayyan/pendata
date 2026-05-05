# Pertemuan 10

## 1. Pengertian Naive Bayes

Naive Bayes merupakan metode klasifikasi yang bekerja berdasarkan konsep probabilitas dengan memanfaatkan Teorema Bayes. Algoritma ini disebut "Naive" karena menganggap setiap fitur atau atribut pada data berdiri sendiri dan tidak saling bergantung. Meskipun pada kenyataannya antarfitur dalam sebuah dataset bisa saja memiliki keterkaitan, Naive Bayes tetap sering digunakan karena cara kerjanya sederhana, prosesnya cepat, dan mampu memberikan hasil yang cukup baik untuk berbagai permasalahan klasifikasi.

Pada proyek ini digunakan jenis **Gaussian Naive Bayes**. Metode ini sesuai untuk dataset IRIS karena atribut yang digunakan berupa data numerik kontinu, seperti panjang sepal, lebar sepal, panjang petal, dan lebar petal.

## 2. Rumus Teorema Bayes

Rumus dasar Teorema Bayes adalah sebagai berikut:

```text
P(C|X) = (P(X|C) x P(C)) / P(X)
```

Keterangan:

- **P(C|X)**: peluang data termasuk ke kelas C berdasarkan atribut X.
- **P(X|C)**: peluang atribut X muncul apabila kelasnya diketahui sebagai C.
- **P(C)**: peluang awal dari kemunculan kelas C.
- **P(X)**: peluang munculnya atribut X.

## 3. Jenis-Jenis Naive Bayes

Beberapa jenis Naive Bayes yang umum digunakan adalah sebagai berikut:

1. **Gaussian Naive Bayes**  
   Digunakan pada data numerik yang bersifat kontinu. Contohnya terdapat pada dataset IRIS yang memiliki atribut `sepal_length`, `sepal_width`, `petal_length`, dan `petal_width`.

2. **Multinomial Naive Bayes**  
   Digunakan untuk data yang berbentuk jumlah atau frekuensi, misalnya pada klasifikasi teks berdasarkan banyaknya kemunculan kata.

3. **Bernoulli Naive Bayes**  
   Digunakan untuk data biner, yaitu data yang hanya memiliki dua kemungkinan nilai, seperti ya/tidak atau 0/1.

## 4. Kelebihan Naive Bayes

Beberapa kelebihan dari algoritma Naive Bayes adalah:

- Memiliki proses komputasi yang cepat dan efisien.
- Mudah diterapkan untuk proses klasifikasi data.
- Dapat digunakan pada dataset sederhana maupun dataset dengan jumlah atribut yang cukup banyak.
- Tidak memerlukan data latih dalam jumlah yang sangat besar untuk memperoleh hasil yang cukup baik.
- Mudah diimplementasikan menggunakan library Python, salah satunya scikit-learn.

---

# TUGAS

## Laporan Proyek: Klasifikasi Naive Bayes Menggunakan KNIME dan Python (Sklearn)

## 5. Deskripsi Proyek

Proyek ini dibuat untuk membangun model klasifikasi menggunakan algoritma **Gaussian Naive Bayes** dari library **scikit-learn Python** yang dijalankan melalui platform **KNIME**. Dataset yang digunakan adalah dataset **IRIS**, yaitu dataset yang berisi data ukuran bunga Iris.

Dataset IRIS memiliki beberapa atribut numerik, yaitu:

- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`

Selain atribut tersebut, dataset ini juga memiliki kolom target atau label, yaitu:

- `species`

Kolom `species` berisi jenis bunga Iris, antara lain:

- `Iris-setosa`
- `Iris-versicolor`
- `Iris-virginica`

Tujuan dari proyek ini adalah membuat model klasifikasi yang dapat memprediksi jenis bunga Iris berdasarkan nilai atribut sepal dan petal. Pembuatan model dilakukan dengan menggabungkan workflow visual pada KNIME dan pemrograman Python melalui node **Python Script**.

## 6. Visualisasi Workflow

![Workflow KNIME](images/pertemuan10/01-workflow-knime.png)

> Gambar 1. Workflow klasifikasi Naive Bayes menggunakan KNIME dan Python Script.

---

# Langkah-Langkah Pembuatan Workflow

## 7. Membaca Data Menggunakan CSV Reader

**Node:** CSV Reader

**Fungsi:**  
Node CSV Reader digunakan untuk memasukkan dataset IRIS dari file CSV ke dalam lingkungan kerja KNIME. File tersebut berisi data bunga Iris yang terdiri dari beberapa fitur numerik dan satu kolom target.

**Konfigurasi:**  
Pada node CSV Reader, file dataset dipilih dari penyimpanan lokal komputer. Setelah file berhasil dibaca, data akan tersedia di KNIME dan dapat digunakan untuk tahapan berikutnya.

---

## 8. Membagi Data Latih dan Data Uji Menggunakan Table Partitioner

**Node:** Table Partitioner

**Fungsi:**  
Node Table Partitioner digunakan untuk membagi dataset menjadi dua bagian, yaitu data latih dan data uji. Data latih digunakan dalam proses pelatihan model, sedangkan data uji digunakan untuk mengetahui kemampuan model dalam melakukan prediksi.

**Konfigurasi:**

- Partition type: **Relative (%)**
- Relative size: **60**
- Sampling strategy: **Random**

Dengan konfigurasi tersebut, **60% data** digunakan sebagai data latih, sedangkan **40% data** digunakan sebagai data uji. Strategi **Random** membuat pembagian data dilakukan secara acak.

Pembagian data ini diperlukan agar model tidak hanya mengingat data latih, tetapi juga dapat diuji menggunakan data lain yang belum digunakan saat proses pelatihan.

![Konfigurasi Table Partitioner](images/pertemuan10/02-table-partitioner.png)

> Gambar 2. Konfigurasi Table Partitioner dengan pembagian 60% data latih dan 40% data uji.

---

## 9. Normalisasi Data Latih Menggunakan Normalizer

**Node:** Normalizer

**Fungsi:**  
Node Normalizer digunakan untuk menyamakan skala nilai pada fitur numerik agar berada pada rentang yang seragam. Proses ini dilakukan supaya fitur yang memiliki nilai lebih besar tidak terlalu memengaruhi proses pembelajaran model.

**Kolom yang dinormalisasi:**

- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`

**Konfigurasi:**  
Pada proyek ini, kolom numerik dipilih secara manual pada bagian **Includes**. Normalisasi dilakukan ke dalam rentang nilai **0 sampai 1**. Output dari node ini berupa data latih yang telah dinormalisasi serta model normalisasi yang menyimpan informasi skala dari data latih.

![Konfigurasi Normalizer](images/pertemuan10/03-normalizer.png)

> Gambar 3. Konfigurasi Normalizer pada kolom numerik dataset IRIS.

---

## 10. Menerapkan Normalisasi ke Data Uji Menggunakan Normalizer Apply

**Node:** Normalizer (Apply)

**Fungsi:**  
Node Normalizer Apply digunakan untuk menerapkan aturan normalisasi dari data latih ke data uji. Dengan proses ini, data uji akan memiliki skala nilai yang sama dengan data latih.

**Konfigurasi:**  
Node ini menerima dua input, yaitu:

1. Model normalisasi dari node **Normalizer**.
2. Data uji dari hasil pembagian node **Table Partitioner**.

Penggunaan Normalizer Apply penting karena dapat menghindari terjadinya **data leakage**. Data leakage terjadi ketika informasi dari data uji ikut memengaruhi proses pelatihan model. Dengan menggunakan model normalisasi yang berasal dari data latih, proses evaluasi menjadi lebih tepat.

---

## 11. Implementasi Naive Bayes Menggunakan Python Script

**Node:** Python Script

**Fungsi:**  
Node Python Script digunakan untuk menjalankan kode Python di dalam KNIME. Pada bagian ini, algoritma **Gaussian Naive Bayes** digunakan untuk melatih model dan menghasilkan prediksi pada data uji.

**Proses yang dilakukan:**

1. Membaca data training dan testing dari input KNIME.
2. Memisahkan kolom fitur dan kolom label/target.
3. Membuat model Gaussian Naive Bayes.
4. Melatih model menggunakan data latih.
5. Melakukan prediksi terhadap data uji.
6. Menambahkan hasil prediksi ke dalam kolom baru bernama `hasil_prediksi`.
7. Mengirim hasil akhir kembali ke KNIME.
8. Menampilkan laporan evaluasi klasifikasi menggunakan `classification_report`.

### Script yang Digunakan

```python
import knime.scripting.io as knio
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# Membaca data training dan testing dari input KNIME
data_latih = knio.input_tables[0].to_pandas()
data_uji = knio.input_tables[1].to_pandas()

# Memisahkan kolom fitur dan kolom label/target
fitur_latih = data_latih.iloc[:, :-1]
label_latih = data_latih.iloc[:, -1]

fitur_uji = data_uji.iloc[:, :-1]
label_uji = data_uji.iloc[:, -1]

# Membuat dan melatih model Naive Bayes Gaussian
model_nb = GaussianNB()
model_nb.fit(fitur_latih, label_latih)

# Melakukan prediksi terhadap data uji
hasil_prediksi = model_nb.predict(fitur_uji)

# Menambahkan hasil prediksi ke dalam data uji
hasil_akhir = data_uji.copy()
hasil_akhir["hasil_prediksi"] = hasil_prediksi

# Mengirim hasil akhir kembali ke KNIME
knio.output_tables[0] = knio.Table.from_pandas(hasil_akhir)

# Menampilkan laporan evaluasi klasifikasi
print(classification_report(label_uji, hasil_prediksi))
```

### Penjelasan Script

Pada script tersebut, data latih dan data uji diambil dari input node Python Script menggunakan `knio.input_tables`. Setelah itu, data diubah menjadi dataframe pandas agar dapat diproses menggunakan library Python.

Tahap berikutnya adalah memisahkan data menjadi fitur dan label. Fitur diambil dari seluruh kolom kecuali kolom terakhir, sedangkan label diambil dari kolom terakhir. Pada dataset ini, kolom label yang digunakan adalah `species`.

Model dibuat menggunakan `GaussianNB()` dari library `sklearn.naive_bayes`. Setelah model selesai dilatih menggunakan data latih, model tersebut digunakan untuk memprediksi data uji. Hasil prediksi kemudian ditambahkan ke dataframe data uji sebagai kolom baru bernama `hasil_prediksi`.

Output dari Python Script dikirim kembali ke KNIME dalam bentuk tabel menggunakan `knio.Table.from_pandas()`.

---

## 12. Menampilkan Hasil Prediksi Menggunakan Table View

**Node:** Table View

**Fungsi:**  
Node Table View digunakan untuk menampilkan hasil akhir dari proses klasifikasi. Pada tabel ini, data uji ditampilkan bersama label sebenarnya dan hasil prediksi dari model.

**Kolom yang ditampilkan:**

- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`
- `species`
- `hasil_prediksi`

Kolom `species` menunjukkan label asli dari dataset, sedangkan kolom `hasil_prediksi` menunjukkan label yang diprediksi oleh model Gaussian Naive Bayes.

![Hasil Table View](images/pertemuan10/04-table-view-result.png)

> Gambar 4. Hasil prediksi model pada Table View dengan kolom `species` dan `hasil_prediksi`.

---

## 13. Evaluasi Model Menggunakan Scorer

**Node:** Scorer

**Fungsi:**  
Node Scorer digunakan untuk menilai performa model klasifikasi. Proses evaluasi dilakukan dengan membandingkan label asli dan label hasil prediksi.

**Konfigurasi:**

- First column: `species`
- Second column: `hasil_prediksi`
- Sorting strategy: **Insertion order**
- Missing values: **Ignore**

Kolom `species` digunakan sebagai label asli, sedangkan kolom `hasil_prediksi` digunakan sebagai label hasil prediksi dari model.

![Konfigurasi Scorer](images/pertemuan10/05-scorer-config.png)

> Gambar 5. Konfigurasi Scorer untuk membandingkan kolom `species` dan `hasil_prediksi`.

### Hasil Evaluasi Scorer

![Hasil Scorer](images/pertemuan10/06-scorer-result.png)

> Gambar 6. Hasil evaluasi model menggunakan Scorer.

Apabila hasil Scorer menunjukkan nilai akurasi yang tinggi, maka model dapat dianggap mampu mengklasifikasikan data IRIS dengan baik. Jika terdapat kesalahan prediksi, biasanya kesalahan tersebut terjadi pada kelas `Iris-versicolor` dan `Iris-virginica` karena kedua jenis bunga tersebut memiliki karakteristik fitur yang cukup mirip.

---

# 14. Kesimpulan

Berdasarkan workflow yang telah dibuat, klasifikasi dataset IRIS menggunakan algoritma Gaussian Naive Bayes berhasil dijalankan di dalam KNIME. Proses diawali dengan pembacaan dataset melalui node CSV Reader, kemudian data dibagi menjadi data latih dan data uji menggunakan node Table Partitioner.

Pada proyek ini, pembagian data menggunakan rasio **60% data latih** dan **40% data uji** dengan strategi **Random**. Setelah itu, data latih dinormalisasi menggunakan node Normalizer pada kolom numerik, yaitu `sepal_length`, `sepal_width`, `petal_length`, dan `petal_width`.

Data uji selanjutnya dinormalisasi menggunakan node Normalizer Apply. Tahap ini dilakukan agar data uji mempunyai skala yang sama dengan data latih, sehingga proses prediksi menjadi lebih konsisten dan tidak terjadi data leakage.

Model Gaussian Naive Bayes dibuat dan dijalankan menggunakan node Python Script. Model dilatih menggunakan data latih, kemudian digunakan untuk memprediksi data uji. Hasil prediksi ditambahkan ke dalam tabel dengan nama kolom `hasil_prediksi`.

Hasil akhir ditampilkan melalui node Table View. Pada Table View, terdapat kolom `species` sebagai label asli dan kolom `hasil_prediksi` sebagai hasil prediksi model. Setelah itu, evaluasi dilakukan menggunakan node Scorer dengan membandingkan kolom `species` dan `hasil_prediksi`.

Melalui proses tersebut, dapat diketahui apakah model berhasil melakukan klasifikasi dengan baik. Jika sebagian besar nilai pada kolom `hasil_prediksi` sama dengan nilai pada kolom `species`, maka model memiliki performa klasifikasi yang baik.

---
