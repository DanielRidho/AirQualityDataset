import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os


@st.cache_data
def load_data():
    os.chdir("../dashboard")
    df = pd.read_csv("dashboard/clean_merged_dataset.csv")
    
    df_Aotizhongxin = pd.read_csv(
        "data/PRSA_Data_Aotizhongxin_20130301-20170228.csv"
    )
    df_Changping = pd.read_csv(
        "data/PRSA_Data_Changping_20130301-20170228.csv"
    )
    df_Dingling = pd.read_csv(
        "data/PRSA_Data_Dingling_20130301-20170228.csv"
    )
    df_Dongsi = pd.read_csv(
        "data/PRSA_Data_Dongsi_20130301-20170228.csv"
    )
    df_Guanyuan = pd.read_csv(
        "data/PRSA_Data_Guanyuan_20130301-20170228.csv"
    )
    df_Gucheng = pd.read_csv(
        "data/PRSA_Data_Gucheng_20130301-20170228.csv"
    )
    df_Huairou = pd.read_csv(
        "data/PRSA_Data_Huairou_20130301-20170228.csv"
    )
    df_Nongzhanguan = pd.read_csv(
        "data/PRSA_Data_Nongzhanguan_20130301-20170228.csv"
    )
    df_Shunyi = pd.read_csv(
        "data/PRSA_Data_Shunyi_20130301-20170228.csv"
    )
    df_Tiantan = pd.read_csv(
        "data/PRSA_Data_Tiantan_20130301-20170228.csv"
    )
    df_Wanliu = pd.read_csv(
        "data/PRSA_Data_Wanliu_20130301-20170228.csv"
    )
    df_Wanshouxigong = pd.read_csv(
        "data/PRSA_Data_Wanshouxigong_20130301-20170228.csv"
    )

    df["date_time"] = pd.to_datetime(df["date_time"])

    return (
        df,
        df_Aotizhongxin,
        df_Changping,
        df_Dingling,
        df_Dongsi,
        df_Guanyuan,
        df_Gucheng,
        df_Huairou,
        df_Nongzhanguan,
        df_Shunyi,
        df_Tiantan,
        df_Wanliu,
        df_Wanshouxigong,
    )


(
    df,
    df_Aotizhongxin,
    df_Changping,
    df_Dingling,
    df_Dongsi,
    df_Guanyuan,
    df_Gucheng,
    df_Huairou,
    df_Nongzhanguan,
    df_Shunyi,
    df_Tiantan,
    df_Wanliu,
    df_Wanshouxigong,
) = load_data()

st.sidebar.image("pic.png")
st.sidebar.title("Air Quality Dataset")
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    [
        "Home",
        "Dataset Tiap Wilayah",
        "Pertanyaan 1",
        "Pertanyaan 2",
        "Pertanyaan 3",
        "Kesimpulan",
    ],
)

wilayah_dir = {
    "Aotizhongxin": df_Aotizhongxin,
    "Changping": df_Changping,
    "Dingling": df_Dingling,
    "Dongsi": df_Dongsi,
    "Guanyuan": df_Guanyuan,
    "Gucheng": df_Gucheng,
    "Huairou": df_Huairou,
    "Nongzhanguan": df_Nongzhanguan,
    "Shunyi": df_Shunyi,
    "Tiantan": df_Tiantan,
    "Wanliu": df_Wanliu,
    "Wanshouxigong": df_Wanshouxigong,
}

