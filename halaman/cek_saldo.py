import streamlit as st

def render(atm):
    akun = st.session_state.akun_login

    st.subheader("💰 Cek Saldo")

    st.success(
        f"Saldo Anda: Rp {akun.saldo:,}"
    )

    st.divider()

    if st.button(
        "⬅️ Kembali ke Menu",
        use_container_width=True
    ):
        st.session_state.page = "menu"
        st.rerun()