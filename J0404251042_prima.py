angka = int(input("Masukkan angka: "))
prima = True
if angka <= 1:
    prima = False
else:
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break

if prima:
    print(angka, "adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")