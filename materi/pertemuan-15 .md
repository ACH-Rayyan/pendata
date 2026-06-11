# pertemuan 15 
Langkah pertama adalah menyiapkan seluruh kebutuhan kode. Kita menggunakan pandas untuk pengolahan data, matplotlib untuk visualisasi grafik, skforecast untuk pemodelan deret waktu, lightgbm sebagai algoritma utama, serta shap dan sklearn untuk analisis interpretasi model.
# Libraries
# ==============================================================================
import pandas as pd
import matplotlib.pyplot as plt
import shap
from sklearn.inspection import permutation_importance
from sklearn.inspection import PartialDependenceDisplay
from lightgbm import LGBMRegressor
from skforecast.datasets import fetch_dataset
from skforecast.recursive import ForecasterRecursive
### Mengunduh Dataset Mentah
Dataset historis `vic_electricity` diunduh langsung menggunakan fitur dari `skforecast`. Data ini mencakup catatan konsumsi listrik harian dan suhu udara di wilayah Victoria, Australia. Perintah `data.head(3)` digunakan untuk menampilkan 3 baris pertama sebagai contoh isi data..

# Download data
# ==============================================================================
data = fetch_dataset(name="vic_electricity")
data.head(3)
### Mengonversi Data ke Skala Harian (Resampling)
Data awal yang dicatat setiap 30 menit diubah menjadi data harian (`'D'`). Total konsumsi listrik per hari dihitung dengan metode penjumlahan(`'sum'`), sementara suhu harian dihitung rata-ratanya (`'mean'`) agar lebih sesuai untuk analisis peramalan jangka panjang.
# Aggregation to daily frequency
# ==============================================================================
data = data.resample('D').agg({'Demand': 'sum', 'Temperature': 'mean'})
data.head(3)
### Membagi Data Latih dan Data Uji (Split Train-Test)
Dataset dipisahkan menjadi dua bagian: data hingga 21 Desember 2014 digunakan sebagai data latih (`data_train`) untuk membangun model, sedangkan data setelah tanggal tersebut dijadikan data uji (`data_test`) untuk mengevaluasi performa model.
# Split train-test
# ==============================================================================
data_train = data.loc[: '2014-12-21']
data_test = data.loc['2014-12-22':]
### Inisialisasi dan Pelatihan Model Peramalan
Membuat objek peramalan menggunakan `ForecasterRecursive` dengan algoritma `LGBMRegressor`. Model ini dikonfigurasi untuk melihat data 7 hari ke belakang (`lags=7`) dan memanfaatkan suhu (`exog`) untuk menebak total konsumsi listrik di masa depan.
# Create a recursive multi-step forecaster (ForecasterRecursive)
# ==============================================================================
forecaster = ForecasterRecursive(
                 estimator = LGBMRegressor(random_state=123, verbose=-1),
                 lags      = 7
             )

forecaster.fit(
    y    = data_train['Demand'],
    exog = data_train['Temperature']
)
forecaster
### Melihat Tingkat Kepentingan Fitur secara Global
Menjalankan perintah `forecaster.get_feature_importances()` untuk mengintip fitur atau variabel mana yang paling sering digunakan dan dianggap paling krusial oleh model dalam menentukan keputusan peramalan secara umum.
# Predictors importances
# ==============================================================================
forecaster.get_feature_importances()
### Mengekstrak Matriks Data Latih Internal
Menggunakan fungsi `create_train_X_y` untuk membedah bentuk tabel data ($X$ dan $y$) yang dibuat secara otomatis oleh `skforecast` di latar belakang sebelum dimasukkan ke dalam algoritma pelatihan *machine learning*.
# Training matrices used by the forecaster to fit the internal regressor
# ==============================================================================
X_train, y_train = forecaster.create_train_X_y(
                       y    = data_train['Demand'],
                       exog = data_train['Temperature']
                   )

display(X_train.head(3))
display(y_train.head(3))
### Menyiapkan Alat Bedah SHAP (Explainer)
Mengaktifkan fungsionalitas JavaScript lewat `shap.initjs()` dan membuat objek `TreeExplainer` yang diarahkan langsung ke mesin model kita (`forecaster.estimator`). Langkah ini krusial untuk menghitung kontribusi nilai (*SHAP values*) pada setiap baris data.
# 1. Inisialisasi JS untuk SHAP
shap.initjs()

# 2. Ganti forecaster.regressor menjadi forecaster.estimator
explainer = shap.TreeExplainer(forecaster.estimator)

