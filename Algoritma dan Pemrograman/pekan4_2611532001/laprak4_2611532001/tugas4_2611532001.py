# ==========================================
# 1. HEADER DAN INPUT DATA PENGUNJUNG
# ==========================================
print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_2001 = input("Masukkan Nama Pengunjung     : ")
umur_2001 = int(input("Input Umur Anda              : "))
is_simC_2001 = input("Apakah Anda Punya SIM C (y/t): ").strip().lower()[0]

print("\nPilihan Paket Wahana (1-5)")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")


# ==========================================
# 2. PEMILIHAN PAKET WAHANA (MATCH-CASE)
# ==========================================
while True:
    input_tiket_2001 = int(input("Masukkan nomor paket (1-5)     : "))

    match input_tiket_2001:
        case 1:
            jenis_wahana_2001 = "Wahana Safari Rimba"
            harga_2001 = 50000
            break
        case 2:
            jenis_wahana_2001 = "Wahana Arung Jeram"
            harga_2001 = 75000
            break
        case 3:
            jenis_wahana_2001 = "Wahana Motor ATV Ekstrim"
            harga_2001 = 120000
            break
        case 4:
            jenis_wahana_2001 = "Wahana Roller Coaster Kilat"
            harga_2001 = 100000
            break
        case 5:
            jenis_wahana_2001 = "Wahana All-Access VIP"
            harga_2001 = 220000
            break
        case _:
            print("\nNomor Paket Tidak Valid. Silakan Pilih Kembali!")


# ==========================================
# 3. INPUT JUMLAH TIKET DAN STATUS TAMBAHAN
# ==========================================
while True:
    jumlah_tiket_2001 = int(input("Masukkan jumlah tiket          : "))
    if (jumlah_tiket_2001 > 0):
        break
    else:
        print("\nJumlah Tiket Tidak Valid. Silakan Masukan Kembali!")

is_member_2001 = input("Apakah Anda member? (y/t)      : ").strip().lower()[0]
is_kode_2001 = input("Apakah kode promo valid? (y/t) : ").strip().lower()[0]

is_kondisi_2001 = True
total_diskon_2001 = 0


# ==========================================
# 4. VALIDASI KELAYAKAN PENGENDARA WAHANA
# ==========================================
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if (input_tiket_2001 == 3):
    if (umur_2001 >= 17 and is_simC_2001 == "y"):
        print(f"STATUS AKSES : Anda Sudah Dewasa dan Boleh Menaiki {jenis_wahana_2001} Sendiri.")
    elif (umur_2001 >= 17 and is_simC_2001 != "y"):
        print(f"STATUS AKSES : Anda Sudah Dewasa tetapi Tidak Boleh Menaiki {jenis_wahana_2001} Sendiri (Wajib Didampingi Instruktur).")
    elif (umur_2001 < 17 and is_simC_2001 == "y"):
        print(f"IDENTITAS TIDAK VALID: Belum Cukup Umur Memiliki SIM.")
        is_kondisi_2001 = False
    else:
        print(f"Anda Belum Cukup Umur dan Tidak Boleh Menaiki {jenis_wahana_2001}.")
        is_kondisi_2001 = False
else:
    if (umur_2001 >= 10):
        print(f"STATUS AKSES : Batas Umur Tercukupi dan Anda Boleh Menaiki {jenis_wahana_2001}.")
    else:
        print(f"STATUS AKSES : Anda Tidak Cukup Umur dan Tidak Boleh Menaiki {jenis_wahana_2001}.")
        is_kondisi_2001 = False


# ==========================================
# 5. AKUMULASI DISKON & RINCIAN PEMBAYARAN
# ==========================================
if is_kondisi_2001:
    if (harga_2001 * jumlah_tiket_2001 >= 200000):
        total_diskon_2001 += 10
    if (is_member_2001 == "y"):
        total_diskon_2001 += 5
    if (is_kode_2001 == "y"):
        total_diskon_2001 += 15
    if (jumlah_tiket_2001 >= 5):
        total_diskon_2001 += 5

    print("\n--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp {harga_2001 * jumlah_tiket_2001:,.0f}")
    print(f"Total Diskon     : {total_diskon_2001}% (Rp {(harga_2001 * jumlah_tiket_2001) * (total_diskon_2001 / 100):,.0f})")
    print(f"Total Bayar       : Rp {(harga_2001 * jumlah_tiket_2001) - ((harga_2001 * jumlah_tiket_2001) * (total_diskon_2001 / 100)):,.0f}")
    if ((harga_2001 * jumlah_tiket_2001) - ((harga_2001 * jumlah_tiket_2001) * (total_diskon_2001 / 100)) > 300000):
            print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
    print("Catatan Layanan  : Terima kasih telah berkunjung.")
    

# ==========================================
# 6. PENUTUP PROGRAM
# ==========================================
print("\nProgram Selesai")