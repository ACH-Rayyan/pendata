# Pertemuan 5
# Z-Score Normalization

## Pengertian

Z-Score Normalization (atau sering disebut **standardization**) adalah salah satu teknik normalisasi data yang digunakan untuk mengubah skala nilai suatu atribut sehingga memiliki distribusi tertentu. Pada metode ini, data diubah sehingga memiliki **nilai rata-rata (mean) sebesar 0** dan **standar deviasi sebesar 1**.

Metode ini banyak digunakan dalam proses **data preprocessing** pada data mining dan machine learning. Dengan melakukan standardisasi, setiap nilai dalam dataset akan menunjukkan seberapa jauh posisinya dari nilai rata-rata dalam satuan standar deviasi.

Hal ini membuat data menjadi lebih mudah dibandingkan satu sama lain, terutama ketika dataset memiliki variasi nilai yang cukup besar atau terdapat nilai yang jauh dari rata-rata (outlier).

Sebagai contoh, jika suatu nilai memiliki Z-score sebesar **1**, maka nilai tersebut berada **satu standar deviasi di atas rata-rata**. Sebaliknya, jika Z-score bernilai **-1**, maka nilai tersebut berada **satu standar deviasi di bawah rata-rata**.

Metode ini sangat berguna ketika:

- Dataset memiliki **outlier**
- Rentang nilai data tidak diketahui secara pasti
- Data akan digunakan pada algoritma yang sensitif terhadap skala data

---

## Rumus Z-Score

Secara matematis, Z-score dapat dihitung menggunakan rumus berikut:
z = (x - μ) / σ


Keterangan:

- **x** = nilai asli data  
- **μ (mu)** = rata-rata dari seluruh data  
- **σ (sigma)** = standar deviasi dari data  

Hasil dari perhitungan ini menunjukkan posisi relatif suatu nilai terhadap distribusi data.

---

## Dataset Contoh

Sebagai contoh, digunakan dataset sederhana berupa nilai ujian mahasiswa berikut:

| Mahasiswa | Nilai |
|----------|------|
| A | 55 |
| B | 60 |
| C | 65 |
| D | 70 |
| E | 95 |

Pada dataset tersebut terlihat bahwa nilai **95** cukup tinggi dibandingkan nilai lainnya. Dengan menggunakan Z-score normalization, kita dapat melihat seberapa jauh nilai tersebut dari rata-rata dataset.

---

## Implementasi Menggunakan Python

Berikut contoh implementasi Z-score normalization menggunakan **Python** dengan bantuan library **scikit-learn**. Kode ini dapat dijalankan menggunakan **Google Colab**.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Membuat dataset
data = {'nilai':[55,60,65,70,95]}
df = pd.DataFrame(data)

# Membuat objek scaler
scaler = StandardScaler()

# Melakukan normalisasi Z-score
df['z_score'] = scaler.fit_transform(df[['nilai']])

# Menampilkan hasil
print(df)
```

## Hasil Normalisasi Z-Score

Setelah menjalankan kode Python, diperoleh hasil normalisasi sebagai berikut:

| No | Nilai | Z-Score |
|----|------|--------|
| 1 | 55 | -1.005141 |
| 2 | 60 | -0.646162 |
| 3 | 65 | -0.287183 |
| 4 | 70 | 0.071796 |
| 5 | 95 | 1.866691 |


# Min-Max Normalization

## Pengertian

Min-Max Normalization adalah salah satu teknik normalisasi data yang digunakan untuk mengubah nilai suatu atribut ke dalam rentang tertentu. Rentang yang paling sering digunakan adalah **0 sampai 1**, tetapi sebenarnya dapat juga menggunakan rentang lain seperti **-1 sampai 1**.

Metode ini bekerja dengan cara menggeser dan menskalakan nilai data berdasarkan nilai minimum dan maksimum yang terdapat dalam dataset. Dengan demikian, nilai terkecil dalam dataset akan berubah menjadi **0**, sedangkan nilai terbesar akan berubah menjadi **1** jika menggunakan rentang standar 0–1.

Teknik ini banyak digunakan pada algoritma machine learning yang sensitif terhadap skala data, seperti **K-Nearest Neighbor (KNN)**, **Neural Network**, dan beberapa algoritma clustering. Dengan melakukan normalisasi Min-Max, setiap atribut akan berada pada skala yang sama sehingga tidak ada atribut yang mendominasi perhitungan.

---

## Rumus Min-Max Normalization

Secara matematis, Min-Max Normalization dapat dihitung menggunakan rumus berikut:
x' = (x - min) / (max - min)


Keterangan:

- **x** = nilai asli data  
- **min** = nilai minimum dalam dataset  
- **max** = nilai maksimum dalam dataset  
- **x'** = nilai hasil normalisasi  

Hasil normalisasi akan menghasilkan nilai dalam rentang **0 sampai 1**.

---

## Dataset Contoh

Dataset yang digunakan sama seperti sebelumnya:

| Mahasiswa | Nilai |
|----------|------|
| A | 55 |
| B | 60 |
| C | 65 |
| D | 70 |
| E | 95 |

Pada dataset tersebut:

- nilai minimum = **55**
- nilai maksimum = **95**

---

## Implementasi Menggunakan Python

Berikut contoh implementasi Min-Max Normalization menggunakan Python dengan library **scikit-learn**. Kode ini dapat dijalankan di **Google Colab**.

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# dataset contoh
data = {'nilai':[55,60,65,70,95]}
df = pd.DataFrame(data)

# membuat objek scaler
scaler = MinMaxScaler()

# melakukan normalisasi min-max
df['minmax'] = scaler.fit_transform(df[['nilai']])

# menampilkan hasil
print(df)
```

