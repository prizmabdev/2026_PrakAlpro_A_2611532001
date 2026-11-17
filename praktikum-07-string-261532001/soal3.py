# Name: Rizki Ramadhani Al Michtari
# NIM: 2611532001
# Question 3

# Bagian A
text = "Informatika"
print(text[-1])
print(text.upper())
print(text[0:20])

# Bagian B
text = "Rizki Ramadhani Al Michtari"
count = 0
text = text.lower()
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)
