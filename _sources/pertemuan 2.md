# ANALISIS DATASET IRIS 

## 1. Import Library dan Membaca Dataset

```python
import pandas as pd

# Membaca dataset
df = pd.read_csv("iris.csv")

# Melihat 5 data pertama
df.head()
```

---

## 2. Statistik Deskriptif

Untuk melihat statistik deskriptif seluruh kolom numerik:

```python
df.describe()
```

Untuk menghitung statistik pada kolom tertentu:

```python
df["sepal_length"].describe()
```

---

## 3. Statistik Deskriptif Sepal Length

Berdasarkan hasil perhitungan diperoleh:

- Jumlah data: 150
- Rata-rata (Mean): 5.84
- Median (Q2): 5.8
- Kuartil 1 (Q1): 5.1
- Kuartil 3 (Q3): 6.4
- Nilai minimum: 4.3
- Nilai maksimum: 7.9

### Interpretasi

- Rata-rata dan median hampir sama sehingga distribusi relatif simetris.
- Rentang data dari 4.3 sampai 7.9 menunjukkan variasi ukuran sepal cukup lebar.
- Sebanyak 50% data berada di antara 5.1 dan 6.4.

---

## 4. Statistik Deskriptif Sepal Width

```python
df["sepal_width"].describe()
```

Ringkasan hasil:

- Rata-rata sekitar 3.05
- Nilai minimum sekitar 2.0
- Nilai maksimum sekitar 4.4

Interpretasi:

Sebaran sepal_width lebih sempit dibandingkan sepal_length dan memiliki variasi sedang.

---

## 5. Statistik Deskriptif Petal Length

```python
df["petal_length"].describe()
```

Ringkasan hasil:

- Rata-rata sekitar 3.76
- Nilai minimum 1.0
- Nilai maksimum 6.9

Interpretasi:

Petal_length memiliki rentang yang cukup lebar dan menunjukkan perbedaan signifikan antar spesies.

---

## 6. Statistik Deskriptif Petal Width

```python
df["petal_width"].describe()
```

Ringkasan hasil:

- Rata-rata sekitar 1.20
- Nilai minimum 0.1
- Nilai maksimum 2.5

Interpretasi:

Petal_width menunjukkan variasi yang jelas antar spesies dan berpotensi kuat sebagai fitur pembeda.

---

## 7. Korelasi Antar Variabel

```python
df.corr(numeric_only=True)
```

Untuk melihat korelasi antara petal_length dan petal_width:

```python
df["petal_length"].corr(df["petal_width"])
```

Hasil menunjukkan korelasi positif yang kuat.

Interpretasi:

Jika petal_length meningkat, maka petal_width juga cenderung meningkat.

---

## 8. Visualisasi Scatter Plot

```python
import matplotlib.pyplot as plt

plt.scatter(df["petal_length"], df["petal_width"])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Scatter Plot Petal Length vs Petal Width")
plt.show()
```

Interpretasi:

- Terlihat pola hubungan positif antara petal_length dan petal_width.
- Kelompok spesies dapat dipisahkan berdasarkan ukuran petal.
- Fitur petal_length dan petal_width efektif untuk klasifikasi.

---

# Insight Analisis

1. Petal_length dan petal_width memiliki korelasi positif yang kuat.
2. Kedua fitur tersebut mampu membedakan spesies secara jelas.
3. Fitur petal lebih informatif dibandingkan fitur sepal dalam klasifikasi.
4. Dataset Iris termasuk permasalahan klasifikasi karena target berupa kategori (species).