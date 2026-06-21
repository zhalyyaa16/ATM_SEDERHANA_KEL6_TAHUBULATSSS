import streamlit as st
from data import akun

def setor(user):
    jumlah = st.number_input("Masukkan jumlah setor:", min_value=0, step=50000)
    if st.button("Setor"):
        if jumlah % 50000 != 0:
            st.error("Setoran harus kelipatan Rp50.000")
        else:
            akun[user]["saldo"] += jumlah
            st.success(f"Berhasil setor Rp {jumlah:,}. Saldo sekarang Rp {akun[user]['saldo']:,}")