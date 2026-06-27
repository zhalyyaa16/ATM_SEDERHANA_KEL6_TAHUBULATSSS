import streamlit as st

def render(atm):
    akun = st.session_state.akun_login

    if "transfer_step" not in st.session_state:
        st.session_state.transfer_step = "cek_rekening"
    if "rek_tujuan_valid" not in st.session_state:
        st.session_state.rek_tujuan_valid = None

    st.markdown("💸 Transfer Antar Rekening")
    
    if st.session_state.transfer_step == "cek_rekening":
        with st.form("form_cek_rekening"):
            tujuan_angka = st.number_input(
                "🏦 Rekening Tujuan",
                min_value=0,
                step=1,
                format="%d"
            )
            
            cek_button = st.form_submit_button(
                "Lanjut", 
                use_container_width=True
            )

        if cek_button:
            tujuan = str(tujuan_angka)

            if tujuan_angka == 0:
                st.warning("⚠️ Rekening tujuan tidak boleh kosong atau 0.")
            elif tujuan == akun.no_rekening: 
                st.error("❌ Tidak bisa mentransfer ke rekening sendiri.")
            else:
                rekening_ada, hasil = atm.cek_rekening(tujuan) 
                
                if rekening_ada:
                    st.session_state.rek_tujuan_valid = tujuan
                    st.session_state.nama_tujuan_valid = hasil.nama
                    st.session_state.transfer_step = "input_nominal"
                    st.rerun()
                else:
                    st.error("❌ Nomor rekening yang dimasukkan tidak ditemukan!")

    elif st.session_state.transfer_step == "input_nominal":
        rek_target = st.session_state.rek_tujuan_valid
        
        st.info(f"🎯 Transfer ke: **{rek_target}**")

        with st.form("form_transfer_nominal"):
            nominal = st.number_input(
                "💰 Nominal Transfer",
                min_value=0,
                step=50000,
                help="Minimal transfer Rp 100.000 | Maksimal Rp 30.000.000"
            )

            kirim = st.form_submit_button(  
                "Transfer Sekarang",
                use_container_width=True
            ) 

        if kirim:
            if nominal <= 0:
                st.warning("⚠️ Nominal harus lebih dari Rp0.")
            elif nominal < 100_000:
                st.warning("⚠️ Minimal transfer adalah Rp 100.000.")
            elif nominal > 30_000_000:
                st.error("❌ Maksimal transfer adalah Rp 30.000.000 per transaksi.")
            elif nominal > akun.saldo:
                st.error("❌ Saldo anda tidak mencukupi.")
            else:

                ok, pesan = atm.transfer(akun, rek_target, nominal)

                if ok:

                    st.session_state.transaksi = {
                        "jenis": "Transfer",
                        "nominal": nominal,
                        "saldo": akun.saldo,
                        "tujuan": rek_target
                    }

                    st.session_state.transfer_step = "cek_rekening"
                    st.session_state.rek_tujuan_valid = None
                    
                    st.session_state.page = "transaksi_berhasil"
                    st.rerun()
                else:
                    st.error(f"❌ {pesan}")

        if st.button("⬅️ Ubah Rekening Tujuan"):
            st.session_state.transfer_step = "cek_rekening"
            st.session_state.rek_tujuan_valid = None
            st.rerun()
            
    st.divider()
    if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
        st.session_state.transfer_step = "cek_rekening"
        st.session_state.rek_tujuan_valid = None
        st.session_state.page = "menu"
        st.rerun()