if menu == "Home":
    st.title("Air Quality Dataset")
    st.markdown(
        """
        By Daniel Ridho Abadi (danielgagg21@gmail.com)\n
        Kualitas udara (Air Quality) adalah ukuran yang menunjukkan kondisi udara di berbagai wilayah China. Sebagai negara dengan perkembangan industri dan populasi yang pesat, pemantauan kualitas udara menjadi aspek kritis dalam pengelolaan lingkungan. Pengukuran dilakukan melalui jaringan stasiun pemantauan yang mencatat beberapa parameter utama:

        1. Polutan yang dipantau:
        - PM2.5 (partikel halus)
        - PM10 (partikel kasar)
        - SO2 (sulfur dioksida)
        - NO2 (nitrogen dioksida)
        - CO (karbon monoksida)
        - O3 (ozon)

        2. Parameter pendukung:
        - TEMP
        - PRES
        - DEWP
        - RAIN
        - WSPM

        Data kualitas udara China digunakan dalam berbagai konteks:
        - Menganalisis pola perubahan polusi udara seiring waktu
        - Memprediksi kondisi udara untuk periode mendatang
        - Menilai keberhasilan program pengendalian polusi
        - Studi korelasi antara polusi dan kesehatan masyarakat
        - Pengembangan strategi perbaikan kualitas udara
        """
    )
    st.subheader("Deskripsi Data")
    st.write(df.describe())
    st.subheader("Head Dataframe yang Sudah Dibersihkan")
    st.dataframe(df.head())
elif menu == "Dataset Tiap Wilayah":
    st.title("Dataset Kualitas Udata berdasarkan Wilayah di Beijing.")

    selected_wilayah = st.sidebar.selectbox("Pilih Wilayah:", list(wilayah_dir.keys()))

    st.subheader(f"Wilayah: {selected_wilayah}")
    st.subheader("Deskripsi Data")
    st.write(wilayah_dir[selected_wilayah].describe())
    st.subheader(f"Head Dataset {selected_wilayah}")
    st.dataframe(wilayah_dir[selected_wilayah].head())
elif menu == "Pertanyaan 1":
    st.title(
        "Bagaimana tren tahunan tingkat rata-rata CO di seluruh lokasi pengukuran dari 2013 hingga 2017 dan apakah ada pola umum  terlihat?"
    )

    # Mengonversi kolom date_time menjadi datetime
    df["date_time"] = pd.to_datetime(df["date_time"])

    # Membuat plot
    yearly_co = df.groupby('year')['CO'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=yearly_co, x='year', y='CO', marker='o', linewidth=2)
    plt.title('Tren Rata-rata Tahunan Tingkat CO (2013-2017)')
    plt.xlabel('Tahun')
    plt.ylabel('Tingkat CO (μg/m³)')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Menambahkan label nilai di atas titik
    for x, y in zip(yearly_co['year'], yearly_co['CO']):
     plt.text(x, y + 30, f'{y:.1f}', ha='center')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    # Menampilkan statistik deskriptif
    st.write("Statistik deskriptif tingkat CO per tahun:")
    st.dataframe(yearly_co.style.format({'CO': '{:.1f}'}))

    # Alternatif tampilan statistik yang lebih detail
    st.write("\nDetail statistik per tahun:")
    st.write("Nilai rata-rata CO tertinggi:", 
                f"{yearly_co['CO'].max():.1f} μg/m³ (Tahun {yearly_co.loc[yearly_co['CO'].idxmax(), 'year']})")
    st.write("Nilai rata-rata CO terendah:", 
                f"{yearly_co['CO'].min():.1f} μg/m³ (Tahun {yearly_co.loc[yearly_co['CO'].idxmin(), 'year']})")
    st.write("Rata-rata keseluruhan:", f"{yearly_co['CO'].mean():.1f} μg/m³")
    st.write("Perubahan dari 2013 ke 2017:", 
                f"{yearly_co.iloc[-1]['CO'] - yearly_co.iloc[0]['CO']:.1f} μg/m³")
         
    # Insight/Kesimpulan
    st.subheader("Insight:")
    st.markdown(
        f"""
        - Peningkatan kecil dari 2013 ke 2014
        - Penurunan dari 2014 hingga 2016
        - Peningkatan signifikan di 2017 (mencapai level tertinggi)
    """
    )

