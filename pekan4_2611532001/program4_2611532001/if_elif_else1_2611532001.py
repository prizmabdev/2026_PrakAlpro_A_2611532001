# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2001 = int(input("Input Umur Anda: "))
sim_2001 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_2001 >= 17 and sim_2001 == 'y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")
elif umur_2001 >= 17 and sim_2001 != 'y':
    print("Anda Sudah Dewasa tetapi Tidak Boleh Bawa Motor")
elif umur_2001 < 17 and sim_2001 == 'y':
    print("Anda Belum Cukup Umur Punya SIM")
else:
    print("Anda Belum Cukup Umur Bawa Motor")

print("Program Selesai")