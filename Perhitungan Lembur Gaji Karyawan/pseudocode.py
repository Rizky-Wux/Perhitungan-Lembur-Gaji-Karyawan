# Fungsi untuk menghitung gaji karyawan
def hitung_gaji(golongan, jam_lembur):
    
    # Inisialisasi Gaji Pokok
    if golongan == 'A':
        gaji_pokok = 5000000
    elif golongan == 'B':
        gaji_pokok = 6500000
    elif golongan == 'C':
        gaji_pokok = 9500000
    else:
        return "Golongan tidak valid!"

    # Inisialisasi Gaji Lembur
    if jam_lembur == 1:
        gaji_lembur = 0.30 * gaji_pokok
    elif jam_lembur == 2:
        gaji_lembur = 0.32 * gaji_pokok
    elif jam_lembur == 3:
        gaji_lembur = 0.34 * gaji_pokok
    elif jam_lembur == 4:
        gaji_lembur = 0.36 * gaji_pokok
    elif jam_lembur >= 5:
        gaji_lembur = 0.38 * gaji_pokok
    else:
        gaji_lembur = 0 # tidak ada gaji lembur jika jam lembur kurang dari 1

    # Hitung total penghasilan
    jumlah_penghasilan = gaji_pokok + gaji_lembur
    return jumlah_penghasilan

# Program Utama
if __name__ == "__main__":
    golongan = input("Masukkan Golongan Karyawan (A/B/C): ")
    jam_lembur = int(input("Masukkan Jam Lembur: "))

    total_penghasilan = hitung_gaji(golongan.upper(), jam_lembur)

    if isinstance(total_penghasilan, str):
        print(total_penghasilan)
    else:
        print(f"Jumlah Penghasilan: Rp {total_penghasilan:,.0f}")