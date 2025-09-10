#soal 2
print("Barang apa yang anda beli ? (ketik 1 untuk barang baru/ketik 2 untuk barang lama): ")
pilihan_barang = int(input('masukkan pilihan anda: '))

if pilihan_barang == 1:
    harga_barang = int(input("Masukkan harga sebelum diskon: "))
    diskon = 0.10 * harga_barang
    harga_setelah_diskon = harga_barang - diskon
    print(f"Harga setelah diskon yang harus dibayarkan adalah: {harga_setelah_diskon:.0f}")
elif pilihan_barang == 2:
    harga_barang = int(input("Masukkan harga sebelum diskon: "))
    if harga_barang <= 50000:
        diskon = 0.15 * harga_barang
        harga_setelah_diskon = harga_barang - diskon
        print(f"Harga setelah diskon yang harus dibayarkan adalah: {harga_setelah_diskon:.0f}")
    elif harga_barang > 50000 and harga_barang <= 200000:
        diskon = 0.20 * harga_barang
        harga_setelah_diskon = harga_barang - diskon
        print(f"Harga setelah diskon yang harus dibayarkan adalah: {harga_setelah_diskon:.0f}")
    elif harga_barang > 200001:
        diskon = 0.25 * harga_barang
        harga_setelah_diskon = harga_barang - diskon
        print(f"Harga setelah diskon yang harus dibayarkan adalah: {harga_setelah_diskon:.0f}")
else:
    print("Pilihan tidak valid.")
