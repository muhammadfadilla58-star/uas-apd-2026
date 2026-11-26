daftar_minuman = {
"minuman" : [
["sprite",  8000, 8],
["fanta",  7000, 10],
["coca cola", 9000, 9],
["ultra milk", 5000, 15],
["soya",  6000, 5]
]
}
def tambah_data(produk, harga, stok):
    if produk == "" or harga == "" or stok == "":
        print("Isi Tidak Boleh Kosong!")
        input("Tekan Enter Untuk Kembali...")
        return
    try:
        harga = int(harga)
        stok = int(stok)
        daftar_minuman["minuman"].append([produk, int(harga), int(stok)])
        print("Data Berhasil Ditambahkan!")
        input("Tekan Enter Untuk Kembali...")
    except ValueError:
        print("Silahkan Input Sesuai yang Diminta!")
        input("Tekan Enter Untuk Kembali...")
        return daftar_minuman