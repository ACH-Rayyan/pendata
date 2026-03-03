# ===============================
# IMPORT LIBRARY
# ===============================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("IRIS.csv")

# Encoding target
le = LabelEncoder()
df["species"] = le.fit_transform(df["species"])

# Gunakan petal features
X = df[["petal_length", "petal_width"]]
y = df["species"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# INISIALISASI MODEL
# ===============================
models = {
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier()
}

results = {}

# ===============================
# TRAINING & EVALUATION
# ===============================
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    
    print(f"\n=== {name} ===")
    print("Akurasi:", acc)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

# ===============================
# VISUALISASI PERBANDINGAN
# ===============================
plt.figure()
plt.bar(results.keys(), results.values())
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Perbandingan Akurasi Model")
plt.xticks(rotation=20)
plt.show()