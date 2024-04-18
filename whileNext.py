# kasus jika looping tanpa akhir

total_buku = 10

print(f'ibu berkata : "bacalah {total_buku} buku dan pahami"')
print("")

buku_dibaca = 0
jumlah_baca = 0

while jumlah_baca < total_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if buku_dibaca == 9:
        print(f"Anak belum paham buku yang ke-{buku_dibaca + 1}")
    else:
        buku_dibaca = buku_dibaca + 1
        print(f"Anak sedang membaca dan memahami buku ke-{buku_dibaca}...Done")