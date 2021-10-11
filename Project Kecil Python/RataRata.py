nama = str(input("\t Masukkan Nama anda : "))
nim = int(input("\t Masukkan NIM anda : "))

array = []

i = int(input("\t Masukkan Jumlah nilai yang ingin di input : "))
for x in range(i):
    nilai = float(input("\t Masukkan nilai ke-{} : ".format(x+1)))
    array.append(nilai)

print("\t Hasil nilai rata-rata dari : ",nama)
print("\t dengan NIM                 : ",nim)
print("\t adalah                     : {}".format(sum(array)/i))