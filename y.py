# print("|===================================|")
# print("|      Menamppilkan Kalender        |")
# print("|===================================|")

# import calendar

# tahun = int(input("Masukan Tahun: "))
# bulan = int(input("Masukan Bulan: "))
# print()

# print("hasil")
# print(calendar.month(tahun, bulan))

import os 

uang_saya = 0 

while True: 
    os.system("cls")
    print("\nSELAMAT DATANG")
    print("PILIH MENU")
    print("1. cek uang")
    print("2. ambil uang saya")
    print("3. tabung uang saya")

    option = int(input("silahkan pilih menu:"))
    if option == 1:
        print("uang kamu: ", uang_saya)
    elif option == 2:
        print("uang kamu: ",uang_saya)
        uang_ambil = int(input("Masukkan Jumlah Uang"))
        if (uang_saya - uang_ambil) < 0:
            print("tidak cukup uang")
        else:
            uang_saya -= uang_ambil
            print("berhasil diambil: ", uang_ambil)
            print("uang kamu sekarang: ", uang_saya)
    elif option == 3:
        print("uang kamu: ", uang_ambil)
        uang_tabung = int(input("masukkan jumlah uang"))
        uang_saya += uang_tabung
        print("berhasil ditabung: ", uang_tabung)
        print("uang kamu sekarang: ", uang_saya)

    lanjut = input("lanjut transaksi ? (no/yes) : ")
    if lanjut == "no":
        print("\nTerima kasih telah bertransaksi")
        print(int(input("Berika rating")))
