# nama variabel ditambah 4 digit nim terakhir contoh: nama_1234
# deklarasi variabel dengan tipe data Boolean

is_lulus_2001 = True
is_cumlaude_2001 = True

# menggunakan boolean
nilai_2001 = 85
batas_lulus_2001 = 75

# menentukan nilai boolean dari kondisi
status_kelulusan_2001 = nilai_2001 >= batas_lulus_2001 # hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai: ", nilai_2001)
print("Apakah lulus?: ", status_kelulusan_2001)
if is_lulus_2001 and is_cumlaude_2001:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")