# DATA PREPARATION — PERTEMUAN 3
## Studi Kasus: Iris + Data Campuran (Mixed-Type)

```{admonition} Identitas Mahasiswa
:class: note

| | |
|---|---|
| **Nama** | Ach Rayyan |
| **NIM** | 240411100188 |
| **Mata Kuliah** | Penambangan Data |
| **Pertemuan** | 3 — Data Preparation |
```

Dokumen ini melanjutkan materi Data Preparation dalam kerangka **CRISP-DM** yang mencakup:
identifikasi missing value, statistik deskriptif, encoding, scaling, **pengukuran jarak**, dan penanganan **data campuran (mixed-type)**.

<hr />

## ✅ Tugas Pertemuan 3

```{admonition} Tugas yang Harus Diselesaikan
:class: important

Berikut tiga tugas utama pada Pertemuan 3 beserta status penyelesaiannya:

| No | Tugas | Status | Keterangan |
|:--:|-------|:------:|------------|
| 1 | **Mengukur Jarak** — ditempatkan di bawah bagian *Data Understanding* | ✅ Selesai | Euclidean, Manhattan, Spearman, Hamming pada data Iris (CSV & SQL) — lihat **Section 3.13–3.14** |
| 2 | **Buat/Cari Data Campuran** — mengandung tipe ordinal, numerik, kategorikal, dan biner | ✅ Selesai | Dataset **Titanic** (`TitanicTrain.csv` + PostgreSQL `Titanic`) — lihat **Section 3.15** |
| 3 | **Lakukan Pengukuran Jarak pada Data Campuran** tersebut | ✅ Selesai | 4 metrik jarak diterapkan di Orange pada data Titanic — lihat **Section 3.15.5** |
```

> **File Orange Workflow:** {download}`Titanic.ows <DataCampuranPertemuan3/Titanic/Titanic.ows>`
>
> **File SQL Database:** {download}`Titanic.sql <DataCampuranPertemuan3/Titanic/Titanic.sql>`

<hr />

## 3.1 Konsep CRISP-DM

**CRISP-DM** (Cross-Industry Standard Process for Data Mining) adalah metodologi standar dalam proyek data mining yang terdiri dari 6 fase berurutan:

| No | Fase | Keterangan |
|----|------|------------|
| 1 | Business Understanding | Memahami tujuan bisnis dan kebutuhan analisis |
| 2 | Data Understanding | Eksplorasi awal data, statistik deskriptif |
| 3 | **Data Preparation** | Pembersihan, transformasi, seleksi fitur |
| 4 | Modeling | Membangun model machine learning |
| 5 | Evaluation | Mengevaluasi performa model |
| 6 | Deployment | Implementasi model ke sistem nyata |

> Pertemuan ini berfokus pada fase **Data Preparation** — fase paling kritis yang memakan 60–70% waktu proyek data mining.

<hr />

## 3.2 Persiapan Lingkungan

Sebelum memulai analisis, kita impor library yang dibutuhkan. Setiap library memiliki peran khusus dalam proses data preparation.

```python
%matplotlib inline
import pandas as pd          # manipulasi dan analisis data tabular
import numpy as np           # komputasi numerik dan array
import matplotlib.pyplot as plt  # visualisasi data

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import pairwise_distances
```

| Library | Fungsi Utama |
|---------|-------------|
| `pandas` | Load CSV, manipulasi DataFrame, groupby, describe |
| `numpy` | Operasi array, kalkulasi jarak manual |
| `matplotlib` | Plot histogram, visualisasi distribusi |
| `StandardScaler` | Normalisasi fitur (mean=0, std=1) sebelum hitung jarak |
| `LabelEncoder` | Konversi label kategorikal ke numerik |
| `pairwise_distances` | Hitung distance matrix antar semua pasang data |

<hr />

## 3.3 Memuat Dataset Awal

Dataset dimuat kembali untuk memastikan seluruh proses preparation dilakukan pada data mentah yang konsisten.

```python
df = pd.read_csv("IRIS.csv")
df.head()
```

**Output `df.head()`** — 5 baris pertama dataset Iris:

| | sepal_length | sepal_width | petal_length | petal_width | species |
|--|---|---|---|---|---|
| **0** | 5.1 | 3.5 | 1.4 | 0.2 | Iris-setosa |
| **1** | 4.9 | 3.0 | 1.4 | 0.2 | Iris-setosa |
| **2** | 4.7 | 3.2 | 1.3 | 0.2 | Iris-setosa |
| **3** | 4.6 | 3.1 | 1.5 | 0.2 | Iris-setosa |
| **4** | 5.0 | 3.6 | 1.4 | 0.2 | Iris-setosa |

Dataset ini berisi **150 baris** dan **5 kolom**, terdiri dari 4 fitur numerik dan 1 kolom target kategorikal.

