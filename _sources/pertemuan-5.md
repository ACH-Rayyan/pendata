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


# Missing Value Imputation Menggunakan Weighted K-Nearest Neighbor (WKNN)

## Pengertian Missing Value

Dalam proses pengolahan data sering ditemukan kondisi dimana beberapa atribut tidak memiliki nilai atau nilainya tidak tersedia. Kondisi ini disebut **missing value**. Missing value dapat terjadi karena berbagai faktor seperti kesalahan saat pencatatan data, data yang tidak dikumpulkan, atau data yang hilang selama proses penyimpanan.

Apabila missing value tidak ditangani dengan baik, maka proses analisis data dapat menghasilkan informasi yang kurang akurat. Oleh karena itu diperlukan teknik untuk memperkirakan atau mengisi nilai yang hilang tersebut.

Salah satu metode yang dapat digunakan adalah **Weighted K-Nearest Neighbor (WKNN)**.

---

# Konsep Weighted K-Nearest Neighbor (WKNN)

Metode **WKNN** merupakan pengembangan dari algoritma **K-Nearest Neighbor (KNN)**. Pada metode ini, nilai yang hilang diperkirakan dengan melihat data lain yang memiliki kemiripan paling tinggi dengan data target.

Perbedaan utama antara KNN biasa dan WKNN terletak pada penggunaan **bobot**. Pada WKNN, setiap tetangga tidak memiliki pengaruh yang sama. Data yang jaraknya lebih dekat dengan data target akan memiliki bobot yang lebih besar dibandingkan data yang jaraknya lebih jauh.

Secara umum langkah-langkah metode WKNN adalah sebagai berikut:

1. Melakukan normalisasi data agar skala setiap atribut menjadi sebanding.
2. Menghitung jarak antara data target dan data lain.
3. Menghitung bobot berdasarkan jarak yang diperoleh.
4. Menghitung estimasi nilai yang hilang menggunakan rata-rata tertimbang.

---

# Dataset

Dataset yang digunakan terdiri dari tiga atribut yaitu **IPK**, **PO**, dan **JML**.

| No | IPK | PO | JML |
|----|----|---------|----|
| 1 | 2 | 2000000 | 2 |
| 2 | 3 | 3000000 | 3 |
| 3 | 4 | 2000000 | 2 |
| 4 | 2 | 2000000 | 3 |
| 5 | 3 | 3000000 | 2 |
| 6 | 4 | 4000000 | 3 |
| 7 | 2 | 3000000 | ? |

Pada baris ke-7 terdapat nilai **JML** yang belum diketahui. Nilai tersebut akan diperkirakan menggunakan metode **WKNN**.

---

# Tahap 1 – Normalisasi Data

Karena nilai atribut **IPK** dan **PO** memiliki skala yang berbeda, maka data perlu dinormalisasi terlebih dahulu menggunakan metode **Min-Max Normalization**.

Rumus yang digunakan:
x' = (x - min) / (max - min)


Contoh rumus Excel untuk normalisasi **IPK**:
=(A2-MIN($A$2:$A$8))/(MAX($A$2:$A$8)-MIN($A$2:$A$8))


Contoh rumus Excel untuk normalisasi **PO**:
=(B2-MIN($B$2:$B$8))/(MAX($B$2:$B$8)-MIN($B$2:$B$8))


Hasil normalisasi data ditunjukkan pada tabel berikut.

| No | IPK | PO | JML |
|----|----|----|----|
| 1 | 0 | 0 | 0 |
| 2 | 0.5 | 0.5 | 1 |
| 3 | 1 | 0 | 0 |
| 4 | 0 | 0 | 1 |
| 5 | 0.5 | 0.5 | 0 |
| 6 | 1 | 1 | 1 |
| 7 | 0 | 0.5 | ? |

Baris ke-7 merupakan **data target** yang nilai JML-nya akan diprediksi.

---

# Tahap 2 – Menghitung Selisih Nilai

Langkah berikutnya adalah menghitung selisih antara nilai normalisasi setiap data dengan nilai data target.

Contoh rumus Excel untuk selisih **IPK**:
=F2-$F$8

Contoh rumus Excel untuk selisih **PO**:
=G2-$G$8


---

# Tahap 3 – Menghitung Kuadrat Selisih

Selisih yang diperoleh kemudian dikuadratkan untuk mendapatkan komponen jarak.

Contoh rumus Excel:
=K2^2

---

# Tahap 4 – Menghitung Bobot

Setelah jarak diperoleh, langkah berikutnya adalah menentukan bobot setiap tetangga menggunakan rumus:
w = 1 / (jarak²)


Rumus Excel:
=1/(L2+N2)


Semakin kecil jarak antara data dengan data target, maka bobotnya akan semakin besar.

---

# Tahap 5 – Menghitung Pembilang

Pembilang dihitung dengan mengalikan bobot dengan nilai **JML** dari setiap data tetangga.

Rumus Excel:
=P2*C2


---

# Tabel Perhitungan WKNN

| No | Selisih IPK | Kuadrat IPK | Selisih PO | Kuadrat PO | Bobot | Pembilang |
|----|-------------|-------------|------------|------------|-------|-----------|
| 1 | 0 | 0 | -0.5 | 0.25 | 4 | 8 |
| 2 | 0.5 | 0.25 | 0 | 0 | 4 | 12 |
| 3 | 1 | 1 | -0.5 | 0.25 | 0.8 | 1.6 |
| 4 | 0 | 0 | -0.5 | 0.25 | 4 | 12 |
| 5 | 0.5 | 0.25 | 0 | 0 | 4 | 8 |
| 6 | 1 | 1 | 0.5 | 0.25 | 0.8 | 2.4 |

---

# Tahap 6 – Menghitung Estimasi Nilai

Setelah semua nilai diperoleh, langkah terakhir adalah menghitung estimasi nilai menggunakan **weighted average**.

Total pembilang:
=SUM(Q2:Q7)

Total bobot:
=SUM(P2:P7)


Perkiraan nilai **JML** dihitung dengan rumus:
=Total Pembilang / Total Bobot


Hasil estimasi yang diperoleh adalah:
JML ≈ 2.5


Nilai tersebut merupakan perkiraan untuk nilai **JML yang sebelumnya tidak diketahui pada baris ke-7**.

![Perhitungan WKNN](images/wknn.png)
