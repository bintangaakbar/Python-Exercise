import numpy as np
def pemmisah():
    print()
def nama():
    print("="*20, " Menghitung harga beras ", "="*20)

nama()
beras = [14000, 12500, 13000, 10000, 11000, 11000, 9750]
harian = [500, 400, 300, 340, 557, 200, 900]

print("Data Harga Beras                             : ",beras)
print("Data Kunjungan Harian                        : ",harian)

def mean(beras):
    sum = 0
    for x in beras:
        sum += x
    return sum/len(beras)
print("Mean Harga Beras                             : Rp.", float(mean(beras)))

if len(beras) % 2 ==0:
    cara = int(len(beras) / 2)
    hasil = (beras[cara - 1] + beras[cara] / 2)
else:
    cara = int((len(beras) + 1 ) / 2)
    hasil = beras[cara - 1]

print("Median Harga Beras                           : Rp.", hasil)

def modus(i=[]):
    a = set(i)
    mode = []
    tinggi = 0
    for x in a:
        hasil = i.count(x)
        if (hasil>1 and hasil>tinggi):
            mode.clear()
            tinggi=hasil
            mode.append(x)
        elif(hasil == tinggi):
            mode.append(x)
    return mode
print("Modus Harga Beras                            : ", modus(beras))

Deviasi = np.std(beras)
print("Standar Deviasi Harga beras                  : ",round(Deviasi,2))

kuartil1 = np.quantile(beras, 0.25)
kuartil2 = np.quantile(beras, 0.5)
kuartil3 = np.quantile(beras, 0.75)
print("Kuartil 1 Harga Beras                        : ", kuartil1)
print("Kuartil 2 Harga Beras                        : ", kuartil2)
print("Kuartil 3 Harga Beras                        : ", kuartil3)

data1 = np.array([beras, harian])
print("Kovarian Harga Beras dengan Jumlah Kunjungan : \n", np.cov(data1))
pemmisah()
print("Korelasi Harga Beras dengan Jumlah Kunjungan : \n", np.corrcoef(data1))