# listKota = [
#     'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
#     'Jogjakarta', 'Semarang', 'Makassar'
# ]

# kotaYangDicari = input('Ketik nama kota yang kamu cari: ')
# for i, kota in enumerate(listKota):
#     if kota.lower() == kotaYangDicari.lower():
#         print('Kota yang anda cari berada pada indeks', i)
#         break
# else:
#     print('Maaf, kota yang anda cari tidak ada')


# listKota = [
# 'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
# 'Jogjakarta', 'Semarang', 'Makassar'
# ]
# # bermain pop
# while listKota:
#     print(listKota.pop())


# a = int(input('Masukkan bilangan ganjil lebih dari 50: '))
# while a % 2 != 1 or a <= 50:
#     a = int(input('Salah, masukkan lagi: '))
# print('Benar')


# listKota = [
#     'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
#     'Jogjakarta', 'Semarang', 'Makassar'
# ]
# # skip jika i adalah bilangan genap dan lebih dari 0

# i = -1
# while i < len(listKota):
#     i += 1
#     if i % 2 == 0 and i > 0:
#         print('skip')
#         continue
#     print(listKota[i])


# listKota = [
#     'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
#     'Jogjakarta', 'Semarang', 'Makassar'
# ]
# kotaYangDicari = input('Masukkan nama kota yang dicari: ')
# i = 0
# while i < len(listKota):
#     if listKota[i].lower() == kotaYangDicari.lower():
#         print('Ketemu di index', i)
#         break
#     print('Bukan', listKota[i])
#     i += 1