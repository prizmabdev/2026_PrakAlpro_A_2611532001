# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2001 = int(input("Masukkan jumlah perulangan: "))

print("Perulangan ke-0 sampai ke-", ulang_2001 - 1)
for i_2001 in range(ulang_2001):
    print(i_2001, end=" ")
print()

print("Perulangan ke-1 sampai ke-", ulang_2001)
for i in range(1, ulang_2001 + 1):
    print(i, end=" ")