<hr />

## 3.4 Penjelasan: Fitur vs Kelas (Target)

Memahami perbedaan **fitur** dan **kelas** adalah dasar sebelum melakukan pemodelan supervised learning.

- **Fitur (features / attributes)** = kolom input yang menjadi karakteristik bunga, digunakan sebagai variabel independen (X).
- **Kelas (class / label / target)** = kolom output yang ingin diprediksi, merupakan variabel dependen (y).

**Tabel Identifikasi Kolom Dataset Iris:**

| Kolom | Tipe Data | Peran | Keterangan |
|-------|-----------|-------|------------|
| `sepal_length` | Numerik (float) | **Fitur** | Panjang kelopak luar / sepal (cm) |
| `sepal_width` | Numerik (float) | **Fitur** | Lebar kelopak luar / sepal (cm) |
| `petal_length` | Numerik (float) | **Fitur** | Panjang mahkota bunga / petal (cm) |
| `petal_width` | Numerik (float) | **Fitur** | Lebar mahkota bunga / petal (cm) |
| `species` | Kategorikal (string) | **Kelas (Target)** | Jenis bunga: *setosa*, *versicolor*, *virginica* |

✅ **Kesimpulan:** `sepal_length`, `sepal_width`, `petal_length`, `petal_width` → **fitur**.
Sedangkan `Iris-setosa`, `Iris-versicolor`, `Iris-virginica` → **kelas/label**.

> Jika membuat kolom `species_encoded`, itu hanya versi **numerik** dari kelas — bukan fitur baru.

<hr />

## Pembersihan Data

<hr />

## 3.5 Identifikasi Missing Value

Identifikasi missing value adalah langkah **pertama dan wajib** dalam data preparation. Data yang memiliki nilai kosong dapat menyebabkan error pada algoritma atau hasil analisis yang bias.

### 3.5.1 Jumlah Missing per Kolom

```python
missing_count = df.isnull().sum()
missing_count
```

### 3.5.2 Persentase Missing per Kolom

```python
missing_percent = (df.isnull().mean() * 100).round(2)
pd.DataFrame({'missing_count': missing_count, 'missing_%': missing_percent})
```

**Hasil Pengecekan Missing Value Dataset Iris:**

| Kolom | Missing Count | Missing % | Status |
|-------|:---:|:---:|:---:|
| `sepal_length` | 0 | 0.00% | ✅ Lengkap |
| `sepal_width` | 0 | 0.00% | ✅ Lengkap |
| `petal_length` | 0 | 0.00% | ✅ Lengkap |
| `petal_width` | 0 | 0.00% | ✅ Lengkap |
| `species` | 0 | 0.00% | ✅ Lengkap |

> Dataset Iris **tidak memiliki missing value**, sehingga tidak diperlukan proses imputasi (pengisian nilai kosong).

### 3.5.3 Menampilkan Baris yang Memiliki Missing (jika ada)

```python
rows_with_missing = df[df.isnull().any(axis=1)]
rows_with_missing.head()
```

<hr />

## Statistik Deskriptif

<hr />

## 3.5.4 Statistik Deskriptif per Fitur (Overall)

Statistik deskriptif memberikan gambaran umum distribusi data setiap fitur — ukuran pusat (mean, median) dan ukuran sebaran (std, min, max).

```python
numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df[numeric_cols].describe().T
```

**Ringkasan Statistik Deskriptif (150 data):**

| Fitur | count | mean | std | min | 25% | 50% | 75% | max |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| sepal_length | 150 | 5.843 | 0.828 | 4.3 | 5.1 | 5.80 | 6.4 | 7.9 |
| sepal_width | 150 | 3.054 | 0.434 | 2.0 | 2.8 | 3.00 | 3.3 | 4.4 |
| petal_length | 150 | 3.759 | 1.765 | 1.0 | 1.6 | 4.35 | 5.1 | 6.9 |
| petal_width | 150 | 1.199 | 0.763 | 0.1 | 0.3 | 1.30 | 1.8 | 2.5 |

### 3.5.5 Frekuensi Tiap Kelas

```python
df['species'].value_counts()
```

**Distribusi Kelas (Species):**

| Kelas | Jumlah | Persentase |
|-------|:---:|:---:|
| Iris-setosa | 50 | 33.3% |
| Iris-versicolor | 50 | 33.3% |
| Iris-virginica | 50 | 33.3% |

> Dataset Iris **seimbang** (*balanced*) — setiap kelas memiliki jumlah data yang sama (50 sampel), sehingga tidak diperlukan teknik resampling.

### 3.5.6 Statistik Deskriptif per Kelas (Ringkas)

```python
df.groupby('species')[numeric_cols].agg(['mean','std','min','max']).round(3)
```

