import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df_day = pd.read_csv('day_clean.csv')
    return df_day

df_day = load_data()

df_day['weather_condition'] = df_day['weather_condition'].map({1: 'Cerah', 2: 'Berawan', 3: 'Hujan'})

df_day['date'] = pd.to_datetime(df_day['date'])

st.title('Bike Sharing Dashboard')

st.header('1. Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')

fig, ax = plt.subplots()
sns.barplot(data=df_day, x='weather_condition', y='count')
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca')
ax.set_xlabel('\nKondisi Cuaca')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

st.header('2. Tren Harian Peminjaman Casual vs Registered')

start_date = pd.to_datetime(st.date_input('Pilih Tanggal Mulai', value=pd.to_datetime('2011-01-01')))
end_date = pd.to_datetime(st.date_input('Pilih Tanggal Akhir', value=pd.to_datetime('2012-12-31')))

filtered_data = df_day[(df_day['date'] >= start_date) & (df_day['date'] <= end_date)]

if filtered_data.empty:
    st.write("Tidak ada data untuk rentang tanggal yang dipilih.")
else:
    trend_data = filtered_data.groupby('date').agg({'registered': 'sum', 'casual': 'sum'}).reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(trend_data['date'], trend_data['registered'], label='Registered', color='blue')
    ax.plot(trend_data['date'], trend_data['casual'], label='Casual', color='orange')
    ax.set_title('Tren Peminjaman Harian Casual vs Registered')
    ax.set_xlabel('\nTanggal')
    ax.set_ylabel('Jumlah Peminjaman')
    ax.legend()
    st.pyplot(fig)

st.header('Kesimpulan')
st.write('Kesimpulan dari analisis ini adalah:')
st.write('- Cuaca memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda.')
st.write('- Tren peminjaman casual dan registered dapat memiliki perbedaan yang signifikan dan pada hari tertentu bisa berbeda.')

st.write('\n\n')
st.markdown('Data: Bike Sharing Dataset')
