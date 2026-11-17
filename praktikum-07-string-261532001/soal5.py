# Name: Rizki Ramadhani Al Michtari
# NIM: 2611532001
# Question 5

# Bagian A
username = input("Username: ")

if len(username) >= 5:
    if username.isalnum():
        if username[0].isalpha():
            print("Valid")
        else:
            print("Invalid: must start with a letter")
    else:
        print("Invalid: letters and digits only")
else:
    print("Invalid: at least 5 characters")

# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

# Bagian B
nim = input("NIM: ")

if len(nim) >= 10:
    if nim.isdigit():
        print("Valid intake year 20" + str(nim[:2]))
    else:
        print("Invalid NIM")
else:
    print("Invalid: must 10 characters")