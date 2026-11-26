from prettytable import PrettyTable
from create_data import daftar_minuman
daftar_minuman = daftar_minuman
def tampilkan_daftar_minuman():
    tabel = PrettyTable()
    tabel.field_names = ["Nama Minuman", "Harga", "Stok"]
    for minuman in daftar_minuman["minuman"]:
        tabel.add_row([
        minuman[0],
        minuman[1],
        minuman[2]
        ])
    tabel.align["Nama Minuman"] = "l"
    print(tabel)