import streamlit as st

def render(atm):
    data = st.session_state.transaksi

    st.success("✅ Transaksi Berhasil")

    st.markdown("---")

    st.write("### Jenis Transaksi")
    st.write(data["jenis"])

    st.write("### Nominal")
    st.write(f"Rp {data['nominal']:,.0f}")

    st.write("### Saldo Sekarang")
    st.write(f"Rp {data['saldo']:,.0f}")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "🔄 Ya, Transaksi Lagi",
            use_container_width=True
        ):
            st.session_state.page = "menu"
            st.rerun()

    with col2:
        if st.button(
            "🚪 Tidak, Logout",
            use_container_width=True
        ):
            st.session_state.akun_login = None
            st.session_state.page = "menu"
            st.rerun()