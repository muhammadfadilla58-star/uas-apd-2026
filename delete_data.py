from create_data import daftar_minuman
daftar_minuman = daftar_minuman
def hapus_data(hapus):
    try:
        hapus = int(hapus)
        try:
            hapus < len(daftar_minuman["minuman"])
            del daftar_minuman["minuman"][hapus]
            print("Data Berhasil Dihapus!")
            input("Tekan Enter Untuk Kembali...")
            return daftar_minuman
        except IndexError:
            print("Jangkauan Tidak Tersedia!")
            input("Tekan Enter Untuk Kembali...")                              
    except ValueError:
        print("Hanya Menerima Input Angka!")
        input("Tekan Enter Untuk Kembali...")