## Hasil Normalisasi Min-Max

| No | Nilai | Min-Max |
|----|------|--------|
| 1 | 55 | 0.000 |
| 2 | 60 | 0.125 |
| 3 | 65 | 0.250 |
| 4 | 70 | 0.375 |
| 5 | 95 | 1.000 |



# Decimal Scaling

## Pengertian

Decimal Scaling merupakan salah satu teknik normalisasi data yang dilakukan dengan cara menggeser posisi titik desimal pada setiap nilai numerik. Metode ini dilakukan dengan membagi setiap nilai dalam dataset menggunakan pangkat 10 tertentu sehingga nilai absolut maksimum dalam dataset menjadi lebih kecil dari 1.

Teknik ini tergolong metode normalisasi yang sederhana karena hanya melakukan pembagian berdasarkan jumlah digit dari nilai terbesar dalam dataset. Dengan cara ini, seluruh data akan memiliki skala yang lebih kecil tanpa mengubah perbandingan antar nilai.

Decimal Scaling sering digunakan ketika tujuan utama normalisasi adalah **mengecilkan skala nilai data** tanpa mengubah distribusi atau jarak relatif antar data.

Langkah utama dalam metode ini adalah menentukan nilai **j**, yaitu jumlah digit dari nilai absolut terbesar pada dataset. Setelah nilai tersebut diketahui, seluruh nilai pada dataset dibagi dengan **10 pangkat j**.

---

## Rumus Decimal Scaling

Secara matematis, Decimal Scaling dapat dituliskan sebagai berikut:
x' = x / 10^j


Keterangan:

- **x** = nilai asli data  
- **j** = jumlah digit dari nilai maksimum dalam dataset  
- **x'** = nilai hasil normalisasi  

Jika nilai maksimum pada dataset adalah **95**, maka jumlah digitnya adalah **2**, sehingga seluruh data akan dibagi dengan **10² = 100**.

---

## Dataset Contoh

Dataset yang digunakan masih sama seperti pada contoh sebelumnya:

| Mahasiswa | Nilai |
|----------|------|
| A | 55 |
| B | 60 |
| C | 65 |
| D | 70 |
| E | 95 |

Pada dataset tersebut, nilai terbesar adalah **95** sehingga jumlah digitnya adalah **2**. Oleh karena itu seluruh nilai akan dibagi dengan **100**.

---

## Implementasi Menggunakan Python

Berikut contoh implementasi Decimal Scaling menggunakan Python. Kode ini dapat dijalankan menggunakan **Google Colab**.

```python
import numpy as np
import pandas as pd

# dataset contoh
data = {'nilai':[55,60,65,70,95]}
df = pd.DataFrame(data)

# fungsi decimal scaling
def decimal_scaling(column):
    max_val = np.max(np.abs(column))
    j = len(str(int(max_val)))
    return column / (10**j)

# menerapkan normalisasi
df['decimal_scaling'] = decimal_scaling(df['nilai'])

# menampilkan hasil
print(df)
```

## Hasil Normalisasi Decimal Scaling

| No | Nilai | Decimal Scaling |
|----|------|----------------|
| 1 | 55 | 0.55 |
| 2 | 60 | 0.60 |
| 3 | 65 | 0.65 |
| 4 | 70 | 0.70 |
| 5 | 95 | 0.95 |



