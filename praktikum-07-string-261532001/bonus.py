# Name: Rizki Ramadhani Al Michtari
# NIM: 2611532001
# Question Bonus

text = input("Input: ")
poin = 0
text = text.lower()
for i in range(len(text)):
  if text[i] == text[-1 - i]:
    poin += 1

if poin == len(text):
  print("Polindrome")
else:
  print("Not a polindrome")