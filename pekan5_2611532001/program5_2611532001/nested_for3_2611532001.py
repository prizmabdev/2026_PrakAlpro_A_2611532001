# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2001 = int(input("Masukkan nilai batas: "))
for i_2001 in range(batas_2001 + 1):
    for j_2001 in range(batas_2001 + 1):
        print(i_2001 + j_2001, end=" ")
    print() # pindah ke baris berikutnya