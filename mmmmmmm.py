import csv
import os
from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta, date
import time
from  prettytable import  PrettyTable

#LOADING
def loading(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        time.sleep(0.5)
#DONE LOGIN
def menu_regislogin():
    os.system('cls')
    print(f'''
          
███╗░░░███╗░█████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░██████╗░████████╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗╚══██╔══╝
██╔████╔██║███████║██████╔╝███████║██╔████╔██║███████║██████╔╝░░░██║░░░
██║╚██╔╝██║██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗░░░██║░░░
██║░╚═╝░██║██║░░██║██║░░██║██║░░██║██║░╚═╝░██║██║░░██║██║░░██║░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
          ''')
    print(35 * "==")
    print(" Selamat Datang di MARAMART".center(70))
    print("1. Admin")
    print("2. Customer")
    pilihan = input("Admin/Customer[1/2] : ")
    if pilihan == "1":
        os.system('cls') 
        loading("Harap Tunggu")
        if pilihan == "1":
            os.system('cls')  
        if not Path('data_admint.csv').is_file():
            with open('data_admint.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['Username', 'Password'], delimiter=',') 
                header.writeheader()
                writer = csv.writer(filecsv)
                writer.writerow(['admin', '123'])
                    
        if not Path('datastok.csv').is_file():
            with open('datastok.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['nama', 'jenisbarang', 'harga', 'stok', 'expireddate'], delimiter=',') 
                header.writeheader()
        if not Path('riwayat_transaksi.csv').is_file():
            with open('riwayat_transaksi.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['Nama Barang', 'Jumlah', 'Harga', 'Total Harga'], delimiter=',')
                header.writeheader()

        os.system('cls')            
        print("========================================")
        print("Menuju Menu Login")
        print("\n========================================")
        loginadmint('data_admint')
    
    elif pilihan == "2":
            os.system('cls')
            print("A. Registrasi")
            print("B. Login")
            jawaban = str(input("Registrasi/Login[A/B] : ")).upper()
            if jawaban == "A" :
                os.system('cls')
                print("========================================")
                loading("Silahkan Registrasi")
                print('\n========================================')
                loading("Masuk ke menu Registrasi")
                if not(Path('data_customer.csv').is_file()):
                    with open('data_customer.csv', 'w', newline='') as filecsv:
                        header = csv.DictWriter(filecsv, fieldnames=['Username','Password'],  delimiter=',') 
                        header.writeheader()
                if not(Path('datastok.csv').is_file()):
                    with open('datastok.csv', 'w', newline='') as filecsv:
                        header = csv.DictWriter(filecsv, fieldnames=['nama','jenisbarang','harga','stok','expireddate'],  delimiter=',') 
                        header.writeheader()
                username= (input("\nMasukkan username = "))
                kondisi = False
                data = []
        
                with open('data_customer.csv', 'r') as file:
                    csv_user = csv.reader(file, delimiter=',')
                    for row in csv_user:
                        data.append({'username': row[0]})
        
                for row in data:
                    if row['username'] == username:
                        kondisi = True
                        break
            
                if kondisi:
                    os.system('cls')
                    print("========================================")
                    print("Username sudah terdaftar")
                    print("Silahkan registrasi dengan username lain")
                    print("\n========================================")
                    loading("Kembali ke menu registrasi")
        
                else:
                    password= (input("Masukkan password = "))
                    with open('data_customer.csv', 'a', newline='') as file:
                        csv_user = csv.writer(file, delimiter=',')
                        csv_user.writerow([username,password])
                        file.close()
                
                    print("========================================")
                    loading("Registrasi Berhasil")
                    os.system('cls')
                    loading("Masuk ke menu login")
                    logincustomer()
            elif jawaban == "B" :
                print("\n========================================")
                loading("Masuk Ke Menu Login")
                logincustomer()
            else: print("Pilihan tidak tersedia")
    else:
        menu_regislogin()

#FITUR BLOM KELAR
def loginadmint(data_admint):
    os.system('cls')
    print("========================================")
    print("Silahkan Login")
    print("========================================")
    username= (input(" Masukkan username = "))
    password= (input(" Masukkan password = "))
    kondisi = False
    data = []
    
    with open('data_admint.csv', 'r') as file:
        data_admint = csv.reader(file, delimiter=',')
        for row in data_admint:
            data.append({'username': row[0],'password': row[1]})
        print(data)

    for row in data:
        if row['username'] == username and row['password'] == password :
            kondisi = True
            break
    if kondisi == True:
        menu_admin()    
        
    if not kondisi:
        os.system('cls')
        print("========================================")
        print("Kamu Bukan Admint")
        print("========================================")
        loading("Kembali ke menu login")
        loginadmint('data_admint')
    else:
        os.system('cls')
        print("========================================")
        print("Login Berhasil")
        os.system('cls')
        loading("Selamat Datang Admint")
        os.system('cls')
        menu_admin()
        
def logincustomer():
    os.system('cls')
    print("========================================")
    print("Silahkan Login")
    print("========================================")
    username= (input(" Masukkan username = "))
    password= (input(" Masukkan password = "))
    kondisi = False
    data = []
    
    with open('data_customer.csv', 'r') as file:
        data_customer = csv.reader(file, delimiter=',')
        for row in data_customer:
            data.append({'username': row[0], 'password': row[1]})
        print(data_customer)
    
    for row in data:
        if row['username'] == username and row['password'] == password:
            kondisi = True
            break
        
    if not kondisi:
        os.system('cls')
        print("========================================")
        print("Kamu Bukan Customer")
        print("========================================")
        loading("Kembali ke menu login")
        logincustomer()
    else:
        os.system('cls')
        print("========================================")
        print("Login Berhasil")
        os.system('cls')
        loading("Selamat Datang Customer")
        os.system('cls')
        menu_customer()

def menu_admin():
    os.system('cls')
    info_exp = False
    data_exp = []
    with open('datastok.csv', 'r') as file:
        datastok = csv.reader(file, delimiter=',')
        for row in datastok:
            strTgl = str(datetime.now().date())
            if row[4] < strTgl:
                data_exp.append({
                    'nama': row[0],'jenisbarang': row[1],'harga': row[2],'stok': row[3], 'expireddate': row[4]})
                data_exp.remove(data_exp[0])
                dp = pd.DataFrame(data_exp)
                dp.index = range(1, len(dp)+1)
                
            else:
                 if not info_exp: 
                     data_exp.append({'Informasi produk expired':'Tidak ada produk expired'})
                     info_exp = True
                     dp = pd.DataFrame(data_exp)
                     dp.index = range(1, len(dp)+1)
        if data_exp:
            print("Informasi produk expired")
            print(dp)
            print('\n')
        else:
            print("Tidak ada produk expired")
            print('\n')
    print("========================================")
    print("Hallo Admin MARAMART")
    print("========================================")
    print("1. Cek Stock")
    print("2. Transaksi") #cek transaksi
    print("3. Keluar") 
    print("========================================")
    

    pilihan = input("Pilih Menu [1/2/3]: ")
    if pilihan == "1":
        cek_stok()
    if pilihan == "2":
        riwayat_transaksi()
    if pilihan == "3":
        menu_regislogin()
    else :
        loginadmint('data_admint')

#admin pake _       
def cek_stok():
    while True:
        os.system('cls')
        print("===Kamu Mau Apa Admint===")
        print("1. Re-Stock")
        print("2. Lihat Stock")
        print("3. Hapus Stock")
        print("4. Kembali")
        pilihan = input("Pilih Menu [1/2/3/4] :")
        if pilihan == "1" :
            stoklagi()
        elif pilihan == "2" :
            lihat_stok ()
        elif pilihan == "3" :
            hapus_barang()
        elif pilihan == "4" :
            menu_admin()
        else:
            menu_regislogin()

def stoklagi():
    os.system('cls')
    with open('datastok.csv', 'a', newline='') as file:
        tambah = csv.writer(file, delimiter=',')
        nama = input("Masukkan Nama Produk: ")
        jenisProduk = input("Masukkan Jenis Produk: ")
        harga = input("Masukkan Harga Produk: ")
        stok = input("Masukkan Stok Produk: ")
        inputan = int(input("Masukan Berapa Hari Expired: "))
        hari = datetime.now().date()
        expireddate = hari + timedelta(days=inputan)
        tambah.writerow([nama,jenisProduk,harga,stok,expireddate,])
        file.close()
        loading("Menambahkan Data")
        os.system('cls')
        print("Data berhasil ditambahkan!")
        input("Tekan Enter untuk kembali ke menu")

def lihat_stok():
    os.system('cls')
    loading("OTW MENAMPILKAN STOK")
    os.system('cls')
    tampilkanstoknya()
    df = pd.read_csv('datastok.csv')
    while True:
        pilihan = input('Ada yang ingin dicari ketik 1(tekan 0 untuk kembali) : ')
        if pilihan == "1":
            nama = input("Masukkan Nama Produk yang ingin dicari: ")
            cari = pd.read_csv('datastok.csv')
            cari_nama = nama
            hasil = cari[cari['nama'].str.contains(cari_nama, na=False)]
            hasil.index = range(1, len(hasil)+1)
            print(hasil)
        elif pilihan == "0":
            cek_stok()
        else: 
            menu_admin()


def hapus_barang():
    print('DATA STOK')
    stok = pd.read_csv('datastok.csv')
    print(stok)
    nama_barang = input("Masukkan nama Barang yang mau dihapus: (tekan enter untuk kembali)")
    if nama_barang in stok['nama'].values:
        stok = stok[stok['nama'] != nama_barang]
        stok.to_csv('datastok.csv', index=False)
        print('Nama Barang berhasil dihapus')
    else:
        print("Nama Barang tidak ditemukan")

def tampilkanstoknya():
    datastok = pd.read_csv('datastok.csv')      
    datastok.index = range(1, len(datastok)+1)
    tabel = PrettyTable()
    tabel.field_names = datastok.columns.tolist()
    for i in datastok.values:
        tabel.add_row(i)
    print(tabel)

def riwayat_transaksi():
    os.system('cls')
    print("\n=== RIWAYAT TRANSAKSI ===")
    
    try:
        with open('riwayat_transaksi.csv', 'r') as filecsv:
            reader = csv.DictReader(filecsv)
            tabel = PrettyTable()
            tabel.field_names = ['nama', 'jenisbarang', 'jumlah', 'harga_satuan', 'total']
            
            for row in reader:
                if all(key in row for key in ['nama', 'jenisbarang', 'jumlah', 'harga_satuan', 'total']):
                    tabel.add_row([row['nama'], row['jenisbarang'], row['jumlah'], row['harga_satuan'], row['total']])
                else:
                    print("Data tidak lengkap dalam baris:", row)
            
            print(tabel)
    except FileNotFoundError:
        print("Riwayat transaksi tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    
    input("\nTekan Enter untuk kembali...")
    menu_admin()

def menu_customer():
    os.system('cls')
    print("========================================")
    print("Selamat Datang di MARAMART")
    print("========================================")
    print("1. List Barang")
    print("2. Transaksi") #cek transaksi
    print("3. Keluar") 

    pilihan = input("Pilih Menu [1/2/3]: ")
    if pilihan == "1":
        lihat_stokc()
    if pilihan == "2":
        transaksi()
    if pilihan == "3":
        menu_regislogin()
    else :
        menu_regislogin()




def lihat_stokc():
    os.system('cls')
    loading("OTW MENAMPILKAN STOK")
    os.system('cls')
    tampilkanstoknya()
    df = pd.read_csv('datastok.csv')
    while True:
        pilihan = input('Ada yang ingin dicari ketik 1(tekan 0 untuk kembali): ')
        if pilihan == "1":
            nama = input("Masukkan Nama Produk yang ingin dicari: ")
            cari = pd.read_csv('datastok.csv')
            cari_nama = nama
            hasil = cari[cari['nama'].str.contains(cari_nama, na=False)]
            hasil.index = range(1, len(hasil)+1)
            print(hasil)
        elif pilihan == "0":
            menu_customer()

def tampilkan_stok():
    datastok = pd.read_csv('datastok.csv')      
    datastok.index = range(1, len(datastok)+1)
    tabel = PrettyTable()
    tabel.field_names = datastok.columns.tolist()
    for i in datastok.values:
        tabel.add_row(i)
    print(tabel)

def tambah_barang():
    global stok, pembelian, total_harga  
    while True:
        nama_barang = input("Apakah Anda ingin menambahkan barang? (masukkan nama barang atau ketik 'selesai' untuk menyelesaikan): ")
        
        if nama_barang.lower() == 'selesai':
            break
        
        barang = stok[stok['nama'].str.contains(nama_barang, case=False, na=False)]
        
        if barang.empty:
            print("Barang tidak ditemukan.")
            continue

        print("Barang yang ditemukan:")
        print(barang)

        try:
            jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        
        if jumlah > barang['stok'].values[0]:
            print("Stok tidak cukup.")
            continue

        harga_satuan = barang['harga'].values[0]
        total_harga += harga_satuan * jumlah

        pembelian.append({
            'nama': barang['nama'].values[0],
            'jenisbarang': barang['jenisbarang'].values[0],
            'jumlah': jumlah,
            'harga_satuan': harga_satuan,
            'total': harga_satuan * jumlah
        })

        stok.loc[stok['nama'] == barang['nama'].values[0], 'stok'] -= jumlah

def cetak_struk():
    os.system('cls')
    if pembelian:
        print('\n===================================')
        print("Struk Pembelian:")
        for item in pembelian:
            print(f"Nama Barang       : {item['nama']}")
            print(f"Jenis Barang      : {item['jenisbarang']}")
            print(f"Jumlah            : {item['jumlah']}")
            print(f"Harga Satuan      : Rp {item['harga_satuan']}")
            print(f"Total Harga       : Rp {item['total']}")
            print('-----------------------------------')
        print(f" Total Keseluruhan  : Rp {total_harga}")
        print('===================================')
    else:
        print("Tidak ada barang yang dibeli.")

def simpan_riwayat():
    df_pembelian = pd.DataFrame(pembelian)
    total_df = pd.DataFrame([{'nama': 'Total Keseluruhan', 'jumlah': '', 'harga_satuan': '', 'total': total_harga}])
    df_riwayat = pd.concat([df_pembelian, total_df], ignore_index=True)

    df_riwayat.to_csv('riwayat_transaksi.csv', mode='a', header=not os.path.exists('riwayat_transaksi.csv'), index=False)

def transaksi():
    global stok, pembelian, total_harga  
    os.system('cls')
    print("========================================")
    print("Silahkan Melakukan Pembayaran")
    print("========================================")
    
    try:
        stok = pd.read_csv('datastok.csv')
    except FileNotFoundError:
        print("Data stok tidak ditemukan.")
        return

    tampilkan_stok()

    pembelian = []
    total_harga = 0

    tambah_barang()

    cetak_struk()

    if pembelian:
        simpan_riwayat()
        stok.to_csv('datastok.csv', index=False)
        print("Transaksi berhasil!")
        
    input("Tekan Enter untuk kembali ke menu")
    os.system('cls')
    menu_customer()

if __name__ == "__main__":
    menu_regislogin()
    
