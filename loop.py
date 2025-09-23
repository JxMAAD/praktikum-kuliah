# i = 14

# while i >= -16:
#     print(i, end = " ")
#     i -= 6

daftar = ['Matematika', 'Fisika', 'Statistika']

for i in range(len(daftar)):
    print("%d: %s" % (i+1, daftar[i]))

for i in range(1,11):
    for j in range(1, i+1):
        print("%d " % (i*j), end='')
    print()

i = 1
while i <=10:
    for j in range(1, i+1):
        print("%d " % (i*j), end=' ')
    print()
    i+=1