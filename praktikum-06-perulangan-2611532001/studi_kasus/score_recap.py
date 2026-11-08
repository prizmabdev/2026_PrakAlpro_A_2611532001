PASS_SCORE = 65
total_score = 0
amount_passed = 0

amount_student = int(input("Input amount of students: "))
while amount_student <= 0:
    print("Invalid student count!. Please enter again.")
    amount_student = int(input("Input amount of students: "))

for i in range(amount_student):
    score = int(input(f"Input score for student {i+1}: "))
    while score < 0 or score > 100:
        print("Invalid score!. Please enter again.")
        score = int(input(f"Input score for student {i+1}: "))
    total_score += score

    if i == 0:
        min_score = score
    else:
        if score < min_score:
            min_score = score

    if score >= PASS_SCORE:
        amount_passed += 1

average_score = total_score / amount_student
print(f"Total score  : {total_score}")
print(f"Average score: {average_score}")
print(f"Passed       : {amount_passed}")
print(f"Lowest score : {min_score}")