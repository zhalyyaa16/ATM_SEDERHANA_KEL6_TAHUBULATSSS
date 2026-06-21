import streamlit as st
from halaman.login import login
from data import akun

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = None

st.title("BCI")
st.subheader("Modern Banking")

no_rekening = st.text_input("Masukkan nomor rekening: ")
pin = st.text_input("Masukkan PIN: ", type="password")

if st.button("Login"):
    user = login(no_rekening, pin)
    if user:
        st.session_state.login = True
        st.session_state.user = user

        st.success(f"Login berhasil! Selamat datang, {akun[user]['nama']}!")
    else:
        st.error("Nomor rekening atau PIN salah. Silakan coba lagi.")