elif menu == "Pertanyaan 2":
    st.title(
        "Apakah ada korelasi antara suhu dan tingkat O3 di seluruh lokasi pengukuran selama periode pengamatan?"
    )

    # Mengonversi kolom date_time menjadi datetime
    df["date_time"] = pd.to_datetime(df["date_time"])

    # Membuat scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='TEMP', y='O3', alpha=0.5)
    plt.title('Korelasi antara Suhu dan Tingkat O3')
    plt.xlabel('Suhu (°C)')
    plt.ylabel('Tingkat O3 (μg/m³)')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    # Menghitung korelasi
    correlation = df[['TEMP', 'O3']].corr()

    # Menampilkan korelasi dalam bentuk tabel
    st.write("Korelasi antara Suhu dan Tingkat O3:")
    st.dataframe(correlation.style.format("{:.6f}"))
    
    # Insight/Kesimpulan
    temp_o3_corr = correlation.iloc[0,1]

    st.subheader("Insight:")
    st.write(f"""
        ---
        - Terdapat korelasi positif moderat (r = {temp_o3_corr:.6f})
        - Scatter plot menunjukkan tren positif yang jelas
        - Semakin tinggi suhu, cenderung semakin tinggi tingkat O3

        """
    )

elif menu == "Pertanyaan 3":
    st.title(
        "Bagaimana distribusi tingkat NO2 di berbagai stasiun pengukuran di Beijing berdasarkan musim, dan stasiun pengukuran mana yang menunjukkan perbedaan tingkat NO2 terkecil antar musim?"
    )

    # Mengonversi kolom date_time menjadi datetime
    df["date_time"] = pd.to_datetime(df["date_time"])

    # Menambahkan plot
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Musim Dingin'
        elif month in [3, 4, 5]:
            return 'Musim Semi'
        elif month in [6, 7, 8]:
            return 'Musim Panas'
        else:
            return 'Musim Gugur'

    df['season'] = df['month'].apply(get_season)

    seasonal_no2 = df.groupby(['station', 'season'])['NO2'].mean().reset_index()

    plt.figure(figsize=(15, 6))
    sns.boxplot(data=df, x='station', y='NO2', hue='season')
    plt.xticks(rotation=45)
    plt.title('Distribusi NO2 berdasarkan Stasiun dan Musim')
    plt.xlabel('Stasiun')
    plt.ylabel('Tingkat NO2 (\u03bcg/m\u00b3)')
    plt.tight_layout()
    st.pyplot(plt)

    seasonal_variation = seasonal_no2.pivot(index='station', columns='season', values='NO2')
    seasonal_variation['variation'] = seasonal_variation.max(axis=1) - seasonal_variation.min(axis=1)
    seasonal_variation = seasonal_variation.sort_values('variation')

    st.write(f"Variasi musiman NO2 di setiap stasiun (dari terkecil ke terbesar):")
    for station, value in seasonal_variation['variation'].items():
        st.write(f"{station}: {value:.6f}")

    # Insight/Kesimpulan
    min_variation = seasonal_variation['variation'].idxmin()
    st.subheader("Insight:")
    st.write(f"""
        ---
        - Perbedaan tingkat NO2 terkecil antar musim yaitu **{min_variation}**
        - Musim dingin dan gugur menunjukkan peningkatan polusi NO2.
        - Stasiun pengukuran dengan variasi tingkat NO2 terkecil antar musim yaitu Dongsi
        - Musim berdampak signifikan pada variasi polusi NO2.

            """)

