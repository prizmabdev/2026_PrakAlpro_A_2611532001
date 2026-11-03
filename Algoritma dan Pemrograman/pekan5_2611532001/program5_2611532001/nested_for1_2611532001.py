# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2001 = int(input("Masukkan nilai batas: "))
for line_2001 in range(1, batas_2001 + 1):
    for j_2001 in range(1, (-1 * line_2001 + batas_2001) + 1):
        print(".", end=" ")
    print(line_2001)