# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2001 = int(input("Masukkan jumlah perulangan: "))

jumlah_2001 = 0
for i_2001 in range(1, ulang_2001 + 1):
    print(i_2001, end=" ")
    jumlah_2001 = jumlah_2001 + i_2001

    if i_2001 < ulang_2001:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_2001, end=" ")
print()

print("Jumlah =", jumlah_2001)