#program menggunakan if else / elif
#input nilai
print('program menggunakan if else / elif')
print('uts 30%')
uts = float(input('Masukan nilai uts: '))
print('utsp 15%')
utsp = float(input('Masukan nilai utsp: '))
print('uas 40%')
uas = float(input('Masukan nilai uas: '))
print('uasp 15%')
uasp = float(input('Masukan nilai uasp: '))

#hitung nilai
nilai_akhir = (uts * 0.30) + (utsp * 0.15) + (uas * 0.40) + (uasp * 0.15)

#tentukan nilai akhir
if 80 <= nilai_akhir <= 100:
    huruf = "A"
elif 70 <= nilai_akhir < 80:
    huruf = "B"
elif 60 <= nilai_akhir < 70:
    huruf = "C"
elif 40 <= nilai_akhir < 60:
    huruf = "D"
else:
    huruf = "E"

print(f"\nNilai akhir: {nilai_akhir:.2f}")
print(f"Huruf mutu: {huruf}")

print("\n========================\n")

#program menggunakan if else tanpa elif
#input nilai
print('program menggunakan if else tanpa elif')
print('uts 30%')
uts = float(input('Masukan nilai uts: '))
print('utsp 15%')
utsp = float(input('Masukan nilai utsp: '))
print('uas 40%')
uas = float(input('Masukan nilai uas: '))
print('uasp 15%')
uasp = float(input('Masukan nilai uasp: '))

#hitung nilai
nilai_akhir = (uts * 0.30) + (utsp * 0.15) + (uas * 0.40) + (uasp * 0.15)

#tentukan nilai akhir
if 80 <= nilai_akhir <= 100:
    huruf = "A"
else:
    if 70 <= nilai_akhir < 80:
        huruf = "B"
    else:
        if 60 <= nilai_akhir < 70:
            huruf = "C"
        else:
            if 40 <= nilai_akhir < 60:
                huruf = "D"
            else:
                huruf = "E"

print(f"\nNilai akhir: {nilai_akhir:.2f}")
print(f"Huruf mutu: {huruf}")