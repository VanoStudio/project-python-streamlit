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
    st.title("Tes Psikologi Seberapa Brainrot kalian")
    st.markdown("""
    Ini adalah web quiz psikologi, untuk menghitung seberapa brainrot kalian

    **Cara kerjanya simpel:**
    - 👉 Klik-klik jawab soal survei absurd
    - 👻 Nanti kamu akan mendapatkan hasil "SEBERAPA BRAINROT KALIAN"

    **✨ Petunjuk:**
    1. Tarik napas pelan.
    2. Pilih jawaban yang paling mendekati dengan kalian
    3. Jangan mikir, pencet aja 
    """)

    if st.button("Mulai Survei"):
        ganti_halaman("soal1")

# ==============================
# Halaman Soal 1
# ==============================
elif st.session_state.page == "soal1":
    st.title("SOAL 1")
    pertanyaan = "🧠Rasa yang lebih kamu suka ?"
    opsi = [
        "🧃 Manis",
        "🧂 Pahit",
        "🌶 Pedas"
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
    pertanyaan = "🧠Lebih prefer ngapain pas libur ?"
    opsi = [
        "🍜 Jalan jalan ke mall",
        "😴 rebahan di kamar",
        "💻 Ngoding"
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
    pertanyaan = "🧠 Kalau bangun pagi, hal pertama yang kamu lakukan:"
    opsi = [
        "📱 Cek HP",
        "🛁 Langsung mandi",
        "😴 Lanjut tidur lagi"
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
    st.title("🔮 JADI, SEBERAPA BRAINROT KAMU ?")

    skor = 0

    # Soal 1
    if st.session_state.soal1 == "🧃 Manis":
        skor += 1
    elif st.session_state.soal1 == "🧂 Pahit":
        skor += 2
    elif st.session_state.soal1 == "🌶 Pedas":
        skor += 3

    # Soal 2
    if st.session_state.soal2 == "🍜 Jalan jalan ke mall":
        skor += 1
    elif st.session_state.soal2 == "😴 rebahan di kamar":
        skor += 2
    elif st.session_state.soal2 == "💻 Ngoding":
        skor += 3

    # Soal 3
    if st.session_state.soal3 == "📱 Cek HP":
        skor += 3
    elif st.session_state.soal3 == "🛁 Langsung mandi":
        skor += 2
    elif st.session_state.soal3 == "😴 Lanjut tidur lagi":
        skor += 1

    # Menentukan hasil
    if skor >= 8:
        gif = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjlyb2Q1aGF6Y2MyOTgxa2NtMWx1b2RnZDBuYmh5MXJpZjJvbnE2byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OVwHlQbBR6vrR2b3PE/giphy.gif"
        audio = "https://files.catbox.moe/rjn4cf.mp3"
        audio_html = f"""
            <audio autoplay loop>
            <source src="{audio}" type="audio/mpeg">
            Your browser does not support the audio element.
            </audio>
            """
        khodam = "LU DAH KENA BRAINROT STADIUM 4"
        deskripsi = "Taruh dulu hape nya, dan keluar rumah guys"

    elif skor >= 5:
        gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGE0NjduajhrNzZlNTdpZGNkMTZycThhazdxMWZvemI5M2dkcnFociZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XsNAXQl1E8ig8MHAhf/giphy.gif"
        audio = "https://files.catbox.moe/lvtu9l.mp3"
        audio_html = f"""
            <audio autoplay loop>
            <source src="{audio}" type="audio/mpeg">
            Your browser does not support the audio element.
            </audio>
            """
        khodam = "SELAMAAT ANDA CUMA TERKENA 30% EFEK DARI BRAINROT"
        deskripsi = "Fokus ke Aktivitas kalian sekarang, jangan tergiur sama konten brainrot yang ada di sosmed"
    else:
        gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGtpMmM4YnVmbnJxY3V1cGowOHo0azBvaGx3bGhpbDhtNGs1NXp6ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DyQrKMpqkAhNHZ1iWe/giphy.gif"
        audio ="https://files.catbox.moe/m0s4fz.mp3"
        audio_html = f"""
            <audio autoplay loop>
            <source src="{audio}" type="audio/mpeg">
            Your browser does not support the audio element.
            </audio>
            """
        khodam = "GG GUYS, KAMUUU JADI SALAH SATU MANUSIA YANG TIDAK TERCEMAR BRAINROT SAMA SEKALI"
        deskripsi = "Jaga diri kalian, jangan sampai diri kalian tercemar dengan brainrot yang dapat merusak kinerja otak kalian"

    # Tampilkan
    st.markdown(audio_html, unsafe_allow_html=True)
    st.image(gif)
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
