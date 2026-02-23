# PERTEMUAN 2 – MEMAHAMI DATA

---

## 1. CRISP-DM

CRISP-DM (Cross Industry Standard Process for Data Mining) adalah standar proses dalam data mining.

Tahapannya:

1. Business Understanding  
2. Data Understanding  
3. Data Preparation  
4. Modeling  
5. Evaluation  
6. Deployment  

Pada pertemuan ini fokus pada tahap Data Understanding.

---

## 2. DATA UNDERSTANDING

Data Understanding adalah proses memahami isi dan karakteristik data sebelum dilakukan analisis atau modeling.

Tujuannya:
- Mengetahui struktur data
- Mengetahui tipe data
- Mengetahui kualitas data
- Mengetahui hubungan antar variabel

---

## 3. PENTINGNYA MEMAHAMI DATA

Jika tidak memahami data:
- Bisa salah memilih metode analisis
- Bisa salah interpretasi hasil
- Bisa salah mengambil keputusan

Memahami data membantu:
- Menentukan apakah masalah termasuk klasifikasi atau regresi
- Menentukan fitur mana yang penting
- Mengetahui apakah data bersih atau tidak

---

## 4. KOMPONEN UTAMA MEMAHAMI DATA

### 1. Pengumpulan Data Awal
Mengumpulkan dataset dari sumber tertentu.

Contoh: Dataset bunga Iris.

---

### 2. Deskripsi Data
Menjelaskan isi dataset:
- Jumlah baris (data object)
- Jumlah kolom (fitur)
- Nama kolom
- Tipe data

Contoh kolom pada dataset Iris:
- sepal_length
- sepal_width
- petal_length
- petal_width
- species

---

### 3. Exploratory Data Analysis (EDA)

EDA adalah proses eksplorasi data menggunakan statistik dan visualisasi.

Yang dilakukan:
- Menghitung mean (rata-rata)
- Menghitung median (nilai tengah)
- Melihat korelasi
- Membuat scatter plot

---

### 4. Kualitas Data

Hal yang diperiksa:
- Missing value
- Data duplikat
- Outlier
- Konsistensi data

---

## 5. TYPES DATA

### A. Nominal / Kategorikal
Data berupa label tanpa urutan.

Contoh:
- species (setosa, versicolor, virginica)

---

### B. Ordinal
Data kategorikal tetapi memiliki urutan.

Contoh:
- Rendah, Sedang, Tinggi

---

### C. Biner
Data dengan dua nilai.

Simetris  
Kedua nilai sama penting.  
Contoh: Laki-laki / Perempuan

Asimetris  
Satu nilai lebih penting.  
Contoh: Penyakit (Ya lebih penting dari Tidak)

---

### D. Numerik

Interval Scaled  
Memiliki jarak yang sama tetapi tidak memiliki nol mutlak.  
Contoh: Suhu Celsius.

Ratio Scaled  
Memiliki nol mutlak.  
Contoh: Berat badan, tinggi badan.

Nilai numerik:
- Diskrit → bilangan bulat (jumlah anak)
- Kontinu → bisa pecahan (tinggi badan)

---

## 6. KOLOM DALAM DATA MINING

Kolom disebut juga:
- Fitur
- Atribut
- Dimensi
- Variabel

Jika dilakukan reduksi dimensi, jumlah kolom bisa berkurang dari kolom asli.

---

## 7. VARIABLE

Independent Variable (X)  
Variabel yang mempengaruhi.

Dependent Variable (Y)  
Variabel yang dipengaruhi.

Contoh pada dataset Iris:
- X → sepal dan petal
- Y → species

Catatan:
Variabel dependen tidak termasuk fitur.

---

## 8. SELEKSI FITUR

Seleksi fitur adalah proses memilih fitur yang paling berpengaruh terhadap target.

Tujuannya:
- Mengurangi kompleksitas model
- Meningkatkan akurasi
- Mengurangi noise

---

## 9. KORELASI

Korelasi adalah hubungan antara dua variabel.

Nilai korelasi:
- Mendekati +1 → hubungan positif kuat
- Mendekati -1 → hubungan negatif kuat
- Mendekati 0 → tidak ada hubungan

---

## 10. DATA OBJECT

Data object adalah satu baris data yang mewakili satu entitas.

Contoh:
Satu baris pada dataset Iris mewakili satu bunga iris.

---

# ANALISIS DATASET IRIS 

## 1. Statistik Deskriptif

## Statistik Deskriptif Sepal Length

Berdasarkan hasil perhitungan menggunakan Python diperoleh:

- Jumlah data: 150
- Rata-rata (Mean): 5.84
- Median (Q2): 5.8
- Kuartil 1 (Q1): 5.1
- Kuartil 3 (Q3): 6.4
- Nilai minimum: 4.3
- Nilai maksimum: 7.9

### Interpretasi

- Rata-rata dan median hampir sama → distribusi relatif simetris.
- Rentang data dari 4.3 sampai 7.9 menunjukkan variasi ukuran sepal cukup lebar.
- 50% data berada di antara 5.1 dan 6.4.

Dilakukan perhitungan:
- Mean (rata-rata)
- Median (nilai tengah)
- Standar deviasi

Tujuan:
Untuk memahami distribusi data.

---

## 2. Korelasi

Hasil analisis menunjukkan bahwa:

Petal_length dan petal_width memiliki korelasi positif yang kuat.

Artinya:
Jika petal_length meningkat, maka petal_width juga meningkat.

---

## 3. Scatter Plot

Scatter plot menunjukkan bahwa:
- Setosa terpisah jelas dari dua spesies lainnya.
- Versicolor dan Virginica sedikit berdekatan tetapi masih dapat dibedakan.

Kesimpulan:
Petal_length dan petal_width efektif digunakan untuk membedakan spesies.

---

# INSIGHT ANALISIS

1. Petal_length dan petal_width memiliki hubungan positif yang kuat.
2. Kedua fitur tersebut mampu memisahkan spesies secara jelas.
3. Fitur sepal kurang kuat dibanding petal dalam membedakan spesies.
4. Permasalahan pada dataset Iris termasuk masalah klasifikasi karena target berupa kategori (species).



## Visualisasi Scatter Plot

Berikut adalah visualisasi hubungan antara petal_length dan petal_width:

![Scatter Plot Iris](images/scatter_iris.png)