# 3. Hitung SHAP values
shap_values = explainer.shap_values(X_train)

### Grafik SHAP Summary Plot (Model Bar)
Menampilkan grafik batang (*bar plot*) dari nilai SHAP untuk mengurutkan variabel dari yang paling berpengaruh hingga yang kurang berpengaruh terhadap hasil prediksi konsumsi listrik secara keseluruhan.

shap.summary_plot(shap_values, X_train, plot_type="bar")
### Grafik Distribusi Pengaruh Fitur (SHAP Density Plot)
Menampilkan grafik titik SHAP untuk melihat arah pengaruh variabel. Melalui grafik ini, kita bisa membaca apakah nilai suhu yang tinggi akan mendorong prediksi konsumsi listrik menjadi naik atau justru malah menurunkannya.
shap.summary_plot(shap_values, X_train)
### Membedah Alasan Prediksi pada Baris Data Pertama
Menggunakan *Force Plot* untuk menganalisis keputusan model secara spesifik (lokal) pada baris data pertama. Grafik ini akan menunjukkan faktor apa saja yang mendorong angka prediksi naik (merah) atau menahannya turun (biru) pada hari tersebut.
shap.initjs()  # Tambahkan ini di sel yang sama
shap.force_plot(explainer.expected_value, shap_values[0, :], X_train.iloc[0, :])
### Visualisasi Kolektif Force Plot (200 Data Pertama)
Menggabungkan visualisasi *Force Plot* untuk 200 baris data pertama sekaligus. Grafik interaktif ini sangat berguna untuk melihat perubahan tren keputusan model seiring berjalannya waktu atau perubahan pola data.
# Force plot for the first 200 observations in the training set
# ==============================================================================
shap.initjs()
shap.force_plot(explainer.expected_value, shap_values[:200, :], X_train.iloc[:200, :])
### Analisis Ketergantungan Variabel Suhu (Dependence Plot)
Membuat grafik khusus untuk melihat hubungan linier atau non-linier antara fluktuasi variabel `Temperature` terhadap perubahan nilai prediksi, sekaligus mendeteksi interaksinya dengan variabel pendukung lain.
# Dependence plot for Temperature
# ==============================================================================
fig, ax = plt.subplots(figsize=(7, 4))
shap.dependence_plot("Temperature", shap_values, X_train, ax=ax)
### Melakukan Peramalan Masa Depan (Predict)
Memerintahkan model yang telah dilatih untuk melakukan peramalan konsumsi listrik sebanyak 10 langkah ke depan (`steps=10`) dengan memasukkan data prediktor suhu dari masa data uji (`data_test`).
# Predict
# ==============================================================================
predictions = forecaster.predict(steps=10, exog=data_test['Temperature'])
predictions
### Membuat Matriks Input untuk Proses Prediksi
Melihat bentuk matriks data ($X$) yang diatur secara otomatis oleh fungsi internal model sewaktu memproses langkah peramalan masa depan (tabel lag yang bergeser secara rekursif).
# Create input matrix for predict method
# ==============================================================================
X_predict = forecaster.create_predict_X(steps=10, exog=data_test['Temperature'])
X_predict
### Membedah Alasan Hasil Ramalan Tanggal 22 Desember 2014
Menerapkan analisis *Force Plot* pada hasil tebakan masa depan untuk tanggal spesifik ('2014-12-22'). Ini membantu memberikan pertanggungjawaban logis mengapa model meramal angka kebutuhan listrik sebesar itu pada tanggal tersebut.
# Force plot for a specific prediction
# ==============================================================================
shap.initjs()
predicted_date = '2014-12-22'
iloc_predicted_date = X_predict.index.get_loc(predicted_date)
shap_values = explainer.shap_values(X_predict)
shap.force_plot(
    explainer.expected_value,
    shap_values[iloc_predicted_date, :],
    X_predict.iloc[iloc_predicted_date, :]
)
### Memuat Ulang Matriks Latih untuk Evaluasi Lanjutan
Menyiapkan kembali pasangan data $X\_train$ dan $y\_train$ dari model guna mempersiapkan pengujian sensitivitas alternatif menggunakan fitur evaluasi bawaan dari `scikit-learn`.
# Training matrices used by the forecaster to fit the internal regressor
# ==============================================================================
X_train, y_train = forecaster.create_train_X_y(
                       y    = data_train['Demand'],
                       exog = data_train['Temperature']
                   )

