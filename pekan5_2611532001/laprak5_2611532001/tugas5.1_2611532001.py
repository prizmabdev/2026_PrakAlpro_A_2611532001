tinggi_2001 = int(input("Masukkan tinggi segitiga: "))


for i_2001 in range(1, tinggi_2001 + 1):
    for j_2001 in range(tinggi_2001 - i_2001):
        print(" ", end="")
    for k_2001 in range(i_2001):
        print("*", end=" ")
    print()