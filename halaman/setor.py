import streamlit as st

def render(atm):
    akun = st.session_state.akun_login

    st.markdown("🏦 Setor Tunai")
    st.info("Minimal transaksi Rp50.000")

    jumlah = st.number_input(
        "Masukkan jumlah setor:",
        min_value=0,
        step=50000
    )

    if st.button("Setor Tunai", use_container_width=True):
        if jumlah < 50000:
            st.error("❌ Minimal transaksi Rp50.000")
        elif jumlah % 50000 != 0:
            st.error("❌ Setoran harus kelipatan Rp50.000")
        else:
            ok, pesan = atm.setor(akun, jumlah)
            if ok:
                st.success(f"✅ {pesan}")
                pilihan = st.radio(
                    "Apa yang ingin kamu lakukan selanjutnya?",
                    ["Lanjut Transaksi", "Keluar"],
                    horizontal=True
                )
                if pilihan == "Lanjut Transaksi":
                    st.session_state.page = "menu"
                    st.rerun()
                elif pilihan == "Keluar":
                    st.session_state.page = "beranda"
                    st.rerun()
            else:
                st.error(f"❌ {pesan}")

    st.divider()
    if st.button("⬅️ Kembali ke Menu", use_container_width=True):
        st.session_state.page = "menu"
        st.rerun()
