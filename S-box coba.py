import streamlit as st
import numpy as np
import pandas as pd
from fpdf import FPDF

def read_sbox_from_file(uploaded_file):
    lines = uploaded_file.getvalue().decode("utf-8").split("\n")
    sbox = [list(map(int, line.split())) for line in lines if line.strip()]
    return np.array(sbox)

def calculate_nonlinearity(Sbox):
    return np.random.randint(100, 130)  # Simulasi hasil

def calculate_sac(Sbox):
    return np.random.uniform(0.4, 0.6)  # Simulasi hasil

def save_to_pdf(results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hasil Analisis S-Box", ln=True, align="C")

    for key, value in results.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align="L")

    pdf_file = "Hasil_Analisis_SBox.pdf"
    pdf.output(pdf_file)
    return pdf_file

st.title("\U0001F4CA Analisis S-Box dengan Streamlit")

uploaded_file = st.file_uploader("\U0001F4C2 Pilih File S-Box (.txt)", type=["txt"])

if uploaded_file:
    Sbox = read_sbox_from_file(uploaded_file)

    nonlinearity = calculate_nonlinearity(Sbox)
    sac = calculate_sac(Sbox)

    results = {
        "Nonlinearity": nonlinearity,
        "SAC": sac
    }
    
    st.table(pd.DataFrame(results.items(), columns=["Metric", "Value"]))

    if st.button("\U0001F4C4 Simpan ke PDF"):
        pdf_file = save_to_pdf(results)
        with open(pdf_file, "rb") as f:
            st.download_button(label="\U0001F4E5 Unduh PDF", data=f, file_name=pdf_file, mime="application/pdf")
