import time

while True:
    try:
        age = int(input("Enter your age \n"))
        break
    except ValueError:
        continue

if age < 12:
    print("Sorry, you are not old enough to create an account. Bye bye !!")
    exit()
    
if age >= 12:
    print("Please create your username and password.")
    print("Create your username: ")
    username = input()

    while True:
        print("Create your password: ")
        password = input()
        if len(password) < 8:
            print("Please create a password greater than or equal to 8 characters.")
            continue
        if not password.isalnum():
            print("Please create a password using letters or numbers.")
            continue
        print("Your name is {0}, Your password is {1}".format(username, password))

        while True:
            change = input("Do you want to change your password ? Y/N \n")
            if change in 'YyNn':
                break

        if change in 'Yy':
            print("What do you want your new password to be ? Please reset：") 
        elif change in 'Nn':
            print("You are all set! Please login.")
            break
        else:
             continue

i = 0

while i < 3:
    i = i + 1
    login_username = input("Login username. \n")
    login_password = input("Login password. \n")
    time.sleep(0.5)
    print("Processing...")
    time.sleep(0.5)
    print("Processing......")
    time.sleep(0.5)
    print("Processing..........")

    if login_username == username and login_password == password :
        break
    else:
        print("Wrong username or password. Please try again. /n")
        continue
        
if i < 3:
    print("Login successful")
else:
    print("Sorry, you are locked out of the system.")
                                                                                
