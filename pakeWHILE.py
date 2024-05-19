# looping dengan menggunakan while

total_buku = 10

print(f'Ibu berkata : "Bacalah {total_buku} buku"')
print("")

buku_dibaca = 0

while buku_dibaca < total_buku:
    buku_dibaca += 1
    print(f"Anak sedang membaca buku ke-{buku_dibaca}...Done")

print("")
print(f"Anak telah membaca {buku_dibaca} buah buku")