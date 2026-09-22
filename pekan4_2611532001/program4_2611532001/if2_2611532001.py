# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

ipk_2001 = float(input("Input IPK Anda = "))

if ipk_2001 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_2001))
else:
    print("Anda Tidak Lulus")

print("Program Selesai")