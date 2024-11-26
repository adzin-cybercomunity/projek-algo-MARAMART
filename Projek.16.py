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
    print("========================================")
    print(" Selamat Datang di MARAMART")
    print("1. Admin")
    print("2. Customer")
    pilihan = input("Admin/Customer[1/2] : ")
    if pilihan == "1":
        os.system('cls')
        print("A. Registrasi")
        print("B. Login")
        jawaban = str(input("Registrasi/Login[A/B] : ")).upper()
        if jawaban == "A" :
            print("========================================")
            loading("Silahkan Registrasi")
            print('\n========================================')
            loading("Masuk ke menu Registrasi")
            if not(Path('data_admint.csv').is_file()):
                with open('data_admint.csv', 'w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=['Username','Password'],  delimiter=',') 
                    header.writeheader()
            if not(Path('datastok.csv').is_file()):
                with open('datastok.csv', 'w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=['nama','jenisbarang','harga','stok','expireddate'],  delimiter=',') 
                    header.writeheader()
            username= (input("\nMasukkan username = "))
            kondisi = False
            data = []
        
            with open('data_admint.csv', 'r') as file:
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
                print("========================================")
                loading("Kembali ke menu registrasi")
        
            else:
                password= (input("Masukkan password = "))
                with open('data_admint.csv', 'a', newline='') as file:
                    csv_user = csv.writer(file, delimiter=',')
                    csv_user.writerow([username,password,aktor])
                    file.close()
                
            print("========================================")
            loading("Registrasi Berhasil")
            os.system('cls')
            loading("Masuk ke menu login")
            loginadmint()
        elif jawaban == "B" :
            print("========================================")
            loading("Menuju Menu Login")
            print("\n========================================")
            loading("Masuk Ke Menu Login")
            loginadmint('data_awal')
        else:
            print("Pilihan tidak tersedia")

            
    elif pilihan == "2":
            os.system('cls')
            print("A. Registrasi")
            print("B. Login")
            jawaban = str(input("Registrasi/Login[A/B] : "))
            if jawaban == "A" :
                os.system('cls')
                print("\n========================================")
                loading("Silahkan Registrasi")
                print('\n========================================')
                loading("Masuk ke Registrasi")
                if not(Path('data_customer.csv').is_file()):
                    with open('data_customer.csv', 'w', newline='') as filecsv:
                        header = csv.DictWriter(filecsv, fieldnames=['Username','Password', 'aktor'],  delimiter=',') 
                        header.writeheader()
                if not(Path('datastok.csv').is_file()):
                    with open('datastok.csv', 'w', newline='') as filecsv:
                        header = csv.DictWriter(filecsv, fieldnames=[
                            'nama','jenisbarang','harga','stok','expireddate'
                            ],  delimiter=',') 
                        header.writeheader()
                aktor = 'Customer' 
                username= (input("Masukkan username = "))
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
                    password= (input("\nMasukkan password = "))
                    with open('data_customer.csv', 'a', newline='') as file:
                        csv_user = csv.writer(file, delimiter=',')
                        csv_user.writerow([username,password,aktor])
                        file.close()
                
                    print("========================================")
                    loading("Registrasi Berhasil")
                    os.system('cls')
                    loading("Masuk ke menu login")
                    logincustomer()
            elif jawaban == "B" :
                print("\n========================================")
                loading("Username Sudah Ada")
                print("\n========================================")
                loading("Masuk Ke Menu Login")
                logincustomer()
            else: print("Pilihan tidak tersedia")
    else:
        print("Pilihan tidak tersedia")

def dataadmint(data_admint): 
    data_awal = [
        {"username": "admin", "password": "12345"}]
    with open(data_admint, mode='w', newline='') as file:
        fieldnames = ["username", "password"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_awal)
    print(f"File '{data_admint}' berhasil dibuat.")

def datasadmint(data_admint):
    """Membaca data username dan password dari file CSV."""
    data_admint = {}
    try:
        with open(data_admint, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_admint[row['username']] = row['password']
    except FileNotFoundError:
        print(f"File '{data_admint}' tidak ditemukan.")
    return data_admint

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
    print("========================================")
    print("Selamat Datang di MARAMART")
    print("========================================")
    print("1. Cek Stock")
    print("2. Transaksi") #cek transaksi
    print("3. Keluar") 
    print("========================================")
    info_exp = False
    data_exp = []
    with open('datastok.csv', 'r') as file:
        datastok = csv.reader(file, delimiter=',')
        for row in datastok:
            strTgl = str(datetime.now().date())
            if row[4] < strTgl:
                data_exp.append({
                    'nama': row[0],'jenisbarang': row[1],'harga': row[2],'stok': row[3], 
                    'expireddate': row[4], 'expireddate': row[5]})
                data_exp.remove(data_exp[0])
                dp = pd.DataFrame(data_exp)
                dp.index = range(1, len(dp)+1)
                
                
            else:
                if not info_exp: 
                    data_exp.append({'Informasi produk expired':'Tidak ada produk expired'})
                    info_exp = True
                    dp = pd.DataFrame(data_exp)
                    dp.index = range(1, len(dp)+1)
    print(dp)

    pilihan = input("Pilih Menu [1/2/3]: ")
    if pilihan == "1":
        cek_stok()
    if pilihan == "2":
        transaksi()
    if pilihan == "3":
        exit()

#admin pake _       
def cek_stok():
    os.system('cls')
    print("===Kamu Mau Apa Admint===")
    print("1. Re-Stock")
    print("2. Lihat Stock")
    print("3. Hapus Stock")
    print("4. Kembali")
    pilihan = input("Pilih Menu [1/2/3/4] :")
    if pilihan == "1" :
        restok()
    if pilihan == "2" :
        lihat_stok ()
    if pilihan == "3" :
        hapusdata()
    if pilihan == "4" :
        menu_admin()


def tampilkanstoknya():
    datastok = pd.read_csv('datastok.csv')      
    datastok.index = range(1, len(datastok)+1)
    tabel = PrettyTable()
    tabel.field_names = datastok.columns.tolist()
    for i in datastok.values:
        tabel.add_row(i)
    print(tabel)

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
        cekstok()
    if pilihan == "2":
        transaksi()
    if pilihan == "3":
        exit()

def cekstok():
    os.system('cls')
    print("===Halo Pelanggan===")
    print("1. Lihat Stock")
    print("2. Beli Barang")
    print("3. Hapus Barang")
    print("4. Kembali")
    pilihan = input("Pilih Menu [1/2/3/4] :")
    if pilihan == "1" :
        lihat_stok()
    if pilihan == "2" :
        lihat_stok ()
    if pilihan == "3" :
        hapusdata()
    if pilihan == "4" :
        menu_admin()

def lihat_stok():
    os.system('cls')
    loading("OTW MENAMPILKAN STOK")
    os.system('cls')
    tampilkanstoknya()
    df = pd.read_csv('datastok.csv')
    pilihan = input('Ada yang ingin dicari ketik 1(tekan 0 untuk kembali): ')
    if pilihan == "1":
        nama = input("Masukkan Nama Produk yang ingin dicari: ")
        cari = pd.read_csv('datastok.csv')
        cari_nama = nama
        hasil = cari[cari['nama'].str.contains(cari_nama, na=False)]
        hasil.index = range(1, len(hasil)+1)
        print(hasil)
    elif pilihan == "0":
        cekstok()

if __name__ == "__main__":
    menu_regislogin()
    # tes