# Name: Rizki Ramadhani Al Michtari
# NIM: 2611532001
# Question 6

# Pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# Program
full_name = input("Name: ")
nim = input("NIM: ")

full_name = full_name.strip().lower()
if full_name.find(" ") != -1:
    print(full_name[:full_name.find(" ")] + str(nim[-3:]))
else:
    print(full_name + str(nim[-3:]))