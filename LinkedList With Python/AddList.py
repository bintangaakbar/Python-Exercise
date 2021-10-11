class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = Node()
       

    def input(self, data):
        newNode = Node(data)
        current = self.head

        while current.next is not None:
            if current.next.data > data:
                break
            current = current.next
        
        newNode.next = current.next
        current.next = newNode

    def tampil(self):
        current = self.head
        while current.next != None:
            current = current.next
            print(current.data)

show = linkedlist()
while True:
    print("\n\t=== guitarra ===")
    print("\nSelamat datang silahkan pilih menu")
    print("\n1. Tambah merk gitar")
    print("2. Daftar Gitar")
    print("0. Keluar")
    user = input("Silahkan Pilih Menu             : ")
    if user == "1":
        nama = input("Masukan Merk Baru : ").title()
        if nama != "cancel".title():
            show.input(nama)
        else:
            break
    elif user == "2":
        print("\tList Gitar : ")
        show.tampil()
        print("\t \nTekan Enter untuk kembali ke menu awal")
        enter = input("")
        if enter == ("") :
            linkedlist()
    elif user == "0":
        exit()
    else:
        print("Tidak Ada Menu")
        break