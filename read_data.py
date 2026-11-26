import inquirer
from prettytable import PrettyTable
from create_data import daftar_minuman
daftar_minuman = daftar_minuman


def baca_data():
    pertanyaan = [
        inquirer.List(
            "pengurutan",
            message="Pilih Pengurutan Daftar Minuman",
            choices=["Urutan Awal", "Sorting Alfabet", "Sorting Harga"],
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return

    minuman_list = daftar_minuman["minuman"]
    if jawaban["pengurutan"] == "Sorting Alfabet":
        minuman_list = sorted(minuman_list, key=lambda minuman: minuman[0].casefold())
    elif jawaban["pengurutan"] == "Sorting Harga":
        minuman_list = sorted(minuman_list, key=lambda minuman: minuman[1], reverse=True)

    print("\n=======DAFTAR MINUMAN=======")
    tabel = PrettyTable()
    tabel.field_names = ["Nama Minuman", "Harga", "Stok"]
    for minuman in minuman_list:
        tabel.add_row([
            minuman[0],
            minuman[1],
            minuman[2]
        ])
    tabel.align["Nama Minuman"] = "l"
    print(tabel)
    input("Tekan Enter Untuk Kembali...")
