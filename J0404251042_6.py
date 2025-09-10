#soal 6
import random
angka_rahasia = random.randint(1, 100)
tebakan = None
jumlah_tebakan = 0
print("Selamat datang di permainan tebak angka!")
print("Saya telah memilih sebuah angka antara 1 hingga 100.")
print("Coba tebak angka tersebut!")
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan angka: "))
    jumlah_tebakan += 1
    if tebakan < angka_rahasia:
        print("Tebakkanmu terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Tebakkanmu terlalu besar")
    else:
        print(f"Selamat, tebakanmu benar!")