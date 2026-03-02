import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Analisis Siswa", layout="wide")

st.title("📊 Dashboard Analisis Hasil Siswa")

# Upload file
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("📄 Data Siswa")
    st.dataframe(df)

    # Ambil kolom pertama sebagai nama siswa
    nama_kolom = df.columns[0]

    # Kolom soal (selain nama)
    soal_columns = df.columns[1:]

    # Pastikan data numerik
    df[soal_columns] = df[soal_columns].apply(pd.to_numeric, errors="coerce").fillna(0)

    # Hitung total benar
    df["Total Benar"] = df[soal_columns].sum(axis=1)

    st.subheader("📈 Total Jawaban Benar per Siswa")
    st.dataframe(df[[nama_kolom, "Total Benar"]])

    # Grafik
    st.subheader("📊 Grafik Total Benar")
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(df[nama_kolom], df["Total Benar"])
    ax.set_xlabel("Nama Siswa")
    ax.set_ylabel("Total Benar")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Statistik
    st.subheader("📌 Statistik Kelas")
    rata_rata = df["Total Benar"].mean()
    nilai_tertinggi = df["Total Benar"].max()
    nilai_terendah = df["Total Benar"].min()

    col1, col2, col3 = st.columns(3)
    col1.metric("Rata-rata", f"{rata_rata:.2f}")
    col2.metric("Tertinggi", int(nilai_tertinggi))
    col3.metric("Terendah", int(nilai_terendah))

else:
    st.info("Silakan upload file Excel terlebih dahulu.")
