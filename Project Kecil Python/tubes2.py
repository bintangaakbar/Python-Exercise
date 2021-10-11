import os
from time import sleep


loop = True


while loop:
    def menu():
        print("-"*10)
        print("Pesan tiket pesawat online")
        print("-"*10)
        print("pilih tujuan")
        print("1.   Jakarta")
        print("2.   Bali")
        print("3.   Palembang")
        print("4.   EXIT")
        print("-"*10)
    
    def pesan():
        jmlh = int(input("Mau beli tiket berapa ?   :"))
        num_array= list()
        org = input("berapa orang yang ingin memesan tiket ?    :")
        print("Masukkan nama pemesanan  :")
        for i in range (int(org)):
            i += 1
            n = input("orang ke {}  :".format(i))
            num_array.append(str(n))
        total_tket = jmlh * harga
        os.system('cls')
        print("-"*10)
        print("Tiket telah dibeli!")
        print("Nama pemesanan   : ".format(len(num_array)))
        for a in num_array:
            print (("- {}").format(a))
        print("Total Harga", "Rp", total_tket)
    
    menu()
    tujuan = int(input("Pilih Tujuan  :   "))

    if ((tujuan) == 1):
        print("-"*15)
        print("\nKode    Nama\tKota\tHarga")
        print("-"*15)
        print("\n101.   Garuda\tJakarta \tRp. 900,000")
        print("\n102.   Nam Air\tBali   \tRp. 1.500,000")
        print("\n103.   Citilink\tPalembang \tRp. 800,000")
        print("-"*20)
        no_pesawat = int(input("Masukkan kode penerbangan   :   "))

        if ((no_pesawat) == 101):
            harga = 900000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()
        
        elif ((no_pesawat) == 102):
            harga = 1500000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()

        elif ((no_pesawat) == 103):
            harga = 800000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()
        
        else:
            os.system('cls')
            print("Penerbangan itu tidak ada di dalam daftar kami")
    
    elif((tujuan) == 2):
        print("-"*10)
        print("\nKode    Nama\tKota\tHarga")
        print("-"*10)
        print("\n201.   Garuda\tJakarta\tRp. 900,000")
        print("\n202.   NAM air\tBali\tRp. 1.500,000")
        print("\n203.   Sriwijaya\tPalembang\tRp. 800,000")
        print("-"*20)
        no_pesawat = int(input("Masukkan kode penerbangan   :   "))

        if ((no_pesawat) == 201):
            harga = 900000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()
        
        elif ((no_pesawat) == 202):
            harga = 1500000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()

        elif ((no_pesawat) == 203):
            harga = 800000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()
        
        else:
            os.system('cls')
            print("Penerbangan itu tidak ada di dalam daftar kami")

    elif((tujuan) == 3):
        print("-"*10)
        print("\nKode    Nama\tKota\tHarga")
        print("-"*10)
        print("\n301.   Nam air\tPalembang\tRp. 800,000")
        print("\n302.   NAM air\tJakarta\tRp. 900,000")
        print("\n303.   Garuda\tBali\tRp. 1.500.000")
        print("-"*20)
        no_pesawat = int(input("Masukkan kode penerbangan   :   "))

        if ((no_pesawat) == 301):
            harga = 800000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()
        
        elif ((no_pesawat) == 302):
             harga = 900000
             print("")
             print("-"*10)
             print("Anda telah memilih kode penerbangan", int(no_pesawat))
             print("-"*10)

        elif ((no_pesawat) == 303):
            harga = 1500000
            print("")
            print("-"*10)
            print("Anda telah memilih kode penerbangan", int(no_pesawat))
            print("-"*10)
            pesan()
        
        else:
            os.system('cls')
            print("Penerbangan itu tidak ada di dalam daftar kami")   
    elif ((tujuan) == 4):
         print("")
         print("\t  >>> Sampai Jumpa lagi <<<")
         sleep(2)
         os.system('cls')
         sleep(1)
         exit
         sleep(2)

    else:
        os.system('cls')
        print(">>>  Maaf, pilihan tidak ada di list kami!   <<<")