# penjumlahan
def add(x,y):
    return x + y

# pengurangan
def subtract(x,y):
    return x - y

# perkalian
def multiply (x,y):
    return x * y

# pembagian
def divide (x, y):
    return x / y

print(">>>>     Pilih operasi   <<<<")
print("1.   Jumlah")
print("2.   kurang")
print("3.   kali")
print("4.   bagi")

choice = input("Masukkan pilihan 1 or 2 or 3 or 4   :")

num1 = int(input("Masukkan Nilai pertama : "))
num2 = int(input("Masukkan Nilai kedua : "))

if choice == '1:':
    print(num1,"+", num2, "=", add(num1,num2) )

elif choice =='2':
    print(num1, "-", num2, subtract (num1, num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Input salah")
