passwords = []
for i in range(5):
    userpassword = input("Enter your password")
    passwords.append(userpassword)
for password in passwords:
    if len(password) >= 8:
        print(" cool man! the password is strong")
    else:
        print("mmmm not realy that strong")