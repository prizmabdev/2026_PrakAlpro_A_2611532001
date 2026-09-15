# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# Nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14

print("pi: %f" % (PI))

jari_2001 = float(input('Masukkan nilai jari-jari: '))
luas_2001 = PI * jari_2001 * jari_2001

print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2001, luas_2001))