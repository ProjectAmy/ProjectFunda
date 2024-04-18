# Belajar menggunakan IF
# dari diagram flowchart

print('Ibu berkata : "beli 1 botol susu"')
print("jika ada telor beli 6 butir telor")
print('anak menjawab : " siap"')
print("anak pergi ke indomaret")

susu = 5
telor = 6

print(" ")
print(f"jumlah susu yang tersedia {susu}")
print(f"jumlah telor yang tersedia {telor}")
print(" ")

if susu > 0:
    print("beli 1 botol susu")
    if telor > 5:
        print("beli telor 6")
        print("anak pulang membawa susu dan telor")
    else:
        print("anak pulang bawa susu saja")
else:
    if telor > 5:
        print("beli telor 6")
        print("anak pulang bawa telor saja")
    else:
        print("anak pulang ndak bawa apa apa")
