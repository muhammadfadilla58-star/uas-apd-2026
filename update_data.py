from create_data import daftar_minuman
daftar_minuman = daftar_minuman
def update_data():
    print("Apa yang Igin Anda Update?")
    print("1. Harga Barang")
    print("2. Stok Barang")
    pilihan = input("Masukkan Pilihan Anda: ")
    if pilihan == "1":
        indeks = input("Masukkan Indeks Minuman yang Ingin di Ganti: ")
        try:
            indeks = int(indeks)
            try:
                indeks < len(daftar_minuman["minuman"])
                try:
                    harga_baru = input("Masukkan Harga Baru: ")
                    harga_baru = int(harga_baru)
                    daftar_minuman["minuman"][indeks][1] = int(harga_baru)
                    print("Harga Baru Berhasil Ditambahkan!")
                    input("Tekan Enter Untuk Kembali...")
                except ValueError:
                    print("Hanya Menerima Input Angka!")
                input("Tekan Enter Untuk Kembali...")
            except IndexError:
                print("Jangkauan Tidak Tersedia!")
                input("Tekan Enter Untuk Kembali...")
        except ValueError:
            print("Hanya Menerima Input Angka!")
            input("Tekan Enter Untuk Kembali...")
        return daftar_minuman        
    elif pilihan == "2":
        indeks = input("Masukkan Indeks yang Ingin di Ganti: ")
        try:
            indeks = int(indeks)
            try:
                indeks < len(daftar_minuman["minuman"])
                try:
                    stok_baru = input("Masukkan Stok Baru: ")
                    stok_baru = int(stok_baru)
                    daftar_minuman["minuman"][indeks][2] = int(stok_baru)
                    print("Stok Baru Berhasil Ditambahkan!")
                    input("Tekan Enter Untuk Kembali...")
                except ValueError:
                    print("Hanya Menerima Input Angka!")
                    input("Tekan Enter Untuk Kembali...")    
            except IndexError:
                print("Jangkauan Tidak Tersedia!")
                input("Tekan Enter Untuk Kembali...")   
        except ValueError:
            print("Hanya Menerima Input Angka!")
            input("Tekan Enter Untuk Kembali...")    
    else:
        print("pilihan Tidak Valid!")
        input("Tekan Enter Untuk Kembali...")
    return daftar_minuman