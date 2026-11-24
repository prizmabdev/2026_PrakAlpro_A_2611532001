menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Input data penjualan menggunakan nested loop
for day in range(number_of_days):
    daily_sales = []
    for menu in menus:
        amount = int(input(f"Day {day + 1}, {menu}: "))
        daily_sales.append(amount)
    sales.append(daily_sales)

print("Total per day:")
for day in range(number_of_days):
    total = 0
    for amount in sales[day]:
        total += amount
    print(f"Day {day + 1}: {total}")

menu_totals = []
for col in range(len(menus)):
    total = 0
    for row in range(number_of_days):
        total += sales[row][col]
    menu_totals.append((menus[col], total))
print("Total per menu:", menu_totals)

best_seller = ""
max_sales = -1
for name, total in menu_totals:
    if total > max_sales:
        max_sales = total
        best_seller = name
print(f"Best seller: {best_seller} ({max_sales})")
