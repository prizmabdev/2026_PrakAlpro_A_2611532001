number_of_rows = 4
seats_per_row = 5
seats = []

for row in range(number_of_rows):
    seats.append(["."] * seats_per_row)

while True:
    for row in range(number_of_rows):
        print(f"Row {row + 1}: {' '.join(seats[row])}")
    row_number = int(input("Row (0 to stop): "))

    if row_number == 0:
        break

    seat_number = int(input("Seat: "))
    if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > seats_per_row:
        print("Invalid seat.")
    elif seats[row_number - 1][seat_number - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row_number - 1][seat_number - 1] = "X"
        print("Seat booked.")

total_taken = 0
for row in range(number_of_rows):
    for seat in range(seats_per_row):
        if seats[row][seat] == "X":
            total_taken += 1
print("Seats taken:", total_taken)