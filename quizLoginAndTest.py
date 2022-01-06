import time
print()
print("Welcome to the Quiz Programme !\n")

age = int(input("Please enter your age \n"))
#validates if user is old enough to create account
if age <= 16:
    print("Sorry, you are not old enough to create an account. Bye bye !!")
    exit()
else:
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

#set 'i' as the number of times the user inputs login details.  
i = 0
noofattempts = 3
#the number of 'i' is less than 3, repeat the process.
login_username = input("Login username. \n")
login_password = input("Login password. \n")

while i < 3:
    i = i + 1

    time.sleep(0.5)
    print("Processing...")
    time.sleep(0.5)
    print("Processing......")
    time.sleep(0.5)
    print("Processing..........")


#if the login username and password matches, stop the process.
#if the login username and password do not match, print wrong.
     
    if login_username == username and login_password == password:
        break
    else:
        noofattempts = noofattempts - 1
        print("Wrong username or password. Please try again. You have " + str(noofattempts) + " attempts left.")

    if noofattempts == 0:
        print("No attempts left.")

#if less than 3 tries, print login successful
#otherwise locked out

if i < 3:
    print("Login successful")
else:
    print("Sorry, you are locked out of the system.")

time.sleep(1.3)


import time
from threading import Timer
timeout = 5
t = Timer(timeout, print, ['Sorry, times up'])

score = 0
print()
print("Welcome to the Maths quiz section ! In this section, you will complete 4 multiple choice questions. You have 5 seconds for each question.\n")

name = input("Enter your name: ")
print("Welcome to the game " + name)

print()
time.sleep(1)
print("Processing question 1...")
time.sleep(0.4)
print("Loading 99...")
time.sleep(0.3)
print("Loading 100... \n")
time.sleep(0.2)
print()

t = Timer(timeout, print, ['Sorry, times up'])
t.start()

print("Q1: What is 7 * 9 ?")
print("a: 72")
print("b: 81")
print("c: 63")
print("d: 42")
answer = input("Which one is the correct answer ? You have 5 seconds to choose the answer.\n")
t.cancel()

if timeout:
    score = score + 0

if answer == "c" or answer == "C" and not timeout:
    score = score + 1
if timeout and (answer != "C" or answer != "c"):
    score = score + 0
    
print()
time.sleep(1)
print("Processing question 2...")
time.sleep(0.4)
print("Loading 99...")
time.sleep(0.3)
print("Loading 100... \n")
time.sleep(0.2)
print()

t = Timer(timeout, print, ['Sorry, times up'])
t.start()

print("Q2: What is 6 * 7")
print("a: 56")
print("b: 42")
print("c: 54")
print("d: 49")
answer = input("Which one is the correct answer ? You have 5 seconds to choose the answer.\n")
t.cancel()

if timeout:
    score = score + 0

if answer == "b" or answer == "B" and not timeout:
    score = score + 1
if timeout and (answer != "b" or answer != "B"):
    score = score + 0

print()
time.sleep(1)
print("Processing question 3...")
time.sleep(0.4)
print("Loading 99...")
time.sleep(0.3)
print("Loading 100... \n")
time.sleep(0.2)
print()

t = Timer(timeout, print, ['Sorry, times up'])
t.start()

print("Q3: What is 8 * 9")
print("a: 72")
print("b: 42")
print("c: 54")
print("d: 91")
answer = input("Which one is the correct answer ? You have 5 seconds to choose the answer.\n")
t.cancel()

if timeout:
    score = score + 0

if answer == "a" or answer == "A" and not timeout:
    score = score + 1
if timeout and (answer != "a" or answer != "A"):
    score = score + 0

print()
time.sleep(1)
print("Processing question 4...")
time.sleep(0.4)
print("Loading 99...")
time.sleep(0.3)
print("Loading 100... \n")
time.sleep(0.2)
print()

t = Timer(timeout, print, ['Sorry, times up'])
t.start()

print("Q4: What is 556 + 16")
print("a: 572")
print("b: 583")
print("c: 558")
print("d: 582")
answer = input("Which one is the correct answer ? You have 5 seconds to choose the answer.\n")
t.cancel()

if timeout:
    score = score + 0

if answer == "d" or answer == "D" and not timeout:
    score = score + 1
if timeout and (answer != "d" or answer != "D"):
    score = score + 0

print()
time.sleep(0.5)
print("Collecting scores...")
time.sleep(1)
print("Loading...")
time.sleep(0.1)
print()

print("Well done for completing this quiz ! You got " + str(score) + " / 4.")