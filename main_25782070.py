from sensor_ops import generator
from tabulate import tabulate


def tampilkan_header():
    print("=" * 40)
    print("PROGRAM SMART ENVIRONMENT NODE".center(40))
    print("=" * 40)
    print("Nama : Irsan Anugrah")
    print("NPM  : 25782070")
    print("=" * 40)
    print()


def tampilkan_menu():
    print("Menu:")
    print("1. Baca Sensor Suhu")
    print("2. Baca Sensor Kelembapan")
    print("3. Keluar")


def main():
    tampilkan_header()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            suhu = generator.generate_temperature()
            data = [["Suhu", f"{suhu} °C"]]

            print("\nHasil:")
            print(tabulate(data, headers=["Jenis", "Nilai"], tablefmt="grid"))

        elif pilihan == "2":
            kelembapan = generator.generate_humidity()
            data = [["Kelembapan", f"{kelembapan} %"]]

            print("\nHasil:")
            print(tabulate(data, headers=["Jenis", "Nilai"], tablefmt="grid"))

        elif pilihan == "3":
            print("\nProgram selesai.")
            break

        else:
            print("\nPilihan tidak valid!")


if __name__ == "__main__":
    main()