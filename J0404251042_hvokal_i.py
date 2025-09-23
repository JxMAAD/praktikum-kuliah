kalimat = input("Masukkan kalimat: ")
vokal = 'aAeEuUoO'
hasil = ""
i = 0

while i < len(kalimat):
    huruf = kalimat[i]
    if huruf in vokal:
        hasil += 'i' if huruf.islower() else 'I'
    else:
        hasil += huruf
    i += 1

print("Hasil ubah vokal i:", hasil)