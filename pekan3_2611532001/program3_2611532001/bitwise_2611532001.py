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
print(angka1_2001, "&", angka2_2001, " ", hasil_2001)
print("Biner hasil", bin(hasil_2001))
print("Biner hasil (8 bit)", format(hasil_2001, "08b"))

# Bitwise OR
hasil_2001 = angka1_2001 | angka2_2001
print("\nBitwise OR (1)")
print(angka1_2001, "I", angka2, "", hasil)
print("Biner hasil, bin(hasil))
print("Biner hasil (8 bit)", format(hasil, "686"))

#Bitwise XOR
hasil angkal angka2
print("\nBitwise XOR (^)")
print(angkal, "^", angka2, "=", hazil)
print("Biner hasil", bin(hasil))
print("Biner hasi) (8 bit)", format(hasil, "086"))

#Bitwise NOT
hasilangkal
print("\nBitwise NOT (~)")
print("-", angkal, "", hasil)
print("Diner hasil", bin(hasil))
print("Biner hasil (8 bit)", format(hasil, "овь"))

#Bitwise geser kiri
jumlah_geser int(input("\nMasukkan jumlah pergeseran bit) "))

hasil angkal << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angkal, "<<", jumlah_geser, "a", hasil)
print("Biner hasil", bin(hasil))
print("Biner hasil (8 bit) a", format(hasil, "056"))

Bitwise geser kanan
hasil angkal >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angkal, ">>", jumlah_geser, "", hasil)
print("Biner hasil", bin(hasil))
print("Biner hasil (B bit)", format(hasil, "06b"))