# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2001 = int(input("Input angka-1: "))
angka2_2001 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2001 = angka1_2001 + angka2_2001
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2001)

# Pengurangan
hasil_2001 = angka1_2001 - angka2_2001
print("\nOperator Pengurangan")
print("Hasil =", hasil_2001)

# Perkalian
hasil_2001 = angka1_2001 * angka2_2001
print("\nOperator Perkalian")
print("Hasil =", hasil_2001)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2001 != 10:
    hasil_2001 = angka1_2001 / angka2_2001
    print("\noperator Pembagian")
    print("Hasil =", hasil_2001)

    hasil_2001 = angka1_2001 // angka2_2001
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2001)

    hasil_2001 = angka1_2001 % angka2_2001
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2001)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2001 = angka1_2001 ** angka2_2001
print("\nOperator Pangkat")
print("Hasil =", hasil_2001)