# Pertemuan 5
## Z-Score Normalization

## 1. Pengertian Z-Score Normalization

Z-Score Normalization atau sering disebut **standardization** adalah salah satu teknik normalisasi data yang digunakan pada tahap **data preprocessing** dalam proses Data Mining maupun Machine Learning.

Dalam banyak kasus, dataset yang digunakan memiliki atribut dengan **skala nilai yang sangat berbeda**. Misalnya satu atribut memiliki rentang nilai kecil seperti 1–5, sedangkan atribut lainnya memiliki nilai yang jauh lebih besar seperti ribuan atau bahkan jutaan. Perbedaan skala ini dapat mempengaruhi proses analisis data, terutama pada algoritma yang menggunakan **perhitungan jarak**.

Z-Score Normalization bertujuan untuk mengubah distribusi data sehingga memiliki:

- **Rata-rata (mean) sebesar 0**
- **Standar deviasi sebesar 1**

Dengan menggunakan metode ini, setiap nilai akan dinyatakan dalam bentuk **berapa standar deviasi jaraknya dari rata-rata data**. Hal ini membuat data menjadi lebih mudah dibandingkan antar atribut karena berada dalam skala yang seragam.

Metode Z-Score banyak digunakan pada berbagai algoritma Machine Learning seperti:

- Logistic Regression
- Support Vector Machine (SVM)
- Principal Component Analysis (PCA)
- Neural Network

Keuntungan utama dari Z-Score adalah metode ini **tidak membatasi nilai pada rentang tertentu**, melainkan hanya menyesuaikan distribusi data agar lebih standar.

---

## 2. Rumus Z-Score Normalization

Rumus yang digunakan dalam Z-Score Normalization adalah sebagai berikut:

\[
z = \frac{x - \mu}{\sigma}
\]

### Keterangan

- **x** = nilai asli dari data  
- **μ (mu)** = rata-rata dari seluruh data  
- **σ (sigma)** = standar deviasi data  
- **z** = nilai hasil normalisasi  

### Interpretasi Nilai Z-Score

- **z = 0** → data berada tepat pada rata-rata  
- **z > 0** → data berada di atas rata-rata  
- **z < 0** → data berada di bawah rata-rata  

Semakin besar nilai absolut Z-Score, maka semakin jauh nilai tersebut dari rata-rata data.

---

## 3. Contoh Perhitungan Z-Score

Misalkan terdapat dataset sederhana sebagai berikut:

```
[10, 20, 30, 40, 100]
```

### Menghitung Rata-Rata (Mean)

Rata-rata dihitung dengan rumus:

```
Mean = (10 + 20 + 30 + 40 + 100) / 5
Mean = 40
```

### Menghitung Standar Deviasi

Standar deviasi dari dataset tersebut adalah:

```
σ ≈ 31.62
```

### Menghitung Nilai Z-Score

Setelah nilai rata-rata dan standar deviasi diketahui, setiap nilai dapat dinormalisasi menggunakan rumus Z-Score.

| Nilai Asli | Z-Score |
|-------------|--------|
| 10 | -0.94 |
| 20 | -0.63 |
| 30 | -0.32 |
| 40 | 0 |
| 100 | 1.89 |

### Interpretasi

- Nilai **40 memiliki Z-Score = 0**, yang berarti nilai tersebut tepat berada pada rata-rata dataset.
- Nilai **10 memiliki Z-Score negatif**, yang menunjukkan bahwa nilai tersebut berada di bawah rata-rata.
- Nilai **100 memiliki Z-Score terbesar**, yang berarti nilai tersebut paling jauh dari rata-rata dataset.

---

## 4. Implementasi Z-Score Menggunakan Python

Normalisasi Z-Score dapat dilakukan dengan mudah menggunakan Python dan library **scikit-learn**, khususnya dengan menggunakan kelas **StandardScaler**.

Berikut contoh implementasi sederhana menggunakan Python.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Data contoh
df = pd.DataFrame({
    'nilai': [10, 20, 30, 40, 100]
})

# Membuat objek scaler
scaler = StandardScaler()

# Melakukan normalisasi
df['z_score'] = scaler.fit_transform(df[['nilai']])

print(df)
```

### Output

```
   nilai  z_score
0     10   -0.94
1     20   -0.63
2     30   -0.32
3     40    0.00
4    100    1.89
```

---

## 5. Implementasi Z-Score di Orange Data Mining

Pada aplikasi **Orange Data Mining**, normalisasi Z-Score dapat dilakukan menggunakan **Python Script Widget**.

### Langkah-langkah

1. Menambahkan widget **File** untuk memasukkan dataset  
2. Menghubungkan widget **File** ke **Data Table** untuk melihat data  
3. Menambahkan widget **Python Script** untuk menjalankan kode Python  
4. Menghubungkan output Python Script ke **Data Table** untuk melihat hasil normalisasi  

### Script Python untuk Orange

Masukkan kode berikut pada widget **Python Script**.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from Orange.data.pandas_compat import table_to_frame, table_from_frame

if in_data is not None:
    
    # Mengubah data Orange menjadi DataFrame
    df = table_to_frame(in_data)
    
    # Mendeteksi kolom numerik
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    # Membuat objek StandardScaler
    scaler = StandardScaler()
    
    # Melakukan normalisasi Z-Score
    for col in numeric_cols:
        df[col + "_zscore"] = scaler.fit_transform(df[[col]])
    
    # Mengembalikan data ke format Orange
    out_data = table_from_frame(df)
```

---

## 6. Hasil Normalisasi

Setelah script dijalankan, dataset akan memiliki beberapa kolom tambahan seperti:

```
IPK_zscore
PO_zscore
JML_zscore
```

Kolom-kolom tersebut merupakan hasil dari proses **Z-Score Normalization** yang telah dilakukan terhadap setiap atribut numerik dalam dataset.

Dengan normalisasi ini, semua atribut memiliki skala yang lebih seimbang sehingga proses analisis data dan penerapan algoritma Machine Learning dapat berjalan dengan lebih optimal.