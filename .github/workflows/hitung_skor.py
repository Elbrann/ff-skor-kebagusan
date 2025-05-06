import pandas as pd

# Fungsi untuk menghitung skor
def hitung_skor(input_file, output_file):
    # Membaca data dari file Excel
    df = pd.read_excel(input_file)

    # Tentukan poin berdasarkan peringkat
    placement_points = {1: 12, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}
    
    # Menambahkan kolom untuk total poin
    df['Placement Points'] = df['Rank'].map(placement_points)
    df['Total Points'] = df['Placement Points'] + df['Kills']

    # Menyimpan hasil perhitungan ke file output
    df.to_excel(output_file, index=False)

# Menjalankan fungsi
input_file = 'Template_Skor_Turnamen_FF.xlsx'  # Ganti dengan path file yang tepat
output_file = 'Hasil_Skor_Turnamen_FF.xlsx'   # Ganti dengan path file output

hitung_skor(input_file, output_file)
