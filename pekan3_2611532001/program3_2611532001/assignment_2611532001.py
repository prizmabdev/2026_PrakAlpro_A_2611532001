# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angkal_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data Integer
# Program operator assignment dalam Python

angka1_2001 = int(input("Input angka-1: "))
angka2_2001 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2001)
print("Nilai angka2 =", angka2_2001)

# Assignment biasa
hasil_2001 = angka1_2001
print("\nAssignment biasa (=)")
print("Hasil =", hasil_2001)

# Assignment penambahan
hasil_2001 = angka1_2001
hasil_2001 = angka2_2001
print("\nAssignment penambahan (+-)")
print("Hasil =", hasil_2001)

# Assignment pengurangan
hasil_2001 = angka1_2001
hasil_2001 = angka2_2001
print("\nAssignment pengurangan (-)")
print("Hasil =", hasil_2001)

# Assignment perkalian
angka1_2001 = hasil_2001
angka2_2001 = hasil_2001
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_2001)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2001 != 0:
    hasil_2001 = angka1_2001
    hasil_2001 /= angka2_2001
    print("\nAssignment pembagian (/-)")
    print("Hasil =", hasil_2001)
    #Operator tambahan
    hasil_2001 = angka1_2001
    hasil_2001 //= angka2_2001
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2001)
    hasil_2001 = angka1_2001
    hasil_2001 %= angka2_2001
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2001)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

#Operator tambahan: assignment perpangkatan
hasil_2001 = angka1_2001
hasil_2001 **= angka2_2001
print("\nAssignment perpangkatan (**)")
print("Hasil =", hasil_2001)