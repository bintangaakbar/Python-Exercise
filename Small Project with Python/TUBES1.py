import numpy as np
import statistics as st

def judul():
    print("""\tData Toko Sukses Selalu
    
    \t1. Data Pengeluaran
    \t2. Data Pemasukan
    \t3. Data Karyawan
    \t4. Bonus Karyawan
    """)

def pemisah():
    print()

class pengeluaran():
    def pemisah(self):
        print()

    def judul(self):
        pengeluaran = [5000, 10000, 4500, 6000, 9000, 12000, 8000, 7000]
        print("="*20, "Total Pengeluaran", "="*20)
        print(pengeluaran)

    def mean(self): 
        pengeluaran = [5000, 10000, 4500, 6000, 9000, 12000, 8000, 7000]
        hasil = np.mean(pengeluaran)   
        print("\tTotal Mean Pengeluaran                      : Rp.", float(hasil))  
    
    def median(self):
        pengeluaran = [5000, 10000, 4500, 6000, 9000, 12000, 8000, 7000]
        hasil = np.median(pengeluaran)
        print("\tTotal Median Pengeluaran                    : Rp.", hasil) 
    
    def modus(self): 
        pengeluaran = [5000, 10000, 4500, 6000, 9000, 12000, 8000, 7000]
        print("\tTotal Modus Pengeluaran                     : Rp.",st.mode(pengeluaran)) 

    def deviasi(self): 
        pengeluaran = [5000, 10000, 4500, 6000, 9000, 12000, 8000, 7000]
        hasil = np.std(pengeluaran) 
        print("\tStandar Deviasi Pengeluaran                 : Rp.",round(hasil,2))

    def kuartil(self): 
        pengeluaran = [5000, 10000, 4500, 6000, 9000, 12000, 8000, 7000]
        kuartil1 = np.quantile(pengeluaran, 0.25) 
        kuartil2 = np.quantile(pengeluaran, 0.5)  
        kuartil3 = np.quantile(pengeluaran, 0.75) 
        print("\tKuartil 1 Pengeluaran                       : Rp.", kuartil1) 
        print("\tKuartil 2 Pengeluaran                       : Rp.", kuartil2) 
        print("\tKuartil 3 Pengeluaran                       : Rp.", kuartil3)

class Pemasukantoko(): 
    def pemisah(self):
        print()

    def judul(self):
        Pemasukan = [6000, 9000, 10000, 23000, 24000, 50000, 21000, 5000]
        print("="*20, "Total Pemasukan", "="*20)  
        print(Pemasukan)

    def mean(self): 
        Pemasukan = [6000, 9000, 10000, 23000, 24000, 50000, 21000, 5000]
        hasil = np.mean(Pemasukan)   
        print("\tTotal Mean Pemasukan                        : ", float(hasil))  
    
    def median(self):
        Pemasukan = [6000, 9000, 10000, 23000, 24000, 50000, 21000, 5000]
        hasil = np.median(Pemasukan)
        print("\tTotal Median Pengeluaran                    : ", hasil) 
    
    def modus(self): 
        Pemasukan = [6000, 9000, 10000, 23000, 24000, 50000, 21000, 5000]
        print("\tTotal Modus Pengeluaran                     : ",st.mode(Pemasukan))

    def deviasi(self): 
        Pemasukan = [6000, 9000, 10000, 23000, 24000, 50000, 21000, 5000]
        hasil = np.std(Pemasukan) 
        print("\tStandar Deviasi Pemasukan                   : ",round(hasil,2))

    def kuartil(self): 
        Pemasukan = [6000, 9000, 10000, 23000, 24000, 50000, 21000, 5000]
        kuartil1 = np.quantile(Pemasukan, 0.25) 
        kuartil2 = np.quantile(Pemasukan, 0.5)  
        kuartil3 = np.quantile(Pemasukan, 0.75) 
        print("\tKuartil 1 Pemasukan                         : ", kuartil1) 
        print("\tKuartil 2 Pemasukan                         : ", kuartil2) 
        print("\tKuartil 3 Pemasukan                         : ", kuartil3)

class pegawai():
    def Karyawan(self):
        print("\t Daftar Pegawai Toko Sukses Selalu")
        print()
        data1 = {'name':'Mawar',    'Jabatan'  : 'Supervisor'}
        data2 = {'name':'Pevita',   'Jabatan'  : 'Kasir'}
        data3 = {'name':'Dewi',     'Jabatan'  : 'Kasir'}
        data4 = {'name':'Iqbal',    'Jabatan'  : 'Operator gudang'}
        data5 = {'name':'Adipati',  'Jabatan'  : 'Operator gudang'}
        data6 = {'name':'Jacob',    'Jabatan'  : 'Supir'}
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        print(data5)
        print(data6)


judul()
pil = int(input("\tPilih Nomor Berapa ? "))
print()

try:
    if pil == 1:
        cetak = pengeluaran()
        cetak.judul()
        cetak.pemisah()
        cetak.mean()
        cetak.pemisah()
        cetak.median()
        cetak.pemisah()
        cetak.modus()
        cetak.pemisah()
        cetak.deviasi()
        cetak.pemisah()
        cetak.kuartil()

    elif pil == 2:
        cetak1 = Pemasukantoko()
        cetak1.judul()
        cetak1.pemisah()
        cetak1.mean()
        cetak1.pemisah()
        cetak1.median()
        cetak1.pemisah()
        cetak1.modus()
        cetak1.pemisah()
        cetak1.deviasi()
        cetak1.pemisah()
        cetak1.kuartil()
    
    elif pil == 3:
        cetak2 = pegawai()
        cetak2.Karyawan()

    elif pil == 4:
        Pemasukan = 148000
        bonus = 0.2
        total = (Pemasukan * bonus) / 6
        print("\tTotal Bonus Karyawan yang Harus dibayar             : Rp. ", int(total))
    else:
        print("\tMaaf input yg anda masukkan tidak ada di list kami")
except:
    print("\tMaaf input yg anda masukkan tidak ada di list kami")
finally:
    print()
    print("All Right Reserved Bintang Tel-U")
    print("banugrah2@gmail.com")

pemisah()