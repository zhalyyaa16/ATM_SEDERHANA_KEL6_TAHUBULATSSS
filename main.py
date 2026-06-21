import streamlit as st

from atm import ATM
from helpers import load_css
from halaman import login, menu, cek_saldo, tarik, setor, transfer, riwayat, transaksi_berhasil

st.set_page_config(page_title="ATM BCI", page_icon="🏧", layout="centered")

load_css("style.css")

@st.cache_resource
def get_atm():
    return ATM()

atm = get_atm()

if "akun_login" not in st.session_state:
    st.session_state.akun_login = None
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "saldo_visible" not in st.session_state:
    st.session_state.saldo_visible = True 


if st.session_state.akun_login is None:
    login.render(atm)
else:
    router = {
        "menu": menu.render,
        "cek_saldo": cek_saldo.render,
        "tarik": tarik.render,
        "setor": setor.render,
        "transfer": transfer.render,
        "riwayat": riwayat.render,
        "transaksi_berhasil": transaksi_berhasil.render,
    }
    router.get(st.session_state.page, menu.render)(atm)