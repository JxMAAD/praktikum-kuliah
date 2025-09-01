#Menjumlahkan 4 bilangan bulat
print("--- Penjumlahan 4 Bilangan Bulat ---")
a = int(input("Masukkan bilangan bulat pertama: "))
b = int(input("Masukkan bilangan bulat kedua: "))
c = int(input("Masukkan bilangan bulat ketiga: "))
d = int(input("Masukkan bilangan bulat keempat: "))

jumlah = a + b + c + d
print("Jumlah dari keempat bilangan bulat tersebut adalah:", jumlah)

#Menentukan bilangan terbesar dan terkecil dari 3 bilangan bulat
print("--- Menentukan Bilangan Terbesar dan Terkecil ---")
x = int(input("Masukkan bilangan bulat pertama: "))
y = int(input("Masukkan bilangan bulat kedua: "))
z = int(input("Masukkan bilangan bulat ketiga: "))

terbesar = max(x, y, z)
terkecil = min(x, y, z)

print("Bilangan terbesar adalah:", terbesar)
print("Bilangan terkecil adalah:", terkecil)

#Menentukan sisa pembagian suatu bilangan bulat dengan x ( x > 0)
print("--- Sisa Pembagian ---")
bilangan = int(input("Masukkan bilangan bulat: "))
x = int(input("Masukkan pembagi (x > 0): "))

if x > 0:
    sisa = bilangan % x
    print(f"Sisa dari {bilangan} dibagi {x} adalah:", sisa)
else:
    print("Pembagi harus lebih dari 0!")

#Menhitung luas
#Luas lingkaran
print("--- Luas Lingkaran ---")
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas_lingkaran = 3.14 * jari_jari ** 2
print("Luas lingkaran =", luas_lingkaran)

#Luaa bujur sangkar
print("--- Luas Bujur Sangkar ---")
sisi = float(input("Masukkan panjang sisi bujur sangkar: "))
luas_bujur_sangkar = sisi ** 2
print("Luas bujur sangkar =", luas_bujur_sangkar)

#Luas segitiga
print("--- Luas Segitiga ---")
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
luas_segitiga = 0.5 * alas * tinggi
print("Luas segitiga =", luas_segitiga)