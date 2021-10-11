def menu():
    print("""Berikut Pilihan Beberapa Program Studi di Telkom University
    1.Sistem Informasi
    2.Teknik Industri
    3.Teknik Informatika
    4.Desain Komunikasi Visual
    5.Administrasi Bisnis""")

print("\tPendaftaran calon Mahasiswa Baru Telkom University")
nama = input("Masukkan Nama Lengkap Anda        : ")
umur = input("Berapa umur anda                  : ")
tahun= input("Tahun kelulusan                   : ")
menu()
prodi =input("Pilihan Program Studi             : ")
teks = "\nnama : {} \numur : {} \ntahun Kelulusan : {}\n--- ".format(nama,umur,tahun)
nfile = input("Masukkan Nama File Penyimpanan   : ")
f = open(nfile, 'w')
f.write(teks)
f.close()
try:
    nama = str(nama)
    umur = int(umur)
    tahun = int(tahun)
    print("Terima kasih ", nama, "telah daftar di telkom university akan kami infokan selanjutnya via email!")
except:
    print("Data yang diisi harus valid sesuai data yang anda miliki")

print("Menampilkan data dari file")
nfile = input("Masukkan Nama File               : ")
try:
    f = open(nfile)
    while True:
        final = f.readline()
        if len(final) == 0:
            break
        print(final)
    f.close()
except:
    print("File yang diminta tidak ada")
