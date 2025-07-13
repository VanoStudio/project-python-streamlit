import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

def ganti_halaman(target):
    st.session_state.page = target
    st.rerun()

# HALAMAN HOMEPAGE START
if st.session_state.page == "home":

    st.title("Tebak Khodam Anomali")
    st.markdown(f""" Ini adalah web untuk mencari khodam anomali brainrot yang selama ini diam-diam tinggal di dirimu.
    Cara kerjanya simpel:\n
    👉 Tinggal klik-klik jawab soal survei absurd,\n
    👻 Nanti muncul khodam aneh yang cocok sama energi chaotic-mu.\n 
    ✨ Cara Mengisi Survei Anomali Ini:\n
    1. Tarik napas, tapi nggak usah dalem-dalem, ntar kepenuhan.\n
    2. Klik jawaban yang paling chaos menurut suara hati dan bisikan jin lokal.\n
    3. Jangan mikir keras, biarkan otak kanan yang bertugas (otak kiri boleh istirahat dulu).\n
    4. Setelah semua terisi, BOOM 💥 kamu bakal dikasih tahu khodam aneh yang cocok sama getaran kamu.""")

    if st.button("Mulai Survei"):
        ganti_halaman("soal1")
# HALAMAN HOMEPAGE END

# HALAMAN SOAL 1 START
elif st.session_state.page == "soal1":
    st.title("SOAL 1")
    #MARKDOWN SOAL
    st.markdown("<div style='font-size:25px;margin-top:15px'>🧠Saat kamu dikasih uang 10 ribu di tengah gurun Sahara, apa yang kamu lakuin?</div>", unsafe_allow_html=True) 
    #MARKDOWN SETTING RADIO STYLE 
    st.markdown("""
    <style>
    div[data-baseweb="radio"] {
        margin-top: 15px;       /* Jarak dari atas */
    }
    div[data-baseweb="radio"] > div {
        font-size: 25px;        /* Ukuran teks radio */
    }
    </style>
    """, unsafe_allow_html=True)
    jawaban = st.radio("",["🧃 Beli es teh manis padahal nggak ada warung, tapi kamu yakin bakal muncul sendiri.","🐍 Ngobrol sama ular pasir, tanya dia bisa transfer BCA nggak.","🛸 Lempar uangnya ke langit sambil teriak “AKU SIAP DIPILIH JADI UTUSAN GALAKSI!”"],label_visibility="collapsed")
# HALAMAN SOAL 1 END
    
    
    col1,col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            ganti_halaman("home")
    with col2:
        if st.button("Next"):
            ganti_halaman("soal2")

elif st.session_state.page == "soal2":
    st.title("Soal 2")
