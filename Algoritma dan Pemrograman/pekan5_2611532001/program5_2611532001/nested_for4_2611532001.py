# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2001 = int(input("Masukkan tinggi (bilangan genap, misal 10): "))

if tinggi_2001 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2001 = tinggi_2001
    c_2001 = a_2001
    lebar_2001 = (2 * tinggi_2001) - 2

    for i_2001 in range(1, tinggi_2001 + 1):
        b_2001 = c_2001 + 1

        for j_2001 in range(1, lebar_2001 + 1):
            # Baris atas dan bawah
            if i_2001 == 1 or i_2001 == tinggi_2001:
                if j_2001 == 1 or j_2001 == lebar_2001:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_2001 == 1 or j_2001 == lebar_2001:
                    print("|", end="")
                else:
                    if j_2001 == c_2001:
                        print("<", end="")
                    elif j_2001 == b_2001:
                        print(">", end="")
                    elif j_2001 == (lebar_2001 - c_2001):
                        print("<", end="")
                    elif j_2001 == (lebar_2001 - c_2001 + 1):
                        print(">", end="")
                    elif j_2001 > b_2001 and j_2001 < (lebar_2001 - c_2001):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_2001 -= 2

        if a_2001 <= 0:
            c_2001 = (-a_2001) + 2
        else:
            c_2001 = a_2001