**Statistik Mean per Kelas:**

| Kelas | sepal_length | sepal_width | petal_length | petal_width |
|-------|:---:|:---:|:---:|:---:|
| Iris-setosa | 5.006 | 3.418 | 1.464 | 0.244 |
| Iris-versicolor | 5.936 | 2.770 | 4.260 | 1.326 |
| Iris-virginica | 6.588 | 2.974 | 5.552 | 2.026 |

Tampilkan pairplot untuk melihat distribusi fitur per kelas secara visual:

```python
import matplotlib.pyplot as plt
import pandas as pd
pd.plotting.scatter_matrix(df[numeric_cols], figsize=(10, 8), c=df['species'].astype('category').cat.codes)
plt.suptitle('Pairplot Fitur Iris per Kelas')
plt.tight_layout()
plt.show()
```

![Pairplot Iris Dataset](images/scatter_iris.png)

![Scatter Plot Petal](images/scaterr2.png)

<hr />

## Data Collecting

<hr />

> 💡 **Catatan:** Setelah memahami statistik data (*Data Understanding*), langkah berikutnya adalah **pengukuran jarak** antar sampel. Dalam urutan CRISP-DM, pengukuran jarak dilakukan tepat setelah eksplorasi data — lihat **Section 3.13** untuk detail metrik dan implementasi.

## 3.11 Cara Collecting Data

Data collecting adalah proses mengumpulkan data **sebelum** preparation dimulai. Kualitas data yang dikumpulkan sangat menentukan kualitas model yang dihasilkan — prinsip "garbage in, garbage out".

**Sumber Data yang Umum Digunakan:**

| Sumber | Contoh Format | Keterangan |
|--------|--------------|------------|
| File lokal | CSV, Excel, JSON | Cara paling umum, mudah diimpor ke Python/Orange |
| Database | MySQL, PostgreSQL | Data terstruktur dari sistem informasi |
| API/Web | REST API, JSON response | Data real-time dari layanan online |
| Sensor/IoT | Time-series, stream | Data dari perangkat fisik |
| Web scraping | HTML → CSV | Pengambilan data web (jika diizinkan) |

<hr />

## Menarik Data dari Database

<hr />

## 3.12 Cara Menarik Data dari MySQL/PostgreSQL ke Orange

### 3.12.1 Langkah Umum (Workflow Orange)

1. Buka **Orange Data Mining**
2. Dari panel widget, tambahkan: **SQL Table**
3. Pilih tipe database: **MySQL** atau **PostgreSQL**
4. Isi parameter koneksi
5. Pilih tabel atau tulis query SQL kustom
6. Sambungkan output ke widget: **Data Table** → **Select Columns** → **Impute** → **Normalize**

### 3.12.2 Contoh Parameter Koneksi

| Parameter | MySQL | PostgreSQL |
|-----------|-------|-----------|
| **Host** | `localhost` | `localhost` |
| **Port** | `3306` | `5432` |
| **Database** | `nama_db` | `nama_db` |
| **User** | `root` | `postgres` |
| **Password** | `(password Anda)` | `(password Anda)` |

### 3.12.3 Contoh Query SQL

```sql
SELECT sepal_length, sepal_width, petal_length, petal_width, species
FROM iris
WHERE sepal_length IS NOT NULL;
```

> Kalau widget **SQL Table** belum tersedia: buka **Options → Add-ons**, cari dan install add-on **Orange-SQL** atau yang mendukung koneksi database.

<hr />

## Transformasi Data

<hr />

## 3.6 Encoding Label

Karena algoritma machine learning memerlukan data numerik, maka label `species` bertipe string perlu dikonversi menjadi bentuk numerik menggunakan `LabelEncoder`.

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['species_encoded'] = le.fit_transform(df['species'])
df.head()
```

**Mapping Encoding:**

| Label Asli | Encoded | Keterangan |
|-----------|:-------:|------------|
| `Iris-setosa` | **0** | Kelas pertama secara alfabet |
| `Iris-versicolor` | **1** | Kelas kedua |
| `Iris-virginica` | **2** | Kelas ketiga |

**Output `df.head()` setelah Encoding:**

| | sepal_length | sepal_width | petal_length | petal_width | species | species_encoded |
|--|---|---|---|---|---|:---:|
| **0** | 5.1 | 3.5 | 1.4 | 0.2 | Iris-setosa | 0 |
| **1** | 4.9 | 3.0 | 1.4 | 0.2 | Iris-setosa | 0 |
| **2** | 4.7 | 3.2 | 1.3 | 0.2 | Iris-setosa | 0 |
| **3** | 4.6 | 3.1 | 1.5 | 0.2 | Iris-setosa | 0 |
| **4** | 5.0 | 3.6 | 1.4 | 0.2 | Iris-setosa | 0 |
