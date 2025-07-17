# Tes Psikologi: Seberapa Brainrot Kamu?

Ini adalah aplikasi kuis berbasis web menggunakan **Streamlit**, yang bertujuan untuk mengetahui tingkat "brainrot" seseorang berdasarkan pilihan absurd mereka.

---

## 🧠 Deskripsi Aplikasi

Aplikasi ini adalah kuis ringan dengan gaya absurd yang terdiri dari 3 pertanyaan pilihan ganda. Berdasarkan jawaban pengguna, skor akan dihitung untuk menentukan level brainrot mereka. Hasil akan ditampilkan bersama dengan **GIF animasi** dan **audio** sesuai dengan tingkat brainrot-nya.

---

## 🚀 Cara Menjalankan

1. Pastikan Python sudah terinstal.
2. Instal Streamlit:

   ```bash
   pip install streamlit
   ```
3. Jalankan aplikasi:

   ```bash
   streamlit run nama_file.py
   ```

---

## 📁 Struktur Navigasi Halaman

Aplikasi ini menggunakan **`st.session_state.page`** untuk mengatur navigasi antar halaman:

* `home` → Halaman pengantar
* `soal1` → Pertanyaan pertama
* `soal2` → Pertanyaan kedua
* `soal3` → Pertanyaan ketiga
* `result` → Hasil akhir kuis

---

## 🔍 Penjelasan Kode

### 1. Inisialisasi dan Navigasi

```python
if "page" not in st.session_state:
    st.session_state.page = "home"

def ganti_halaman(target):
    st.session_state.page = target
    st.rerun()
```

* Mengecek apakah kunci `'page'` sudah ada dalam `session_state`.
* Fungsi `ganti_halaman()` digunakan untuk berpindah halaman dan mererun Streamlit.

---

### 2. Styling CSS

```python
st.markdown("""
<style>
div[data-baseweb="radio"] {
    margin-top: 15px;
}
div[data-baseweb="radio"] > div {
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)
```

* Menyesuaikan tampilan radio button agar lebih besar dan rapi.

---

### 3. Halaman `home`

Berisi:

* Judul kuis
* Deskripsi cara kerja
* Tombol "Mulai Survei"

---

### 4. Halaman Soal (`soal1`, `soal2`, `soal3`)

Setiap halaman:

* Menampilkan satu pertanyaan
* 3 opsi pilihan
* Navigasi **Back** dan **Next**
* Jawaban disimpan di `st.session_state["soalX"]`

Contoh:

```python
jawaban = st.radio("", opsi, index=opsi.index(st.session_state.soal1), label_visibility="collapsed")
st.session_state.soal1 = jawaban
```

---

### 5. Halaman `result`

* Skor dihitung berdasarkan jawaban:

```python
if st.session_state.soal1 == "📱 Media sosial":
    skor += 3
```

* Berdasarkan skor, pengguna dikategorikan menjadi 3 level:

  * Skor ≥ 8 → Brainrot Stadium 4
  * Skor 5-7 → Terkena efek brainrot
  * Skor < 5 → Tidak tercemar brainrot

* Hasil ditampilkan dengan:

  * **GIF**
  * **Audio loop**
  * **Pesan & deskripsi**
  * **Rekap jawaban**
  * **Tombol "Ulangi Survei"**

---

## 📊 Skor dan Kategori

| Skor  | Kategori                  |
| ----- | ------------------------- |
| 8 - 9 | Brainrot Stadium 4        |
| 5 - 7 | Terkena 30% Efek Brainrot |
| < 5   | Tidak Tercemar Brainrot   |

---

## 📦 Dependencies

* `streamlit`
* (Audio dan GIF dimuat dari URL eksternal)

---

---

## 📸 Screenshot

### Home
<img width="1899" height="848" alt="image" src="https://github.com/user-attachments/assets/87d205f3-75ee-4200-a1f7-dd27c7d34e3f" />

### Soal 1
<img width="1893" height="846" alt="image" src="https://github.com/user-attachments/assets/ca7390b4-c3f3-42ec-a148-d4c42eab3c9e" />

### Soal 2
<img width="1919" height="858" alt="image" src="https://github.com/user-attachments/assets/fd7631dc-55de-4e4e-a4b7-933eb4e9f293" />

### Soal 3
<img width="1918" height="843" alt="image" src="https://github.com/user-attachments/assets/e3c4e71e-312d-4c5b-a588-a7ff902a31fe" />

### Result
<img width="1898" height="853" alt="image" src="https://github.com/user-attachments/assets/13745217-5821-49e3-83d8-763b84fb95dd" />
<img width="1894" height="849" alt="image" src="https://github.com/user-attachments/assets/d91a5b20-b524-40f0-ad68-5b52569949ff" />
<img width="1894" height="856" alt="image" src="https://github.com/user-attachments/assets/27cde8fd-65d5-4638-9c71-342e87e3e58d" />

## ‼️Bugs
* Ada beberapa browser yang tidak support untuk audio autoplay di bagian result nya

## 🧑‍💻 Dibuat oleh Stevano Sunuprakoso Sosroraharjo

> Aplikasi ini dibuat sebagai hiburan psikologis ringan berbasis web untuk mengenali kebiasaan absurd yang lucu namun relate.
