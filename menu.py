"""Halaman dashboard menu (termasuk tombol logout)."""
import streamlit as st
from helpers import kartu_saldo, goto


def render(atm):
    akun = st.session_state.akun_login

    st.markdown(f"#### 👋 Halo, {akun.nama}")
    kartu_saldo(akun)
    st.write("")

    menu_items = [
        ("💰", "Cek Saldo", "cek_saldo"),
        ("💸", "Tarik Tunai", "tarik"),
        ("🏦", "Setor Tunai", "setor"),
        ("🔁", "Transfer", "transfer"),
        ("📜", "Riwayat", "riwayat"),
    ]

    for ikon, label, page in menu_items:
        if st.button(f"{ikon}  {label}", key=f"menu_{page}", use_container_width=True):
            goto(page)

    st.divider()

    if st.button("🚪  Logout", key="logout", use_container_width=True):
        st.session_state.akun_login = None
        st.session_state.page = "menu"
        st.rerun()