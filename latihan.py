angka = float(input('masukkan angka: '))

if angka % 2 == 0:
    print(f'{angka}', 'adalah angka genap')
elif angka % 2 == 1:
    print(f'{angka}', 'adalah angka ganjil')
else:
    print(f'{angka}', 'adalah desimal')

# loop angka 1+2+3+4...+n while
n = int(input('masukkan angka: '))
i = 1
num = 0
while i <= n:
    num += i
    i += 1
print('num =', num)

# perkalian
k = int(input('masukkan angka: '))
l = 1
# for
for j in range(0, 10):
    print (f'{k} x {l} = {k*l}')
    l += 1

# while (sebelum menggunakan while, ubah for menjadi command)
while l <= 10:
    print (f'{k} x {l} = {k*l}')
    l += 1

