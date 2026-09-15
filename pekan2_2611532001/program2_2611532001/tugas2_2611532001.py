print("=== SISTEM REGISTRASI PRAKTIKUM ALPRO 2026 ===")
nama_2001 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_2001 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_2001 = int(input("Masukkan Umur           : "))
skor_tes_2001 = float(input("Masukkan Skor Tes Awal  : "))
alamat_2001 = """
  Asrama Hijau Universitas Andalas,
  Kecamatan Pauh,
  Kota Padang
"""
id_token_2001 = 100+3j
batas_2001 = 75.0

print("\n=== DATA PRAKTIKUM & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_2001, "| Tipe:", type(nama_2001))
print("Jenis Kelamin  :", jenis_kelamin_2001, "| Tipe:", type(jenis_kelamin_2001))
print("Alamat Domisili:", alamat_2001, "| Tipe:", type(alamat_2001))
print("Umur           :", umur_2001, "tahun | Tipe:", type(umur_2001))
print("Skor Tes Awal  :", skor_tes_2001, "| Tipe:", type(skor_tes_2001))
print("ID Token Sinyal:", id_token_2001, "| Tipe:", type(id_token_2001))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", batas_2001)
if skor_tes_2001 >= batas_2001:
  hasil_2001 = True
else:
  hasil_2001 = False
print("Apakah Dinyatakan Lulus?:", hasil_2001, "| Tipe:", type(hasil_2001))
