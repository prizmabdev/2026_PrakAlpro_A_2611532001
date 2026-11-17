# Name: Rizki Ramadhani Al Michtari
# NIM: 2611532001
# Question 7

print("==============================")
print("         STUDENT CARD         ")
print("==============================")
full_name = input("Name      : ")
nim = input("NIM       : ")

full_name = full_name.strip().lower()
if full_name.find(" ") != -1:
    print("Username  : " + full_name[:full_name.find(" ")] + nim[-3:])
else:
    print("Username  : " + full_name + str(nim[-3:]))

print("Intake    : 20" + nim[:2])
print("==============================")