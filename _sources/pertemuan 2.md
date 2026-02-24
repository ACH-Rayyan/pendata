# Pertemuan 2 



---

## 1. CRISP-DM Data Understanding

CRISP-DM (Cross Industry Standard Process for Data Mining) adalah metodologi standar dalam data mining yang terdiri dari 6 tahap:

1. Business Understanding  
2. Data Understanding  
3. Data Preparation  
4. Modeling  
5. Evaluation  
6. Deployment  

Pada pertemuan ini difokuskan pada tahap **Data Understanding**.

---

## 2. Data Understanding

Data Understanding bertujuan untuk memahami isi dan karakteristik dataset sebelum dilakukan analisis lanjutan atau modeling.

### Tujuan:

- Memahami struktur data  
- Mengidentifikasi tipe data  
- Mengetahui kualitas data  
- Menganalisis hubungan antar variabel  

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
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
df.head()
```

---

# 2. Statistik Deskriptif

## 2.1 Statistik Umum

```python
df.describe()
```

Digunakan untuk melihat ringkasan statistik seluruh kolom numerik.

---

## 2.2 Ringkasan Statistik per Fitur

| Fitur          | Karakteristik Umum | Insight |
|---------------|-------------------|---------|
| Sepal Length  | Rentang 4.3 – 7.9 | Distribusi relatif simetris |
| Sepal Width   | Variasi lebih kecil | Tidak terlalu ekstrem |
| Petal Length  | Variasi besar antar spesies | Sangat potensial sebagai pembeda |
| Petal Width   | Variasi sangat jelas | Fitur paling kuat untuk klasifikasi |

Contoh melihat statistik satu kolom:

```python
df["sepal_length"].describe()
```

---

# 3. Analisis Korelasi

Korelasi digunakan untuk melihat hubungan antar variabel numerik.

## 3.1 Korelasi Semua Variabel

```python
df.corr(numeric_only=True)
```

---

## 3.2 Korelasi Antar Fitur

```python
df["petal_length"].corr(df["petal_width"])
df["sepal_length"].corr(df["sepal_width"])
```

---

## 3.3 Tabel Korelasi dan Interpretasi

| Variabel 1     | Variabel 2     | Nilai Korelasi | Kekuatan Hubungan | Interpretasi |
|---------------|---------------|---------------|------------------|--------------|
| petal_length | petal_width  | 0.96 | Sangat Kuat (Positif) | Jika petal_length naik, petal_width ikut naik |
| sepal_length | sepal_width  | -0.12 | Lemah (Negatif) | Hubungan sangat lemah, hampir tidak signifikan |
| sepal_length | petal_length | 0.87 | Kuat (Positif) | Sepal panjang cenderung memiliki petal panjang |
| sepal_length | petal_width  | 0.82 | Kuat (Positif) | Hubungan cukup kuat |
| sepal_width  | petal_length | -0.43 | Sedang (Negatif) | Hubungan terbalik |
| sepal_width  | petal_width  | -0.37 | Sedang (Negatif) | Hubungan terbalik |

### Kesimpulan Korelasi

- Fitur **petal_length dan petal_width** memiliki korelasi paling kuat.
- Fitur sepal memiliki hubungan yang jauh lebih lemah.
- Fitur petal lebih efektif untuk membedakan spesies.

---

# 4. Visualisasi Scatter Plot

```python
plt.scatter(df["petal_length"], df["petal_width"])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Scatter Plot Petal Length vs Petal Width")
plt.show()
```

---

## Hasil Visualisasi

![Scatter Plot Iris](images/scater.png)

![Scatter Plot Iris](images/scaterr2.png)

### Interpretasi Visualisasi

- Spesies **Setosa** terpisah sangat jelas.
- **Versicolor** dan **Virginica** berdekatan tetapi masih dapat dibedakan.
- Terlihat pola linear positif antara petal_length dan petal_width.

---

# Insight Analisis

1. Petal_length dan petal_width memiliki hubungan positif sangat kuat.
2. Kedua fitur tersebut efektif untuk klasifikasi spesies.
3. Fitur sepal kurang kuat dibanding fitur petal.
4. Dataset Iris merupakan permasalahan **klasifikasi**, karena target berupa kategori (species).

---

# Kesimpulan Akhir

Pada tahap Data Understanding:

- Dataset memiliki kualitas baik (tidak ada nilai kosong).
- Fitur petal merupakan fitur paling informatif.
- Visualisasi dan korelasi mendukung bahwa dataset cocok untuk pemodelan klasifikasi.

Tahap selanjutnya dalam CRISP-DM adalah **Data Preparation**.