# Belajar Analisis Data dengan Python
Proyek ini bertujuan untuk membangun dashboard interaktif yang memungkinkan pengguna menganalisis dan memvisualisasikan data kualitas udara, sehingga memudahkan eksplorasi tren serta pola polusi dengan lebih efektif.

# Noted
This repository only use to deploy [Streamlit.app](https://airqualitydataset-daniel.streamlit.app/)

If you run in your pc, you should change the directory of read.csv(data) to the correct directory.

If you want to deploy to a streamlit, you should change the directory of read.csv(data) to the correct directory and make the clean merged dataset from usual to url by create the Releases(Github) and then copy the link and change teh code from:

   df = pd.read_csv("clean_merged_dataset.csv")

to:

    url = "https://github.com/DanielRidho/AirQualityDataset/releases/download/v1.0.0/clean_merged_dataset.csv"
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')

Or, you can search the different by see on my [repository](https://github.com/DanielRidho/AirQualityDataset)

The zip file that I sent in the Dicoding project submission is code that can be run on a local computer.

# Dataset
Find the Air Quality Dataset in [Air Quality Dataset](https://github.com/marceloreis/HTI/tree/master)

## Setup environment

- Install Visual Studio Code for Better Code Editor
- Execute this command on command line (as administrator prefered)

```
pip install numpy pandas scipy matplotlib seaborn jupyter
```

## Project installation

The steps to create your virtual environment from this project is as follows:

1. Clone this repository

   ```
   git clone https://github.com/anndeviant/analisis-data_airquality.git
   ```

2. Move to directory dicoding-airquality/
   ```
   cd analisis-data_airquality
   ```
3. Move to directory dashboard/
   ```
   cd dashboard
   ```
5. Run streamlit app
   ```
   streamlit run dashboard.py
   ```
6. Stop the application in terminal by
   ```
   ctrl + c
   ```
