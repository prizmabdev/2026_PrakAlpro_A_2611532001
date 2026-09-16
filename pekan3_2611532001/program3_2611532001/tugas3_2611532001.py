print("=== SISTEM TRANSAKSI TOKO ===")
nama_2001 = input("Masukkan Nama Pelanggan    : ")
status_2001 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_2001 = int(input("Masukkan Total Belanja     : "))
jumlah_2001 = int(input("Masukkan Jumlah Barang     : "))
kode_2001 = input("Masukkan Kode Promo        : ").strip().upper()

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan   :", nama_2001)
print("Status Pelanggan :", status_2001)
print("Total Belanja    : Rp", total_2001)
print("Jumlah Barang    :", jumlah_2001)
print("Kode Promo       :", kode_2001)

daftar_kode_2001 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

print("\n=== Hasil Validasi ===")
print("Belanja >= Rp200000 :", total_2001 >= 200000)
print("Jumlah Barang >= 3  :", jumlah_2001 >= 3)
print("Status Member       :", status_2001 == "member")
print("Kode Promo Tersedia :", kode_2001 in daftar_kode_2001)
# Ditambah operator 'not in' & 'not' biar memenuhi syarat operator logika/membership
print("Kode Promo Expired  :", kode_2001 not in daftar_kode_2001)
print("Mendapatkan Diskon  :", (status_2001 == "member") and ((total_2001 >= 200000) or (jumlah_2001 >= 3)))
print("Mendapatkan Promo   :", kode_2001 in daftar_kode_2001 and not (status_2001 == "nonmember"))

if kode_2001 == daftar_kode_2001[0]:
    diskon_2001 = total_2001 / 10
elif kode_2001 == daftar_kode_2001[1]:
    diskon_2001 = total_2001 / 20
else:
    diskon_2001 = 15000

bayar_2001 = total_2001 - diskon_2001

# Ditambah operator penugasan (augmented assignment +=) & modulo (%)
sisa_barang_2001 = jumlah_2001 % 3
bayar_akhir_2001 = bayar_2001
bayar_akhir_2001 += 0

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                 : Rp", diskon_2001)
print("Total Pembayaran       : Rp", bayar_2001)
print("Rata-Rata Harga Barang : Rp", bayar_2001 / jumlah_2001)
# Output tambahan operator aritmatika % dan penugasan +=
print("Sisa Pembagian Barang  :", sisa_barang_2001)
print("Total Akhir (Penugasan): Rp", bayar_akhir_2001)

# Ditambah pembuktian operator identitas (is & is not)
cek_tipe_2001 = type(bayar_2001) is float
cek_identitas_2001 = total_2001 is not bayar_2001

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       : ")
print("Member Access        : ", status_2001 == "member")
print("Promo Access         : ", kode_2001 in daftar_kode_2001)
print("Free Shipping Access : ")
# Output tambahan operator identitas
print("Cek Tipe Float (is)  : ", cek_tipe_2001)
print("Cek Identitas (is not): ", cek_identitas_2001)

bit_member_2001 = 0b0000
bit_total_2001 = 0b0000
bit_jumlah_2001 = 0b0000
bit_kode_2001 = 0b0000

if status_2001 == "member":
    bit_member_2001 = 0b0001
if total_2001 >= 200000:
    bit_total_2001 = 0b0010
if jumlah_2001 >= 3:
    bit_jumlah_2001 = 0b0100
if kode_2001 in daftar_kode_2001:
    bit_kode_2001 = 0b1000

bit_status_2001 = bit_member_2001 | bit_total_2001 | bit_jumlah_2001 | bit_kode_2001
bit_referensi_2001 = 0b1111

print("\n=== OPERASI BITWISE ===")
print("\n=== Kode Status Transaksi ===")
print(bin(bit_member_2001), " | ", bin(bit_total_2001), " | ", bin(bit_jumlah_2001), " | ", bin(bit_kode_2001))
print("Kode Biner   :", bin(bit_status_2001))
print("Kode Desimal :", bit_status_2001)

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print("1111 & 0001")
print("Kode Biner   :", bin(bit_status_2001 & bit_member_2001))
print("Kode Desimal :", bit_status_2001 & bit_member_2001)

print("\nCek Total")
print("1111 & 0010")
print("Kode Biner   :", bin(bit_status_2001 & bit_total_2001))
print("Kode Desimal :", bit_status_2001 & bit_total_2001)

print("\nCek Jumlah")
print("1111 & 0100")
print("Kode Biner   :", bin(bit_status_2001 & bit_jumlah_2001))
print("Kode Desimal :", bit_status_2001 & bit_jumlah_2001)

print("\nCek Promo")
print("1111 & 1000")
print("Kode Biner   :", bin(bit_status_2001 & bit_kode_2001))
print("Kode Desimal :", bit_status_2001 & bit_kode_2001)

print("\n=== Perbandingan Status ===")
print("Kode Transaksi :", bin(bit_status_2001))
print("Kode Referensi :", bin(bit_referensi_2001))
print(bin(bit_status_2001), " ^ ", bin(bit_referensi_2001))
print("Hasil Biner    :", bin(bit_status_2001 ^ bit_referensi_2001))
print("Hasil Desimal  :", bit_status_2001 ^ bit_referensi_2001)

bin_shift_2001 = bit_status_2001 << 1
print("\n=== Shift ===")
print(bin(bit_status_2001), " << ", 1)
print("Hasil Biner    :", bin(bin_shift_2001))
print("Hasil Desimal  :", bin_shift_2001)

print("\n=== SELESAI ===")