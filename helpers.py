"""Fungsi bantu & komponen UI yang dipakai bersama antar halaman."""
import os
import streamlit as st


def load_css(nama_file):
    if os.path.exists(nama_file):
        with open(nama_file, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def format_rupiah(nilai):
    return f"Rp{nilai:,.0f}".replace(",", ".")


def goto(page):
    st.session_state.page = page
    st.rerun()


def kartu_saldo(akun, show_toggle=True):
    """Tampilkan kartu saldo. Saldo bisa disembunyikan via session_state.saldo_visible."""
    visible = st.session_state.saldo_visible
    nilai_tampil = format_rupiah(akun.saldo) if visible else "Rp ••••••••"
    icon_btn = "🙈" if visible else "👁️"
    label_btn = "Sembunyikan Saldo" if visible else "Tampilkan Saldo"

    st.markdown(
        f"""
        <div class="balance-card">
            <div class="bc-label">Saldo Saat Ini</div>
            <div class="bc-value">{nilai_tampil}</div>
            <div class="bc-footer">
                <span>{akun.nama}</span>
                <span>•••• {akun.no_rekening[-4:]}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if show_toggle:
        if st.button(
            f"{icon_btn}  {label_btn}",
            key=f"toggle_saldo_{st.session_state.page}",
            use_container_width=True,
        ):
            st.session_state.saldo_visible = not st.session_state.saldo_visible
            st.rerun()


def tombol_kembali():
    if st.button("← Kembali ke Menu", use_container_width=True):
        goto("menu")