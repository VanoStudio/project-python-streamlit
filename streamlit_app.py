import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

def ganti_halaman(target):
    st.session_state.page = target
    st.rerun()

if st.session_state.page == "home":

    st.title("Tebak Khodam Anomali")
    st.markdown(f""" Ini adalah web untuk mencari khodam anomali brainrot yang selama ini diam-diam tinggal di dirimu.
    Cara kerjanya simpel:\n
    👉 Tinggal klik-klik jawab soal survei absurd,\n
    👻 Nanti muncul khodam aneh yang cocok sama energi chaotic-mu.""")

    if st.button("Mulai Survei"):
        ganti_halaman("halaman1")


elif st.session_state.page == "halaman1":
    st.title("halaman soal nya")
    

    if st.button("Back"):
        ganti_halaman("home")