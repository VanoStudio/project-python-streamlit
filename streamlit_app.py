import streamlit as st

# Inisialisasi halaman awal
if "page" not in st.session_state:
    st.session_state.page = "home"

def ganti_halaman(target):
    st.session_state.page = target
    st.rerun()

# Styling
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

# ==============================
# Halaman HOME
# ==============================
if st.session_state.page == "home":
    st.title("Tebak Khodam Anomali")
    st.markdown("""
    Ini adalah web untuk mencari khodam anomali brainrot yang selama ini diam-diam tinggal di dirimu.

    **Cara kerjanya simpel:**
    - 👉 Klik-klik jawab soal survei absurd
    - 👻 Nanti muncul khodam aneh yang cocok sama energi chaotic-mu

    **✨ Petunjuk:**
    1. Tarik napas pelan.
    2. Pilih jawaban yang paling absurd menurut bisikan jin lokal.
    3. Jangan mikir, biar chaos mengalir alami.
    """)

    if st.button("Mulai Survei"):
        ganti_halaman("soal1")

# ==============================
# Halaman Soal 1
# ==============================
elif st.session_state.page == "soal1":
    st.title("SOAL 1")
    pertanyaan = "🧠Saat kamu dikasih uang 10 ribu di tengah gurun Sahara, apa yang kamu lakuin?"
    opsi = [
        "🧃 Beli es teh manis padahal nggak ada warung, tapi kamu yakin bakal muncul sendiri.",
        "🐍 Ngobrol sama ular pasir, tanya dia bisa transfer BCA nggak.",
        "🛸 Lempar uangnya ke langit sambil teriak “AKU SIAP DIPILIH JADI UTUSAN GALAKSI!”"
    ]

    st.markdown(f"<div style='font-size:25px;margin-top:15px'>{pertanyaan}</div>", unsafe_allow_html=True)

    if "soal1" not in st.session_state:
        st.session_state.soal1 = opsi[0]

    jawaban = st.radio("", opsi, index=opsi.index(st.session_state.soal1), label_visibility="collapsed")
    st.session_state.soal1 = jawaban

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Back"):
            ganti_halaman("home")
    with col3:
        if st.button("Next"):
            ganti_halaman("soal2")

# ==============================
# Halaman Soal 2
# ==============================
elif st.session_state.page == "soal2":
    st.title("SOAL 2")
    pertanyaan = "🧠Kalau kamu tiba-tiba nyasar ke dunia anime, reaksi pertama kamu?"
    opsi = [
        "🍜 Cari tukang ramen, siapa tahu Naruto nongol.",
        "💥 Langsung tantang karakter terkuat biar jadi rival abadi.",
        "📺 Ngelamar kerja jadi figuran latar biar aman."
    ]

    st.markdown(f"<div style='font-size:25px;margin-top:15px'>{pertanyaan}</div>", unsafe_allow_html=True)

    if "soal2" not in st.session_state:
        st.session_state.soal2 = opsi[0]

    jawaban = st.radio("", opsi, index=opsi.index(st.session_state.soal2), label_visibility="collapsed")
    st.session_state.soal2 = jawaban

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Back"):
            ganti_halaman("soal1")
    with col3:
        if st.button("Next"):
            ganti_halaman("soal3")

# ==============================
# Halaman Soal 3
# ==============================
elif st.session_state.page == "soal3":
    st.title("SOAL 3")
    pertanyaan = "🧠Kalau kamu bangun tidur dan jadi kecoa, langkah pertama?"
    opsi = [
        "🪞Cermin dulu. Gaya rambut kecoa kayak apa sih.",
        "🎭 Bikin drama Shakespeare versi kecoa.",
        "📞 Telepon teman pakai sinyal antena biar viral di tiktok."
    ]

    st.markdown(f"<div style='font-size:25px;margin-top:15px'>{pertanyaan}</div>", unsafe_allow_html=True)

    if "soal3" not in st.session_state:
        st.session_state.soal3 = opsi[0]

    jawaban = st.radio("", opsi, index=opsi.index(st.session_state.soal3), label_visibility="collapsed")
    st.session_state.soal3 = jawaban

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Back"):
            ganti_halaman("soal2")
    with col3:
        if st.button("Next"):
            ganti_halaman("result")

# ==============================
# Halaman Hasil (Result)
# ==============================
elif st.session_state.page == "result":
    st.title("🔮 Hasil Khodam Anomali Kamu 🔮")

    skor = 0

    # Soal 1
    if st.session_state.soal1 == "🧃 Beli es teh manis padahal nggak ada warung, tapi kamu yakin bakal muncul sendiri.":
        skor += 1
    elif st.session_state.soal1 == "🐍 Ngobrol sama ular pasir, tanya dia bisa transfer BCA nggak.":
        skor += 2
    elif st.session_state.soal1 == "🛸 Lempar uangnya ke langit sambil teriak “AKU SIAP DIPILIH JADI UTUSAN GALAKSI!”":
        skor += 3

    # Soal 2
    if st.session_state.soal2 == "🍜 Cari tukang ramen, siapa tahu Naruto nongol.":
        skor += 1
    elif st.session_state.soal2 == "💥 Langsung tantang karakter terkuat biar jadi rival abadi.":
        skor += 3
    elif st.session_state.soal2 == "📺 Ngelamar kerja jadi figuran latar biar aman.":
        skor += 2

    # Soal 3
    if st.session_state.soal3 == "🪞Cermin dulu. Gaya rambut kecoa kayak apa sih.":
        skor += 1
    elif st.session_state.soal3 == "🎭 Bikin drama Shakespeare versi kecoa.":
        skor += 2
    elif st.session_state.soal3 == "📞 Telepon teman pakai sinyal antena biar viral di tiktok.":
        skor += 3

    # Menentukan hasil
    if skor >= 8:
        khodam = "👹 RAHWANA SI MULTIVERSE"
        deskripsi = "Kamu adalah raja chaos dari segala realitas. Kehadiranmu menggetarkan semua dimensi."
    elif skor >= 5:
        khodam = "👺 SUTRADARA ASTRAL"
        deskripsi = "Chaos kamu punya struktur. Kamu tipe pengendali kericuhan dari balik layar."
    else:
        khodam = "👻 JIN BACKSTAGE"
        deskripsi = "Tenang tapi nyeleneh. Kamu chaos dengan cara yang nggak disangka-sangka."

    # Tampilkan
    st.markdown(f"## {khodam}")
    st.write(deskripsi)

    st.markdown("---")
    st.subheader("Jawabanmu:")
    st.markdown(f"**Soal 1:** {st.session_state.soal1}")
    st.markdown(f"**Soal 2:** {st.session_state.soal2}")
    st.markdown(f"**Soal 3:** {st.session_state.soal3}")

    if st.button("Ulangi Survei"):
        for k in ["soal1", "soal2", "soal3"]:
            st.session_state.pop(k, None)
        ganti_halaman("home")
