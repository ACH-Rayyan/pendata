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



