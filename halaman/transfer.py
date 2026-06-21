import streamlit as st

def render(atm):
    akun = st.session_state.akun_login

    st.markdown("💸 Transfer Antar Rekening")
    st.info(f"💳 Saldo kamu: Rp {akun.saldo:,}")
    st.divider()

    with st.form("form_transfer"):
        tujuan = st.text_input(
            "🏦 Rekening Tujuan",
            placeholder="Masukkan nomor rekening"
        )

        nominal = st.number_input(
            "💰 Nominal Transfer",
            min_value=0,
            step=50000
        )

        catatan = st.text_input(
            "📝 Catatan (opsional)",
            placeholder="Contoh: Bayar utang"
        )

        kirim = st.form_submit_button(
            "Transfer Sekarang",
            use_container_width=True
        )

    if kirim:
        if not tujuan:
            st.warning("⚠️ Rekening tujuan tidak boleh kosong.")

        elif nominal <= 0:
            st.warning("⚠️ Nominal harus lebih dari Rp0.")

        elif nominal > akun.saldo:
            st.error("❌ Saldo tidak mencukupi.")

        else:
            ok, pesan = atm.transfer(
                akun,
                tujuan,
                nominal
            )

            if ok:
                st.success(f"✅ {pesan}")
                st.balloons()

                if catatan:
                    st.caption(f"📝 Catatan: {catatan}")

            else:
                st.error(f"❌ {pesan}")

    st.divider()

    if st.button(
        "⬅️ Kembali ke Menu",
        use_container_width=True
    ):
        st.session_state.page = "menu"
        st.rerun()