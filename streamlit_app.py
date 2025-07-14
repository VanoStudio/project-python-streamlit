import streamlit as st

# Inisialisasi halaman awal
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigasi antar halaman
def ganti_halaman(target):
    st.session_state.page = target
    st.rerun()

# Data pertanyaan & pilihan
soal_data = {
    "soal1": {
        "pertanyaan": "🧠Saat kamu dikasih uang 10 ribu di tengah gurun Sahara, apa yang kamu lakuin?",
        "opsi": [
            "🧃 Beli es teh manis padahal nggak ada warung, tapi kamu yakin bakal muncul sendiri.",
            "🐍 Ngobrol sama ular pasir, tanya dia bisa transfer BCA nggak.",
            "🛸 Lempar uangnya ke langit sambil teriak “AKU SIAP DIPILIH JADI UTUSAN GALAKSI!”"
        ]
    },
    "soal2": {
        "pertanyaan": "🧠Kalau kamu tiba-tiba nyasar ke dunia anime, reaksi pertama kamu?",
        "opsi": [
            "🍜 Cari tukang ramen, siapa tahu Naruto nongol.",
            "💥 Langsung tantang karakter terkuat biar jadi rival abadi.",
            "📺 Ngelamar kerja jadi figuran latar biar aman."
        ]
    },
    "soal3": {
        "pertanyaan": "🧠Kalau kamu bangun tidur dan jadi kecoa, langkah pertama?",
        "opsi": [
            "🪞Cermin dulu. Gaya rambut kecoa kayak apa sih.",
            "🎭 Bikin drama Shakespeare versi kecoa.",
            "📞 Telepon teman pakai sinyal antena biar viral di tiktok."
        ]
    }
}

# Styling radio
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

# HALAMAN HOME
if st.session_state.page == "home":
    st.title("Tebak Khodam Anomali")
    st.markdown("""
    Ini adalah web untuk mencari khodam anomali brainrot yang selama ini diam-diam tinggal di dirimu.

    **Cara kerjanya simpel:**
    - 👉 Tinggal klik-klik jawab soal survei absurd
    - 👻 Nanti muncul khodam aneh yang cocok sama energi chaotic-mu

    **✨ Cara Mengisi Survei Anomali Ini:**
    1. Tarik napas, tapi nggak usah dalem-dalem.
    2. Klik jawaban yang paling chaos menurut suara hati dan bisikan jin lokal.
    3. Jangan mikir keras, biarkan otak kanan yang bertugas.
    4. Setelah semua terisi, BOOM 💥 kamu bakal dikasih tahu khodam aneh yang cocok sama getaran kamu.
    """)

    if st.button("Mulai Survei"):
        ganti_halaman("soal1")

# HALAMAN SOAL 1 - 3
elif st.session_state.page in ["soal1", "soal2", "soal3"]:
    key = st.session_state.page
    data = soal_data[key]

    st.title(f"{key.upper()}")
    st.markdown(f"<div style='font-size:25px;margin-top:15px'>{data['pertanyaan']}</div>", unsafe_allow_html=True)

    if key not in st.session_state:
        st.session_state[key] = data["opsi"][0]

    jawaban = st.radio(
        "",
        data["opsi"],
        index=data["opsi"].index(st.session_state[key]),
        label_visibility="collapsed"
    )
    st.session_state[key] = jawaban

    col1, col2, col3 = st.columns(3)
    halaman_sebelumnya = "home" if key == "soal1" else f"soal{int(key[-1]) - 1}"
    halaman_selanjutnya = "result" if key == "soal3" else f"soal{int(key[-1]) + 1}"

    with col1:
        if st.button("Back"):
            ganti_halaman(halaman_sebelumnya)
    with col3:
        if st.button("Next"):
            ganti_halaman(halaman_selanjutnya)

# HALAMAN RESULT
elif st.session_state.page == "result":
    st.title("🔮 Hasil Khodam Anomali Kamu 🔮")

    # Contoh hasil sederhana berdasarkan jumlah pilihan chaos
    jawaban_list = [st.session_state.get(f"soal{i+1}", "") for i in range(3)]
    skor_chaos = sum([
        "galaksi" in j.lower() or "viral" in j.lower() or "rival" in j.lower()
        for j in jawaban_list
    ])

    if skor_chaos == 3:
        khodam = "👹 RAHWANA SI MULTIVERSE"
        deskripsi = "Kamu adalah raja chaos dari segala realitas. Dimanapun kamu berada, kerusuhan pasti terjadi — dalam cara yang memesona."
    elif skor_chaos == 2:
        khodam = "👺 SUTRADARA ASTRAL"
        deskripsi = "Kamu suka jadi pusat perhatian tanpa kelihatan mencolok. Chaos-mu elegan, nggak murahan."
    else:
        khodam = "👻 JIN BACKSTAGE"
        deskripsi = "Tenang, kamu mungkin nggak kelihatan chaotic, tapi dalem hati, kamu punya dunia sendiri yang absurd."

    st.markdown(f"## {khodam}")
    st.write(deskripsi)

    st.markdown("---")
    st.subheader("Jawabanmu:")
    for i, j in enumerate(jawaban_list, 1):
        st.markdown(f"**Soal {i}:** {j}")

    if st.button("Ulangi Survei"):
        for key in ["soal1", "soal2", "soal3"]:
            st.session_state.pop(key, None)
        ganti_halaman("home")
