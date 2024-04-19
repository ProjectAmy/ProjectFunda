# kita akan belajar menggunakan tipe data list

daftar_buku = ['fiqih','tauhid','hadis']
print(daftar_buku)
print('')
for buku in daftar_buku:
    print(buku)

print('\nbuku nomer 3 adalah:')

print(daftar_buku[2])

print('\nkalo pake range gini')

for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmembahkan buku baru')

daftar_buku.append('mustolah')

for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nclear list')

daftar_buku.clear()
print(daftar_buku)

print('\nGanti elemen pertama')
daftar_buku = ['fiqih','tauhid','hadis']

daftar_buku[0] =  'tafsir'

for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

buku_diambil = daftar_buku.pop(1)
print(f'\nbuku yang diambil adalah {buku_diambil}')