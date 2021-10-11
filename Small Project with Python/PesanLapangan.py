import os #Modul portabel tergantung sistem operasi
from time import sleep #import sleep dari time

loop = True # Pengulangan didepan

while loop:
    def menu():     #Memulai fungsi dan bisa digunakan kembali
        print("="*10)
        print("Pesan Lapangan Futsal Online")
        print("="*10)
        print("pilih Tipe Lapangan! ")
        print("-"*10)
        print("1.   Karpet")
        print("2.   Rumput")
        print("3.   Semen")
        print("4.   EXIT")
        print("-"*10)

    def pesan():    #Memulai fungsi dan bisa digunakan kembali
        jmlh = int(input("Mau main berapa jam ?   : "))
        org = input("Pesanan atas nama  :  ")
        total_hrg = jmlh * harga
        os.system('cls')
        print("-"*10)
        print("Lapangan telah dipesan!")
        print("Atas nama   : ", org)
        print("Total Harga : ", "Rp", total_hrg)
        sleep(2)
    
    menu()
    tipe = int(input("Pilih Tipe Lapangan  :   "))

    if ((tipe) == 1):
        print("-"*15)
        print("\nNomor    Nama\tTipe\tHarga per Jam")
        print("-"*15)
        print("\n101.   Damar\tKarpet \tRp. 150,000")
        print("\n102.   Bangkit\tKarpet \tRp. 150,000")
        print("-"*20)
        no_lpg = int(input("Masukkan No lapangan   :   "))

        if ((no_lpg) == 101):
            harga = 150000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        elif ((no_lpg) == 102):
            harga = 150000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        else:
            print("\t   Yahh lapangan Belum tersedia di tempat kami, semoga kedepan nya ada yaa!")
            sleep(3)
            os.system('cls')

    elif((tipe) == 2):
        print("-"*15)
        print("\nNomor    Nama\tTipe\tHarga per Jam")
        print("-"*15)
        print("\n201.   Karang\tRumput\tRp. 100,000")
        print("\n202.   Mangudu\tRumput\tRp. 100,000")
        print("-"*20)

        no_lpg = int(input("Masukkan Nomor Lapangan   :   "))

        if ((no_lpg) == 201):
            harga = 100000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        elif ((no_lpg) == 202):
            harga = 100000
            print("")
            print("-"*10)
            print("Anda telah memilih lapangan", int(no_lpg))
            print("-"*10)
            pesan()
        
        else:
            print("\t   Yahh lapangan Belum tersedia di tempat kami, semoga kedepan nya ada yaa!")
            sleep(3)
            os.system('cls')

    elif((tipe) == 3):
        print("-"*15)
        print("\nNomor    Nama\tTipe\tHarga per Jam")
        print("-"*15)
        print("\n301.   Barung\tSemen\tRp. 80,000")
        print("\n302.   Deli\tSemen\tRp. 80,000")
        print("-"*15)
        no_lpg = int(input("Masukkan Nomor Lapangan   :   "))

        if ((no_lpg) == 301):
            harga = 80000
            print("")
            print("-"*10)
            print("Anda telah memilih Lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        elif ((no_lpg) == 302):
            harga = 80000
            print("")
            print("-"*10)
            print("Anda telah memilih Lapangan", int(no_lpg))
            print("-"*10)
            pesan()

        else:
            print("\t   Yahh lapangan Belum tersedia di tempat kami, semoga kedepan nya ada yaa!")
            sleep(3)
            os.system('cls')      

    elif ((tipe) == 4):
        print("")
        print("\t  >>> Sampai Jumpa lagi <<<")
        sleep(2)
        os.system('cls')
        sleep(1)
        exit
        sleep(1)

    else:
        os.system('cls')
        print(">>>  Maaf, Lapangan tidak ada di list kami!   <<<")