elif menu == "Kesimpulan":
    st.title("Kesimpulan Analisis Kualitas Udara (Air Quality)")

    st.subheader("1. Tren Tahunan Tingkat Rata-rata CO dari 2013 hingga 2017 di Semua Lokasi Pengukuran")
    st.write(
        """
        - **Pola Fluktuatif dengan Tren Peningkatan Akhir Periode:**

            Analisis terhadap tren tahunan tingkat rata-rata karbon monoksida (CO) dari 2013 hingga 2017 menunjukkan pola fluktuatif, dengan peningkatan signifikan menjelang akhir periode pengamatan. Tren ini mencerminkan dinamika emisi CO di seluruh lokasi pengukuran yang tersebar di Beijing.

        - **Periode 2013-2014: Peningkatan Moderat**

            Pada tahun 2013, tingkat rata-rata CO berada di sekitar **1180.1 μg/m³**. Ini adalah titik awal pengamatan. Selama periode 2013 hingga 2014, terdapat sedikit peningkatan, dan tingkat rata-rata CO naik menjadi **1204.6 μg/m³**. Peningkatan moderat ini bisa jadi akibat dari faktor-faktor musiman, seperti peningkatan lalu lintas dan kegiatan industri.

        - **Periode 2014-2016: Penurunan Bertahap**

            Dari 2014 hingga 2016, terjadi penurunan bertahap dalam tingkat CO. Pada tahun 2015, CO rata-rata menurun menjadi **1138.2 μg/m³**, dan terus menurun hingga mencapai titik terendah dalam periode ini pada tahun 2016, yaitu **1085.3 μg/m³**. Penurunan ini mungkin disebabkan oleh upaya pemerintah Beijing dalam mengurangi polusi udara dengan menerapkan kebijakan pengendalian emisi yang lebih ketat, seperti pembatasan lalu lintas dan peningkatan standar lingkungan pada industri.

        - **Tahun 2017: Lonjakan Signifikan**

            Namun, pada tahun 2017, ada lonjakan yang cukup tajam dalam tingkat rata-rata CO yang mencapai **1358.6 μg/m³**, yang berarti peningkatan sekitar **25%** dibandingkan tahun sebelumnya. Ini adalah peningkatan terbesar selama periode pengamatan. Faktor-faktor seperti cuaca ekstrem, peningkatan lalu lintas, atau kelonggaran sementara dalam regulasi lingkungan mungkin menjadi penyebab utama dari lonjakan ini.

        - **Kesimpulan Umum:**

            Meskipun ada beberapa fluktuasi dari tahun ke tahun, secara keseluruhan, rata-rata tingkat CO di seluruh lokasi pengukuran selama periode pengamatan cukup tinggi, yaitu lebih dari **1000 μg/m³**. Tren yang meningkat menjelang akhir periode bisa menjadi sinyal perlunya tindakan lebih lanjut untuk mengurangi polusi udara di Beijing, terutama dalam hal emisi CO, yang banyak dihasilkan dari transportasi dan industri.

        ---
        """
    )

    st.subheader("2. Korelasi Antara Suhu dan Tingkat O3 Selama Periode Pengamatan")
    st.write(
        """
        - **Korelasi Positif yang Signifikan (r = 0.596):**

            Analisis statistik menunjukkan adanya **korelasi positif yang signifikan** antara suhu dan tingkat Ozon (O3) di seluruh stasiun pengukuran selama periode pengamatan, dengan **nilai korelasi r = 0.596**. Ini menunjukkan bahwa ketika suhu meningkat, tingkat O3 juga cenderung meningkat secara proporsional di semua lokasi pengukuran.

        - **Pola Sebaran Menunjukkan Hubungan Linear:**

            Data menunjukkan bahwa ada hubungan linear yang jelas antara suhu dan O3, di mana setiap kenaikan suhu **1°C** berkaitan dengan peningkatan konsisten dalam level O3. Hal ini dapat dipahami dari perspektif kimia atmosfer, di mana suhu yang lebih tinggi mendukung reaksi fotokimia yang diperlukan untuk pembentukan O3 di lapisan troposfer.

        - **Fenomena Fotokimia:**

            Peningkatan tingkat O3 seiring dengan naiknya suhu sesuai dengan teori fotokimia yang mengatakan bahwa sinar ultraviolet (UV) dari matahari memicu reaksi antara nitrogen oksida (NOx) dan senyawa organik volatil (VOC), membentuk O3 sebagai produk samping. Proses ini dipercepat pada suhu yang lebih tinggi, yang menjelaskan mengapa musim panas biasanya memiliki tingkat O3 yang lebih tinggi.

        - **Implikasi pada Manajemen Kualitas Udara:**

            Temuan ini memiliki implikasi penting untuk kebijakan pengendalian polusi udara, terutama selama bulan-bulan panas. Peningkatan suhu, yang sering terjadi di musim panas, dapat menyebabkan pembentukan O3 yang lebih tinggi, sehingga langkah-langkah pencegahan tambahan mungkin diperlukan untuk mengurangi paparan O3 di musim panas.

        - **Variabilitas Faktor Lain:**

            Meskipun ada hubungan yang signifikan antara suhu dan O3, data juga menunjukkan adanya variabilitas yang mungkin disebabkan oleh faktor-faktor lain, seperti kelembapan, kecepatan angin, dan variasi sumber emisi polutan. Faktor-faktor ini perlu dipertimbangkan lebih lanjut dalam analisis mendalam terkait polusi O3.

        ---

        """
    )

    st.subheader("3. Distribusi Musiman NO2 di Berbagai Stasiun Pengukuran di Beijing Berdasarkan Musim")
    st.write(
        """
        - **Variasi Musiman NO2 di Berbagai Stasiun:**

            Tingkat NO2 menunjukkan variasi yang signifikan di berbagai stasiun pengukuran di Beijing berdasarkan musim. Secara umum, konsentrasi NO2 cenderung lebih tinggi pada **musim dingin** dan lebih rendah pada **musim panas**, dengan musim semi dan gugur berada di antara kedua musim tersebut. Pola ini dapat dijelaskan oleh peningkatan aktivitas pemanasan selama musim dingin, yang meningkatkan emisi NO2 dari sumber-sumber seperti pembakaran bahan bakar fosil.

        - **Variasi Terkecil di Stasiun Dongsi (17.46 μg/m³):**

            Stasiun pengukuran yang menunjukkan perbedaan tingkat NO2 terkecil antar musim adalah **Stasiun Dongsi**, dengan variasi sebesar **17.46 μg/m³**. Ini menunjukkan bahwa tingkat NO2 di Stasiun Dongsi relatif stabil sepanjang tahun, kemungkinan karena lokasinya di pusat kota yang lebih terkontrol dari segi sumber polusi atau dilindungi oleh struktur bangunan kota.

        - **Variasi Tertinggi di Stasiun Changping (24.96 μg/m³):**

            Sebaliknya, **Stasiun Changping** menunjukkan variasi musiman yang paling signifikan dengan perbedaan sebesar **24.96 μg/m³** antara musim dengan tingkat NO2 tertinggi dan terendah. Lokasi stasiun di daerah pinggiran kota mungkin lebih rentan terhadap fluktuasi polutan yang dipengaruhi oleh angin, suhu, dan aktivitas manusia yang berbeda antara musim.

        - **Faktor-faktor yang Mempengaruhi Distribusi Musiman:**

            Beberapa faktor yang mempengaruhi pola distribusi musiman NO2 meliputi kondisi meteorologi, seperti suhu, kelembapan, dan arah angin, serta pola aktivitas manusia yang berbeda di setiap musim, seperti pemanasan di musim dingin dan pendinginan di musim panas. Selain itu, karakteristik geografis dari lokasi stasiun juga mempengaruhi tingkat NO2 yang terukur.

        - **Kesimpulan:**

            Secara keseluruhan, stasiun di area perkotaan cenderung menunjukkan variasi musiman NO2 yang lebih kecil dibandingkan dengan stasiun di pinggiran kota, seperti Changping. Hal ini menunjukkan bahwa faktor lingkungan lokal dan aktivitas manusia berperan besar dalam mempengaruhi tingkat polutan di udara.
        """
    )
