import streamlit as st
from data import akun

def tampilkan_saldo(user):
    saldo = akun[user]["saldo"]

    st.subheader("Cek Saldo")
    st.success(f"Saldo Anda: Rp {saldo:,}")