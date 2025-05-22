import streamlit as st
from model.text_simplifier import simplify_text
from model.reader import read_text
from model.extractor import extract_text_from_file

# --- Pengaturan Halaman ---
st.set_page_config(page_title="Spello - Pembaca Disleksia AI", layout="centered")
st.title("📘 Spello - Pembaca Buku & Dokumen AI untuk Disleksia")

# --- Upload File atau Input Teks ---
st.header("1. Masukkan Teks atau Dokumen Anda")
input_method = st.radio("Pilih metode input:", ["Unggah Dokumen", "Tulis Manual"])

raw_text = ""

if input_method == "Unggah Dokumen":
    uploaded_file = st.file_uploader("Unggah file PDF atau DOCX", type=["pdf", "docx"])
    if uploaded_file is not None:
        raw_text = extract_text_from_file(uploaded_file)
        st.success("✅ Dokumen berhasil dibaca.")

elif input_method == "Tulis Manual":
    raw_text = st.text_area("Tulis atau tempelkan teks Anda di sini:", height=200)

# --- Penyederhanaan Teks ---
if raw_text:
    st.header("2. Hasil Penyederhanaan Teks")
    simplified_text = simplify_text(raw_text)
    st.markdown(f"""
        <div style='font-family:OpenDyslexic, sans-serif; font-size:18px; line-height:1.6; background-color:#272630; padding:15px; border-radius:8px;'>
            {simplified_text}
        </div>
    """, unsafe_allow_html=True)

    # --- Text to Speech ---
    st.header("3. Pembacaan Teks dengan Suara")
    if st.button("🔊 Baca Teks"):
        read_text(simplified_text)

# --- Gaya Tambahan untuk Font Disleksia ---
st.markdown("""
    <style>
        @font-face {
            font-family: 'OpenDyslexic';
            src: url('https://cdn.jsdelivr.net/gh/antijingoist/open-dyslexic/web/OpenDyslexic-Regular.otf') format('opentype');
        }
    </style>
""", unsafe_allow_html=True)
