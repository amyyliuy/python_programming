import time
from threading import Timer
timeout = 10
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

print("Q1: What is 23 * 9 ?")
print("a: 209")
print("b: 227")
print("c: 207")
print("d: 217")
answer = input("You have 10 seconds to choose the answer: \n")
t.cancel()

if timeout:
    score = 0

if answer == "c" or answer == "C":
    score = score + 1
else: 
    score = 0

    
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

print("Q2: What is 45 * 6")
print("a: 280")
print("b: 370")
print("c: 260")
print("d: 270")
answer = input("You have 10 seconds to choose the answer: \n")
t.cancel()

if timeout:
    score = 0

if answer == "d" or answer == "D":
    score = score + 1
else:
    score = 0

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

print("Q3: What is 87 * 9")
print("a: 783")
print("b: 773")
print("c: 883")
print("d: 763")
answer = input("You have 10 seconds to choose the answer: \n")
t.cancel()

if timeout:
    score = 0

if answer == "a" or answer == "A":
    score = score + 1
else:
    score = 0

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

print("Q4: What is 556 * 4")
print("a: 2424")
print("b: 1224")
print("c: 2324")
print("d: 2224")
answer = input("You have 10 seconds to choose the answer: \n")
t.cancel()

if timeout:
    score = 0

if answer == "d" or answer == "D":
    score = score + 1
else:
    score = 0

print()
time.sleep(0.5)
print("Collecting scores...")
time.sleep(1)
print("Loading...")
time.sleep(0.1)
print()

print("Thank you for completing this quiz ! You got " + str(score) + " / 4.")
