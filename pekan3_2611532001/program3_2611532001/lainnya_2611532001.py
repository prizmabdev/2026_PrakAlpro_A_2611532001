# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan Fungsi input()
# Program operator keanggotaan dan identitas

print("=======================")
print("1. OPERATOR KEANGGOTAAN")
print("=======================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2001 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2001 = [int(angka_2001.strip()) for angka_2001 in input_data_2001.split(",")]

nilai_dicari_2001 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2001 = nilai_dicari_2001 in data_2001
print("\nOperator keanggotaan IN")
print(nilai_dicari_2001, "in", data_2001, "=", hasil_2001)

# Operator not in
hasil_2001 = nilai_dicari_2001 not in data_2001
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2001, "not in", data_2001, "=", hasil_2001)

print("\n=====================")
print("2. OPERATOR IDENTITAS")
print("=====================")

# objek1_2001 menggunakan list dari input pengguna
objek1_2001 = data_2001

# objek2_2001 merujuk pada objek yang sama dengan objek1_2001
objek2_2001 = objek1_2001

# objek3_2002 memiliki isi sama, tetapi merupakan objek baru
objek3_2001 = data_2001.copy()

print("objek1_2001 =", objek1_2001)
print("objek2_2001 =", objek2_2001)
print("objek3_2001 =", objek3_2001)

# Operator is
hasil_2001 = objek1_2001 is objek3_2001
print("\nOperator identitas IS")
print("objek1_2001 is objek2_2001", hasil_2001)

# Operator is not
hasil_2001 = objek1_2001 is not objek3_2001
print("\nOperator identitas IS NOT")
print("objek1_2001 is not objek3_2001", hasil_2001)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_2001 is objek3_2001", objek1_2001 is objek3_2001)
print("objek1_2001 == objek3_2001", objek1_2001 == objek3_2001)

