vokal = input('Masukkan huruf vokal: ').lower()

if vokal in 'aeiou':
    print(f'{vokal} adalah huruf vokal')
else:
    print(f'{vokal} bukan huruf vokal')