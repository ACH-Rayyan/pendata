# Pertemuan 2 


<hr />

## 1. CRISP-DM Data Understanding

CRISP-DM (Cross Industry Standard Process for Data Mining) adalah metodologi standar dalam data mining yang terdiri dari 6 tahap:

1. Business Understanding  
2. Data Understanding  
3. Data Preparation  
4. Modeling  
5. Evaluation  
6. Deployment  

Pada pertemuan ini difokuskan pada tahap **Data Understanding**.

<hr />

## 2. Data Understanding

Data Understanding bertujuan untuk memahami isi dan karakteristik dataset sebelum dilakukan analisis lanjutan atau modeling.

### Tujuan:

- Memahami struktur data  
- Mengidentifikasi tipe data  
- Mengetahui kualitas data  
- Menganalisis hubungan antar variabel  


<hr />

## 3. Pentingnya Memahami Data

Memahami data sangat penting sebelum melakukan modeling karena:
- Menghindari kesalahan analisis
- Mengetahui karakteristik variabel
- Menentukan teknik yang tepat
- Mengidentifikasi masalah kualitas data

<hr />

## 4. Komponen Data Understanding

1. Pengumpulan Data Awal  
2. Deskripsi Data  
3. Exploratory Data Analysis (EDA)  
4. Evaluasi Kualitas Data  

<hr />

## 5. Types of Data

### 5.1 Nominal (Kategorikal)
Data tanpa urutan.
Contoh: jenis kelamin, warna, spesies.

### 5.2 Ordinal
Data memiliki tingkatan.
Contoh: rendah, sedang, tinggi.

### 5.3 Biner
- Simetris → kedua nilai sama penting
- Asimetris → salah satu nilai lebih penting

### 5.4 Numerik
- Interval Scale → tidak memiliki nol mutlak
- Ratio Scale → memiliki nol mutlak

Nilai numerik dapat berupa:
- Diskrit
- Kontinu

---

## 6. Konsep Atribut dan Variabel

Dalam data mining, kolom disebut:
- Fitur
- Atribut
- Dimensi
- Variabel

### Independent Variable
Variabel yang mempengaruhi.

### Dependent Variable (Target)
Variabel yang dipengaruhi.

Target tidak termasuk fitur dalam proses modeling.

---

## 7. Seleksi Fitur

Seleksi fitur adalah proses menghapus fitur yang tidak berpengaruh terhadap target.

Tujuan:
- Mengurangi dimensi
- Mengurangi noise
- Meningkatkan akurasi model

---

## 8. Korelasi

Korelasi digunakan untuk mengukur hubungan antar variabel numerik.

Nilai korelasi:
- Mendekati +1 → hubungan positif kuat
- Mendekati -1 → hubungan negatif kuat
- Mendekati 0 → tidak ada hubungan

---

## 9. Data Object

Data object adalah representasi satu entitas dalam dataset.

Contoh pada dataset Iris:
- Satu baris data = satu bunga Iris
- Kolom = atribut dari bunga tersebut

---


# ANALISIS DATASET IRIS

Dataset yang digunakan adalah **Iris Dataset** dengan 150 data dan 5 kolom:

- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`
- `species`

---

## 1. Import Library dan Membaca Dataset

```python
import pandas as pd
```