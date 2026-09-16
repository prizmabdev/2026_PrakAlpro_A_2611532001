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

is_belanja_min_2001 = total_2001 >= 200000
is_barang_min_2001 = jumlah_2001 >= 3
is_member_2001 = status_2001 == "member"
is_promo_ada_2001 = kode_2001 in daftar_kode_2001
is_promo_tidak_ada_2001 = kode_2001 not in daftar_kode_2001

dapat_diskon_2001 = is_member_2001 and (is_belanja_min_2001 or is_barang_min_2001)
dapat_promo_2001 = is_promo_ada_2001 and not is_promo_tidak_ada_2001

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000 :", is_belanja_min_2001)
print("Jumlah Barang >= 3  :", is_barang_min_2001)
print("Status Member       :", is_member_2001)
print("Kode Promo Tersedia :", is_promo_ada_2001)
print("Mendapatkan Diskon  :", dapat_diskon_2001)
print("Mendapatkan Promo   :", dapat_promo_2001)

if kode_2001 == daftar_kode_2001[0]:
    diskon_2001 = total_2001 / 10
elif kode_2001 == daftar_kode_2001[1]:
    diskon_2001 = total_2001 / 20
else:
    diskon_2001 = 15000

bayar_2001 = total_2001 - diskon_2001
sisa_bagi_barang_2001 = jumlah_2001 % 3

total_setelah_pajak_2001 = bayar_2001
total_setelah_pajak_2001 += 2000

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                 : Rp", diskon_2001)
print("Total Pembayaran       : Rp", bayar_2001)
print("Rata-Rata Harga Barang : Rp", bayar_2001 / jumlah_2001)
print("Sisa Pembagian Barang  :", sisa_bagi_barang_2001)
print("Total + Biaya Admin    : Rp", total_setelah_pajak_2001)

cek_tipe_bayar_2001 = type(bayar_2001) is float
cek_identitas_2001 = total_2001 is not bayar_2001

print("\n=== HAK AKSES & IDENTITAS PELANGGAN ===")
print("Kode Hak Akses       : ")
print("Member Access        : ", is_member_2001)
print("Promo Access         : ", dapat_promo_2001)
print("Free Shipping Access : ", is_promo_ada_2001 and (kode_2001 == "GRATISONGKIR"))
print("Tipe Total float?    : ", cek_tipe_bayar_2001)
print("Total != Bayar Obj?  : ", cek_identitas_2001)

bit_member_2001 = 0b0000
bit_total_2001 = 0b0000
bit_jumlah_2001 = 0b0000
bit_kode_2001 = 0b0000

if is_member_2001:
    bit_member_2001 = 0b0001
if is_belanja_min_2001:
    bit_total_2001 = 0b0010
if is_barang_min_2001:
    bit_jumlah_2001 = 0b0100
if is_promo_ada_2001:
    bit_kode_2001 = 0b1000

bit_status_2001 = bit_member_2001 | bit_total_2001 | bit_jumlah_2001 | bit_kode_2001
bit_referensi_2001 = 0b1111

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(bin(bit_member_2001), " | ", bin(bit_total_2001), " | ", bin(bit_jumlah_2001), " | ", bin(bit_kode_2001))
print("Kode Biner   :", bin(bit_status_2001))
print("Kode Desimal :", bit_status_2001)

print("\n=== Pemeriksaan Status (Bitwise AND &) ===")
print("Cek Member (Status & 0001)")
res_member = bit_status_2001 & 0b0001
print("Kode Biner   :", bin(res_member))
print("Kode Desimal :", res_member)

print("Cek Total (Status & 0010)")
res_total = bit_status_2001 & 0b0010
print("Kode Biner   :", bin(res_total))
print("Kode Desimal :", res_total)

print("Cek Jumlah (Status & 0100)")
res_jumlah = bit_status_2001 & 0b0100
print("Kode Biner   :", bin(res_jumlah))
print("Kode Desimal :", res_jumlah)

print("Cek Promo (Status & 1000)")
res_kode = bit_status_2001 & 0b1000
print("Kode Biner   :", bin(res_kode))
print("Kode Desimal :", res_kode)

print("\n=== Perbandingan Status (Bitwise XOR ^) ===")
print("Kode Transaksi :", bin(bit_status_2001))
print("Kode Referensi :", bin(bit_referensi_2001))
print(bin(bit_status_2001), " ^ ", bin(bit_referensi_2001))
print("Hasil Biner    :", bin(bit_status_2001 ^ bit_referensi_2001))
print("Hasil Desimal  :", bit_status_2001 ^ bit_referensi_2001)

bin_shift_2001 = bit_status_2001 << 1
print("\n=== Shift (Bitwise <<) ===")
print(bin(bit_status_2001), " << ", 1)
print("Hasil Biner    :", bin(bin_shift_2001))
print("Hasil Desimal  :", bin_shift_2001)

print("\n=== SELESAI ===")