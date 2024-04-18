# belajar menggunakan for

total_buku = 10
print(f'ibu berkata "bacalah {total_buku} buku"')
print(" ")

buku_dibaca = 0

for buku_dibaca in range(1, total_buku+1):
    print(f"Anak sedang membaca buku ke-{buku_dibaca}")

print(" ")
print(f"anak telah membaca {buku_dibaca} buah buku")