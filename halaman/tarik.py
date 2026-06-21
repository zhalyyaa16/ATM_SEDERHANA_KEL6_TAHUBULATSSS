import streamlit as st

def render(atm):
    akun = st.session_state.akun_login

    st.markdown("💸 Tarik Tunai")
    st.info(f"💳 Saldo kamu: Rp {akun.saldo:,}")

    jumlah = st.number_input(
        "Masukkan jumlah tarik:",
        min_value=0,
        step=50000
    )

    if st.button(
        "Tarik Tunai",
        use_container_width=True
    ):

        if jumlah % 50000 != 0:
            st.error(
                "❌ Penarikan harus kelipatan Rp50.000"
            )

        elif jumlah <= 0:
            st.error(
                "❌ Nominal harus lebih dari Rp0"
            )

        else:
            ok, pesan = atm.tarik(
                akun,
                jumlah
            )

            if ok:

                st.session_state.transaksi = {
                    "jenis": "Tarik Tunai",
                    "nominal": jumlah,
                    "saldo": akun.saldo
                }

                st.session_state.page = "transaksi_berhasil"
                st.rerun()

            else:
                st.error(f"❌ {pesan}")

    st.divider()

    if st.button(
        "⬅️ Kembali ke Menu",
        use_container_width=True
    ):
        st.session_state.page = "menu"
        st.rerun()