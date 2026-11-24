LAST_DIGIT = 1 #change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
total = 0
limit = 0
for i in range(7):
    daily = int(input(f"Day {i+1}: "))
    expenses.append(daily)

    total += daily
    if daily > daily_limit:
        limit += 1

    if i == 0:
        min = daily
        max = daily
        max_index = i
    if min > daily:
        min = daily
    if max < daily:
        max = daily
        max_index = i

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {total / len(expenses):.1f}")
print(f"Highest: day {max_index + 1} ({max})")
print(f"Days above limit: {limit}")