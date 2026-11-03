# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angkal 1234
# Program ini menggunakan fungsi input()

print("\n===================")
print("3. OPERATOR BITWISE")
print("===================")

angka1_2001 = int(input("Masukkan angka bitwise-1: "))
angka2_2001 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_2001 =", angka1_2001, "| biner", bin(angka1_2001))
print("angka2_2001 =", angka2_2001, "| biner", bin(angka2_2001))

# Bitwise AND
hasil_2001 = angka1_2001 & angka2_2001
print("\nBitwise AND (&)")
print(angka1_2001, "&", angka2_2001, "=", hasil_2001)
print("Biner hasil =", bin(hasil_2001))
print("Biner hasil (8 bit) =", format(hasil_2001, "08b"))

# Bitwise OR
hasil_2001 = angka1_2001 | angka2_2001
print("\nBitwise OR (|)")
print(angka1_2001, "|", angka2_2001, "=", hasil_2001)
print("Biner hasil =", bin(hasil_2001))
print("Biner hasil (8 bit) =", format(hasil_2001, "08b"))

# Bitwise XOR
hasil_2001 = angka1_2001 ^ angka2_2001
print("\nBitwise XOR (^)")
print(angka1_2001, "^", angka2_2001, "=", hasil_2001)
print("Biner hasil =", bin(hasil_2001))
print("Biner hasil (8 bit) =", format(hasil_2001, "08b"))

# Bitwise NOT
hasil_2001 = ~angka1_2001
print("\nBitwise NOT (~)")
print("~", angka1_2001, "=", hasil_2001)
print("Biner hasil =", bin(hasil_2001))
print("Biner hasil (8 bit) =", format(hasil_2001, "08b"))

# Bitwise geser kiri
jumlah_geser_2001 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2001 = angka1_2001 << jumlah_geser_2001
print("\nBitwise geser kiri (<<)")
print(angka1_2001, "<<", jumlah_geser_2001, "=", hasil_2001)
print("Biner hasil =", bin(hasil_2001))
print("Biner hasil (8 bit) =", format(hasil_2001, "08b"))

# Bitwise geser kanan
hasil_2001 = angka1_2001 >> jumlah_geser_2001
print("\nBitwise geser kanan (>>)")
print(angka1_2001, ">>", jumlah_geser_2001, "=", hasil_2001)
print("Biner hasil =", bin(hasil_2001))
print("Biner hasil (8 bit) =", format(hasil_2001, "08b"))