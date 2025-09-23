kalimat = input("Masukkan kalimat: ")
vokal = 'aiueoAIUEO'
jumlah = 0
i = 0

while i < len(kalimat):
    if kalimat[i] in vokal:
        jumlah += 1
    i += 1

print("Jumlah huruf vokal:", jumlah)