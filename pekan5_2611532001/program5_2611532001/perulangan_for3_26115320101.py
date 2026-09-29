# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2001 = int(input("Masukkan jumlah perulangan: "))

jumlah_2001 = 0
for i in range(1, ulang_2001+1):
    print(i, end=" ")
    jumlah_2001 = jumlah_2001 + i

    if i < ulang_2001:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_2001, end=" ")
print()

print("Jumlah =", jumlah_2001)