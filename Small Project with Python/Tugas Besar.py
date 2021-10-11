import numpy as np
import statistics as st  

class datageneral():   
    def judul(self):
        print("\tPencarian hasil pengeluaran") 
        print("\tToko Sukses Selalu")  
   
    def data(self):     
        data = [5000, 5500, 6000, 9000, 8000, 4500, 10000, 20000, 1000, 2000]  
        print("Data pengeluaran 10 hari terakhir              : ", data) 

class suhu():
    def judul(self):
        print("="*20, "Menghitung Hasil Pengeluaran", "="*20)

    def max(self): 
        data = [5000, 5500, 6000, 9000, 8000, 4500, 10000, 20000, 1000, 2000]  
        hasil = np.max(data)   
        print("Pengeluaran Tertinggi                          : ", float(hasil))

    def rata(self):
        data = [5000, 5500, 6000, 9000, 8000, 4500, 10000, 20000, 1000, 2000]  
        hasil = np.average(data)
        print("Rata-Rata dari pengeluaran                     : ", float(hasil))
    
    def min(self):
        data = [5000, 5500, 6000, 9000, 8000, 4500, 10000, 20000, 1000, 2000]  
        hasil = np.min(data)
        print("Pengeluaran Terendah                           : ", hasil) 
    
    def modus(self): 
        data = [5000, 5500, 6000, 9000, 8000, 4500, 10000, 20000, 1000, 2000]  
        print("modus Dari pengeluaran                         : ",st.mode(data)) 

    def kuartil(self): 
        data = [5000, 5500, 6000, 9000, 8000, 4500, 10000, 20000, 1000, 2000]  
        kuartil1 = np.quantile(data, 0.25) 
        kuartil2 = np.quantile(data, 0.5)  
        kuartil3 = np.quantile(data, 0.75) 
        print("Kuartil 1 Pengeluaran                          : ", kuartil1) 
        print("Kuartil 2 Pengeluaran                          : ", kuartil2) 
        print("Kuartil 3 Pengeluaran                          : ", kuartil3)

cetak = datageneral()
cetak.judul()
cetak.data()

cetak1 = suhu()
cetak1.judul()
cetak1.max()
cetak1.min()
cetak1.rata()
cetak1.modus()
cetak1.kuartil()
