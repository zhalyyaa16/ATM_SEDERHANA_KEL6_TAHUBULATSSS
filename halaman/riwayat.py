import streamlit as st
import pandas as pd

def render(atm):
    st.subheader("📜 Riwayat Transaksi")

    akun = st.session_state.akun_login

    if len(akun.riwayat) == 0:
        st.info("Belum ada riwayat transaksi.")

    else:
        df = pd.DataFrame(akun.riwayat)

        df.rename(
            columns={
                "jenis": "Jenis",
                "tujuan": "Tujuan",
                "dari": "Dari",
                "nominal": "Nominal"
            },
            inplace=True
        )

        if "Nominal" in df.columns:
            df["Nominal"] = df["Nominal"].apply(
                lambda x: f"Rp {x:,.0f}".replace(",", ".")
            )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    if st.button(
        "⬅️ Kembali ke Menu",
        use_container_width=True
    ):
        st.session_state.page = "menu"
        st.rerun()