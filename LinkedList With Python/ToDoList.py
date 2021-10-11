class Node:
    def __init__(self, element = None, tgl = None):
        self.element = element
        self.tgl = tgl
        self.nextnode = None
        
    def get_data(self):
        return self.element
        return self.tgl
    
    def get_next(self):
        return self.nextnode
    
    def set_next(self, new_next):
        self.nextnode = new_next

class linkedlist:
    def __init__(self):
        self.head = Node()

    def tambah(self, element, tgl):
        new_node = Node(element,tgl)
        pointer = self.head

        while pointer.nextnode is not None:
            if pointer.nextnode.tgl > tgl:
                break
            pointer = pointer.nextnode
        
        new_node.nextnode = pointer.nextnode
        pointer.nextnode = new_node
        
    def delete(self, element):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == element:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            X = input("")
            
    def tampil(self):
        pointer = self.head
        while pointer.nextnode != None:
            pointer = pointer.nextnode
            print(pointer.element, pointer.tgl, "Hari")

output = linkedlist()
while True:
    print("\n\t=== To Do List ===")
    print("1. Tambah Kegiatan")
    print("2. Hapus Kegiatan")
    print("3. Daftar Kegiatan")
    print("0. Keluar")
    user = input("Silahkan Pilih Menu             : ")
    if user == "1":
        td = str(input("Masukkan Kegiatan               : "))
        tgl = int(input("Deadlinenya berapa hari        : "))
        output.tambah(td, tgl,)
        print("\nDeadline Matakuliah")
        output.tampil()
    elif user == "2":
        output.tampil()
        hps = str(input("Kegiatan Yang Sudah Dilakukan \t:  "))
        print("Tekan Enter untuk melanjutkan")
        output.delete(hps)
        print("\n\nJadwal Saat ini ")
        output.tampil()
    elif user == "3":
        print("\tList Tugas anda : ")
        output.tampil()
    elif user == "0":
        exit()
    else:
        print("Tidak Ada Menu")
        break