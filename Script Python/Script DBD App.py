
import pandas as pd

def baca_dan_gabungkan_data():
    # Load data dari file
    health = pd.read_excel("Health_Data_Jakarta_Selatan.xlsx")
    iot = pd.read_excel("Data_IoT_Sensor_DBD.xlsx")
    crowdsourced = pd.read_csv("Data_Crowdsourced_DBD.csv")
    weather = pd.read_excel("Data_Cuaca_Jakarta_Selatan.xlsx")

    # Konversi kolom tanggal ke format datetime
    health['Tanggal'] = pd.to_datetime(health['Tanggal'])
    iot['Tanggal'] = pd.to_datetime(iot['Tanggal'])
    crowdsourced['Tanggal'] = pd.to_datetime(crowdsourced['Tanggal'])
    weather['Tanggal'] = pd.to_datetime(weather['Tanggal'])

    # Gabungkan data berdasarkan kolom Tanggal
    data = pd.merge(health, iot, on='Tanggal', how='outer')
    data = pd.merge(data, crowdsourced, on='Tanggal', how='outer')
    data = pd.merge(data, weather, on='Tanggal', how='outer')

    return data

def deteksi_potensi_dbd(data):
    # Tambahkan logika deteksi sederhana (ubah nama kolom sesuai data asli)
    data['Potensi_DBD'] = (
        (data['Suhu'] > 29) &
        (data['Kelembaban'] > 80) &
        (data['Jumlah_Jentik'] > 10) &
        (data['Laporan_DB'] > 5)
    )
    return data

def simpan_hasil(data):
    data.to_excel("Hasil_Deteksi_Potensi_DBD.xlsx", index=False)
    print("Deteksi selesai. Hasil disimpan dalam 'Hasil_Deteksi_Potensi_DBD.xlsx'")

def main():
    data = baca_dan_gabungkan_data()
    hasil = deteksi_potensi_dbd(data)
    simpan_hasil(hasil)

if __name__ == "__main__":
    main()
