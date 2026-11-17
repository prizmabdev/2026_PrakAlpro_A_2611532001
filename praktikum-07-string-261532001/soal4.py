# Name: Rizki Ramadhani Al Michtari
# NIM: 2611532001
# Question 4

phone = "082611532001"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)