#Application Development Assignment
#Group C16
#Name: Abylay AKHMETZHAN, ID: 22104119D
#Name: Miah Safwan ABDAL, ID: 22105084D
#Name: Zhanggir SAPAR, ID: 22103921D

from polyn import Polyn
# Adds a user, st is the user is name, pa is password
def addUser(st, pa):
    with open('users.txt', 'a') as file:
        file.write(st + '\n')
        file.write(pa + '\n')
    print(f"{st} has been added")

# Deletes a user's info, taking in username and password
def delUser(st):
    password = input("Password: ")
    with open('users.txt', 'r') as file:
        lines = file.readlines()

    with open('users.txt', 'w') as file:
        user_found = False
        for i in range(0, len(lines), 2):
            if lines[i].strip() == st:
                if lines[i+1].strip() == password:
                    user_found = True
                    continue  # Skip writing the user and password to file
                else:
                    print("Incorrect password")
            file.write(lines[i])
            file.write(lines[i+1])

    if user_found:
        print(f"{st} has been removed")
    else:
        print(f"User {st} not found or password incorrect")

# Change st's password to pa(the new password)
def changePass(st, pa):
    with open('users.txt', 'r') as file:
        lines = file.readlines()
    with open('users.txt', 'w') as file:
        for i in range(0, len(lines), 2):
            if lines[i].strip() == st:
                file.write(lines[i])
                file.write(pa + '\n')
            else:
                file.write(lines[i])
                file.write(lines[i+1])
    print("Password has been changed")

# Returns True if login is successful, otherwise returns false st is username and pa is password
def login(st):
    pa = input("Password: ")
    with open('users.txt', 'r') as file:
        lines = file.readlines()
    for i in range(0, len(lines), 2):
        if lines[i].strip() == st and lines[i+1].strip() == pa:
            return True
    return False

# Main program which handles the user interface and input
login_attempts = 0
while True:
    print("1. User login")
    print("2. Change password")
    print("3. Add user")
    print("4. Delete user")
    print("5. Quit")

    ch = input("Your choice = ").strip()

    if ch == "1":
        st = input("User name = ")
        if login(st):
            print("Login successful!")
            logged_in = True
            while logged_in:
            #once successfully logged in, calculates the difference of the two polynomials or roots
                roots_or_diff = input("Do you wish to calculate difference of two polynomials or roots? (d/r) ")
                if roots_or_diff == "d":
                    z1 = Polyn()    # creates the polynomial object z1
                    z1.input()      # takes input for the coefficients of polynomial z1
                    z2 = Polyn()    # creates the polynomial object z2
                    z2.input()      #takes input for the coefficients of polynomial z2
                    print(z1, "-", z2, "=", z1 - z2)# Task 1, subtraction of the two polynomials
                elif roots_or_diff == "r":
                    z = Polyn(); z.input()
                    roots = z.find_roots()
                    print(roots)
                    print("P.S. x+0j means that x is a real root")
                else:
                    print("Invalid input")

                choice_further = input("Do you wish to continue? Y/N").lower()
            #asks whether you wish to continue with further calculation, allows the user to calculate repeatedly
                if choice_further == "n":
                    break
                elif choice_further == "y":
                    logged_in = True
                else:
                    print("Invalid input")
            login_attempts = 0  # Reset login attempts on successful login
        else:
            print("Incorrect user name or password")
            login_attempts += 1
            #Prevents too many login attempts
            if login_attempts >= 3:
                print("Too many incorrect login attempts. Exiting...")
                break


    elif ch == "2":
        # takes username, and checks the login credentials by calling login function
        st = input("User name = ")
        if login(st):
            # after login is successful, takes input for new password and calls the changePass function to change the password
            pa = input("New password = ")
            changePass(st, pa)
        else:
            print("Incorrect user name or password")

    elif ch == "3":
        st = input("User name = ")
        pa = input("Password: ")
        addUser(st, pa)

    elif ch == "4":
        st = input("User name = ")
        delUser(st)

    elif ch == "5":
        print("Goodbye!")
        break

    else:
        print("Illegal choice!")

