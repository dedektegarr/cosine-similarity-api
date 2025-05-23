# 📌 REST API Cosine Similarity dengan Flask

API ini digunakan untuk **preprocessing teks** dan **menghitung cosine similarity** antar teks yang telah diproses.

---

## 🚀 Instalasi

### 1️⃣ **Clone Repository**

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 2️⃣ **Buat Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Instal Dependensi**

```bash
pip install -r requirements.txt
```

---

## 🚀 Menjalankan Server API

```bash
python app.py
```

Secara default, API berjalan di `http://127.0.0.1:5000`.

---

## 🔥 Endpoint API

### 1️⃣ **Preprocessing Teks**

- **URL:** `/preprocess`
- **Method:** `POST`
- **Request Body:**

```json
{
  "texts": [
    "Mahasiswa sedang mengerjakan tugas akhir di kampus dengan tekun.",
    "Mahasiswa sedang mengerjakan tugas akhir di kampus dengan tekun."
  ]
}
```

- **Response:**

```json
{
  "processed_texts": [
    "mahasiswa tugas akhir kampus tekun",
    "mahasiswa tugas akhir kampus tekun"
  ]
}
```

---

### 2️⃣ **Perhitungan Cosine Similarity**

- **URL:** `/similarity`
- **Method:** `POST`
- **Request Body:**

```json
{
  "texts": [
    "mahasiswa tugas akhir kampus tekun",
    "tugas akhir mahasiswa kampus rajin"
  ]
}
```

- **Response:**

```json
{
  "similarity_matrix": [
    [1.0000000000000007, 0.8757463061376463],
    [0.8757463061376463, 1.0000000000000002]
  ]
}
```

---

## 🎯 Teknologi yang Digunakan

- **Flask** (Framework API)
- **NLTK & Sastrawi** (Preprocessing)
- **Scikit-Learn** (Cosine Similarity)

---

**🔥 Enjoy Coding! 🚀**
