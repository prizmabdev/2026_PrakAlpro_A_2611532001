height = int(input("Enter height: "))
for row in range(height, 0, -1):
    for column in range(row, 0, -1):
        print("*", end=" ")
    print()