# Pertemuan 5

## Z-Score Normalization

## 1. Pengertian Z-Score Normalization

Z-Score Normalization atau sering disebut **standardization** adalah salah satu teknik normalisasi data yang digunakan pada tahap **data preprocessing** dalam proses Data Mining maupun Machine Learning.

Dalam banyak kasus, dataset yang digunakan memiliki atribut dengan **skala nilai yang sangat berbeda**. Misalnya satu atribut memiliki rentang nilai kecil seperti **1–5**, sedangkan atribut lainnya memiliki nilai yang jauh lebih besar seperti **ribuan atau bahkan jutaan**. Perbedaan skala ini dapat mempengaruhi proses analisis data, terutama pada algoritma yang menggunakan **perhitungan jarak**.

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

$$
z = \frac{x - \mu}{\sigma}
$$

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

Misalkan terdapat dataset sederhana sebagai berikut: [10, 20, 30, 40, 100]


### Menghitung Rata-Rata (Mean)

Rata-rata dihitung dengan rumus:

Mean = (10 + 20 + 30 + 40 + 100) / 5
Mean = 40


### Menghitung Standar Deviasi

Standar deviasi dari dataset tersebut adalah: σ ≈ 31.62
