import streamlit as st

def render(atm):
    akun = st.session_state.akun_login

    st.markdown("🏦 Setor Tunai")
    st.info(f"💳 Saldo kamu: Rp {akun.saldo:,}")

    jumlah = st.number_input(
        "Masukkan jumlah setor:",
        min_value=0,
        step=50000
    )

    if st.button(
        "Setor Tunai",
        use_container_width=True
    ):

        if jumlah <= 0:
            st.error("❌ Nominal harus lebih dari Rp0")

        elif jumlah % 50000 != 0:
            st.error("❌ Setoran harus kelipatan Rp50.000")

        else:
            ok, pesan = atm.setor(
                akun,
                jumlah
            )

            if ok:
                st.success(
                    f"✅ {pesan}\n\nSaldo sekarang: Rp {akun.saldo:,}"
                )

            else:
                st.error(f"❌ {pesan}")

    st.divider()

    if st.button(
        "⬅️ Kembali ke Menu",
        use_container_width=True
    ):
        st.session_state.page = "menu"
        st.rerun()