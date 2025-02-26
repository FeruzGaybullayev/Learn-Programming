# 5. Password Checker Task: Create a simple password checker.
# User input
password = input("Enter a password: ")
# String in set
password_in_set = {n for n in password}
password_upper = {i.upper() for i in password}
intersection_password = password_in_set.intersection(password_upper)
# Use conditionals for password length
if len(password) < 8:
    print("Password is too short.")

# Use conditionals for know password uppercase
elif bool(intersection_password):
    print("Password is strong.")
else:
    print("Password must contain an uppercase letter.")