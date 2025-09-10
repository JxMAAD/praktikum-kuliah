#soal 1
harga_pokok = int(input("Masukkan harga pokok: "))
harga_jual = int(input("Masukkan harga jual: "))

presentase_keuntungan = ((harga_jual - harga_pokok) / harga_pokok) * 100
print(f"Presentase keuntungan adalah: {presentase_keuntungan:.2f}%")