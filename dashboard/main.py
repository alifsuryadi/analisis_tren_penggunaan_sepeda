import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load Data
all_df = pd.read_csv("dashboard/all.csv")

# Sidebar
with st.sidebar:
    st.title("E-Commerce Dashboard")
    st.markdown("""Berikut adalah Tren Penggunaan Sepeda saat ini""")
    st.image("dashboard/pngegg.png")


# Title
st.header("E-Commerce Dashboard :bike:")

# 1. Tren Penggunaan Sepeda per Bulan
st.subheader("Tren Penggunaan Sepeda per Bulan")
st.markdown("""
Dari visualisasi tren penggunaan sepeda per bulan, terlihat bahwa penggunaan sepeda cenderung meningkat dari bulan-bulan awal tahun menuju puncaknya pada musim panas (biasanya bulan Juni hingga Agustus), kemudian mulai menurun menjelang akhir tahun. Ini menunjukkan bahwa cuaca dan musim memiliki pengaruh signifikan terhadap permintaan sepeda.
""")

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
monthly_total = all_df.groupby('month')['cnt_x'].sum()  # Perbaikan di sini: cnt_x sesuai dengan nama kolom di all.csv
monthly_total.plot(marker='o', color='b', ax=ax)
ax.set_title('Total Penggunaan Sepeda per Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Penggunaan Sepeda')
ax.set_xticks(monthly_total.index)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
ax.grid(True)
st.pyplot(fig)





# 2. Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur
st.subheader("Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur")

st.markdown("""
Berdasarkan perbandingan penggunaan sepeda antara hari kerja dan hari libur, terlihat bahwa penggunaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan dengan hari libur. Hal ini mungkin disebabkan oleh kebutuhan transportasi sehari-hari ke tempat kerja. Informasi ini bisa menjadi pertimbangan dalam merencanakan promosi atau menyesuaikan layanan sesuai dengan pola penggunaan sepeda yang berbeda antara hari kerja dan hari libur.
""")

# Visualisasi
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='workingday_y', y='cnt_x', data=all_df, ax=ax)  # Perbaikan di sini: cnt_x sesuai dengan nama kolom di all.csv
ax.set_title('Perbandingan Penggunaan Sepeda antara Hari Kerja dan Hari Libur')
ax.set_xlabel('Hari Kerja (0: Hari Libur, 1: Hari Kerja)')
ax.set_ylabel('Total Penggunaan Sepeda')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Hari Libur', 'Hari Kerja'])
ax.grid(True)

# Menampilkan visualisasi dengan st.pyplot(fig)
st.pyplot(fig)



# 3. Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda")

st.markdown("""
Dari visualisasi penggunaan sepeda berdasarkan kondisi cuaca, terlihat bahwa kondisi cuaca yang lebih baik (weathersit=1) memiliki jumlah penggunaan sepeda yang lebih tinggi daripada kondisi cuaca yang buruk. Hal ini konsisten dengan asumsi bahwa cuaca yang cerah dan baik akan mendorong orang untuk menggunakan sepeda lebih banyak. Dapat disimpulkan bahwa cuaca, terutama faktor suhu dan kondisi cuaca umum, memiliki pengaruh yang signifikan terhadap permintaan sepeda. Informasi ini dapat digunakan untuk mengarahkan strategi pemasaran dan promosi, serta menyesuaikan layanan sesuai dengan kondisi cuaca yang sedang berlangsung.
""")

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
weather_condition = all_df.groupby('weathersit_x')['cnt_x'].sum()  # Perbaikan di sini: cnt_x sesuai dengan nama kolom di all.csv
weather_condition.plot(kind='bar', color='skyblue')
plt.title('Penggunaan Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Total Penggunaan Sepeda')
plt.xticks(rotation=0)
plt.grid(axis='y')

# Menambahkan keterangan di bawah setiap batang
for i, val in enumerate(weather_condition.values):
    ax.text(i, val + 20, str(val), ha='center', va='bottom')
    
# Menyimpan gambar Matplotlib ke dalam variabel fig
st.pyplot(fig)

# Copyright
st.caption('Copyright (C) Alif Suryadi 2024')