# Permutation importances
# ==============================================================================
r = permutation_importance(
    estimator    = forecaster.estimator,  # Ganti dari forecaster.regressor menjadi forecaster.estimator
    X            = X_train,
    y            = y_train,
    n_repeats    = 3,
    max_samples  = 0.5,
    random_state = 123
)

importances = pd.DataFrame({
    'feature': X_train.columns,
    'mean_importance': r.importances_mean,
    'std_importance': r.importances_std
}).sort_values('mean_importance', ascending=False)

importances
### Grafik Ketergantungan Parsial (Partial Dependence Plots)
Menampilkan visualisasi akhir menggunakan modul `sklearn.inspection` untuk mengukur efek marjinal dari satu atau dua fitur terpilih terhadap hasil prediksi model *decision tree*, sebagai validasi pelengkap dari hasil SHAP.
# Scikit-learn partial dependence plots
# ==============================================================================
fig, ax = plt.subplots(figsize=(9, 4))
ax.set_title("Decision Tree")
pd.plots = PartialDependenceDisplay.from_estimator(
    estimator    = forecaster.estimator,
    X         = X_train,
    features  = ["Temperature", "lag_1"],
    kind      = 'both',
    ax        = ax,
)
ax.set_title("Partial Dependence Plot")
fig.tight_layout();
# Jawaban Pertanyaan

---

## 1. Analisis Prediksi tentang Apa?
Analisis ini berfokus pada **peramalan kebutuhan listrik harian (*daily electricity demand*)** di wilayah Victoria, Australia.

Tidak hanya memperkirakan konsumsi listrik di masa depan, analisis ini juga menekankan pada **keterjelasan model (model explainability)**. Tujuannya adalah memahami bagaimana model *machine learning* bekerja (yang umumnya bersifat *black box*) serta mengetahui faktor-faktor utama yang memengaruhi perubahan konsumsi listrik, seperti kondisi cuaca dan pola penggunaan pada hari sebelumnya.

---

## 2. Struktur Data Training (Input & Output)
Data awal dengan interval 30 menit diolah menjadi data harian melalui proses agregasi. Struktur data yang digunakan adalah:

| Jenis Variabel | Nama Kolom / Fitur | Deskripsi / Keterangan |
| :--- | :--- | :--- |
| **Output (Target / y)** | `Demand` | Total konsumsi listrik harian yang akan diprediksi. |
| **Input (Features / X)** | `lag_1` s.d. `lag_7` | Nilai konsumsi listrik dari 1 hingga 7 hari sebelumnya. |
| **Input (Exogenous / X)** | `Temperature` | Rata-rata suhu udara harian sebagai faktor eksternal. |

---

## 3. Apa itu *Lag*?
Dalam *time series*, **lag adalah nilai historis dari variabel target** yang digunakan untuk memprediksi nilai di masa depan. Karena data bersifat harian, maka:

- **`lag_1`**: konsumsi listrik pada hari sebelumnya  
- **`lag_2`**: konsumsi listrik dua hari sebelumnya  
- **`lag_7`**: konsumsi listrik pada hari yang sama di minggu sebelumnya  

Penggunaan lag penting karena data deret waktu biasanya memiliki keterkaitan kuat dengan nilai di masa lalu.

---

## 4. Proses Analisis yang Dilakukan
Analisis dilakukan melalui empat tahap utama:

1. **Persiapan Data (Data Preparation)**  
   Data diubah dari interval 30 menit menjadi harian menggunakan `.resample('D')`. Nilai konsumsi dijumlahkan, sedangkan suhu dirata-ratakan. Setelah itu, data dibagi menjadi data latih dan data uji.

2. **Pelatihan Model (Model Training)**  
   Model dibuat menggunakan `ForecasterRecursive` dengan algoritma **LightGBM (`LGBMRegressor`)**. Model memanfaatkan 7 nilai lag serta variabel eksternal berupa suhu.

3. **Analisis Kepentingan Fitur (Feature Importance)**  
   Dilakukan menggunakan `forecaster.get_feature_importances()` untuk mengetahui fitur yang paling berpengaruh. Hasilnya menunjukkan bahwa **Temperature** dan **lag_1** menjadi faktor utama dalam prediksi.

4. **Visualisasi Explainability (SHAP Values)**  
   Library `shap` digunakan untuk menjelaskan keputusan model secara visual, meliputi:
   - **Summary Plot**: menunjukkan pengaruh global tiap fitur  
   - **Force Plot**: menjelaskan alasan di balik satu prediksi tertentu  
   - **Dependence Plot**: memperlihatkan hubungan antara suhu dan hasil prediksi  