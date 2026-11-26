import os
import inquirer
from daftar_minuman import tampilkan_daftar_minuman
from create_data import tambah_data
from update_data import update_data
from read_data import baca_data
from delete_data import hapus_data
akun = {
"akun" : [
]
}
daftar_minuman = {
"minuman" : [
["sprite",  8000, 8],
["fanta",  7000, 10],
["coca cola", 9000, 9],
["ultra milk", 5000, 15],
["soya",  6000, 5]
]
}
apd = 0
def menu_utama():
    pertanyaan = [
        inquirer.List(
            "menu", 
            message="Pilih Menu", 
            choices=["Login", "Registrasi", "Exit"],
            )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]
    
def menu_admin():
    pertanyaan = [
        inquirer.List(
            "menu",
            message="Pilih Menu",
            choices=["Tambah Daftar Minuman Baru", "Tampilkan Daftar Minuman", "Update Barang", "Hapus Daftar Minuman", "Exit"]
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]
def menu_pengguna():
    pertanyaan = [
        inquirer.List(
            "menu",
            message="Pilih Menu",
            choices=["Tampilkan Daftar Minuman", "Exit"]
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]
while True:
    os.system("cls")
    pilihan = menu_utama()
    if pilihan == "Login":
        akun_valid = False
        username = str(input("Masukkan Username Anda: "))
        password = str(input("Masukkan Password Anda: "))
        for i in akun["akun"]:
            if  i[0] == username and i[1] == password:
                akun_valid = True
                role = i[2] 
        if akun_valid == False:
            print("Username atau Password Anda Salah!")
            input("Tekan Enter Untuk Kembali...")
        elif role == "admin":
            print("======LOGIN BERHASIL!=====")
            print("Selamat Datang, Admin")
            input("Tekan Enter Untuk Melanjutkan...")
            while True:
                os.system("cls")
                tampilkan_daftar_minuman()
                pilihan = menu_admin()   
                if pilihan == "Tambah Daftar Minuman Baru":
                    produk = input("Tambahkan Daftar Minuman: ").strip()
                    harga = input("Tambahkan Harga: ")
                    stok = input("Tambahkan Stok: ")
                    tambah_data(produk, harga, stok )
                elif pilihan == "Tampilkan Daftar Minuman":
                    baca_data()
                elif pilihan == "Update Barang":
                    update_data()
                elif pilihan == "Hapus Daftar Minuman":
                    hapus = input("Data Mana yang Ingin Anda Hapus: ")
                    hapus_data(hapus)
                elif pilihan == "Exit":
                    print("Terima kasih!")
                    input("Tekan Enter Untuk Kembali...")
                    break
                else:
                    print("Pilihan Tidak Valid!")
                    input("Tekan Enter Untuk Kembali...")
        elif role == "pengguna":
            while True:
                os.system("cls")
                pilihan = menu_pengguna()
                if pilihan == "Tampilkan Daftar Minuman":
                    tabel = baca_data()
                    print(tabel)
                elif pilihan == "Exit":
                    print("Terima kasih!")
                    break
                else:
                    print("Pilihan Tidak Valid!")
                    input("Tekan Enter Untuk Kembali...")
        else:
            print("Role Tidak Tersedia!")
            input("Tekan Enter Untuk Kembali...")
    elif pilihan == "Registrasi":
        x = True
        username = str(input("Masukkan Username Anda: ")).strip()
        password = str(input("MasukkanPassword Anda: ")).strip()
        role = str(input("Masukkan Role Anda: ")).lower().strip()
        for i in akun["akun"]:
            if i[0] == username or i[1] == password:
                print("Username atau Password Tersebut Telah Digunakan!")
                x = False
                input("Tekan Enter Untuk Kembali...")
                break
        if username == "" or password == "" or role == "":
            print("Username, Password, atau role Tidak Boleh Kosong!")
            input("Tekan Enter Untuk Kembali...")
        elif x == True:
            akun["akun"].append([username, password, role])
            print("Registrasi Berhasil!")
            input("Tekan Enter Untuk Kembali...")
    elif pilihan == "Exit":
        print("Terima Kasih Telah Menggunakan Aplikasi Manajemen Stok Minuman!")
        break
    else:
        print("Pilihan Tidak Tersedia!")
        input("Tekan Enter untuk Kembali...")