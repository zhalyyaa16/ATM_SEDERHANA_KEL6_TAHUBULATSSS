import streamlit as st
from data import akun

def tarik(user):
    jumlah = st.number_input("Masukkan jumlah tarik:", min_value=0, step=50000)
    if st.button("Tarik"):
        if jumlah % 50000 != 0:
            st.error("Penarikan harus kelipatan Rp50.000")
        elif jumlah <= akun[user]["saldo"]:
            akun[user]["saldo"] -= jumlah
            st.success(f"Berhasil tarik Rp {jumlah:,}. Saldo sekarang Rp {akun[user]['saldo']:,}")
        else:
            st.error("Saldo tidak cukup!")