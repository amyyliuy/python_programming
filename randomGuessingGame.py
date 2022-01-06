import random
score = 0
myName = ''

print()
print("Player 1, please get ready!")
myName1 = input("Enter your name, player 1: ")


randomNumber = random.randrange(0,100)
print()
print('Well, ' + myName1 + ', I am thinking of a number between 1 and 100. You need the minimum number of tries to win!')
print()
guessed = False
count = 0

while guessed is False and count<8:
    userInput = int(input("Have a guess: "))
    count += 1
    if userInput == randomNumber:
        print("You are right! I was thinking of " + str(randomNumber) + "!")
        print()
        guessed = True
        if count==1:
            score=score+10000

        elif count==2:
            score=score+5000

        elif count==3:
            score=score+3000

        elif count==4:
            score=score+1000

        elif count==5:
            score=score+500

        elif count==6:
            score=score+300

        elif count==7:
            score=score+200

        elif count==8:
            score=score+100

        elif count==9:
            score=score+50

        elif count==10:
            score=score+1

            
    if userInput > randomNumber:
        print(str(userInput) + " is too high.")
        print()
    if userInput < randomNumber:
        print(str(userInput) + " is too low.")
        print()

player1 = 0
player1 = player1 + score

if count==9:
    print("Your guess is incorrect. The right answer is " + str((randomNumber)))

print("Your score is " + str(score) + ".")


import random
count = 0

print("Player 2, please get ready!")
print("Enter your name, player 2: ")
myName2 = input()
score = 0

randomNumber = random.randrange(0,100)
print()
print('Well, ' + myName2 + ', I am thinking of a number between 1 and 100. You have 8 tries to guess it.')
print()
guessed = False 

while guessed is False and count<8:
    userInput = int(input("Have a guess: "))
    print()
    count += 1
    if userInput == randomNumber:
        print("You are right! I was thinking of " + str(randomNumber) + "!")
        guessed = True
        if count==1:
            score=score+10000

        elif count==2:
            score=score+5000

        elif count==3:
            score=score+3000

        elif count==4:
            score=score+1000

        elif count==5:
            score=score+500

        elif count==6:
            score=score+300
            
        elif count==7:
            score=score+200

        elif count==8:
            score=score+100

        elif count==9:
            score=score+50

        elif count==10:
            score=score+1
            
    if userInput > randomNumber:
        print(str(userInput) + " is too high.")
        print()
    if userInput < randomNumber:
        print(str(userInput) + " is too low.")
        print()
        
player2 = 0
player2 = player2 + score


if count==9:
    print("Your guess is incorrect. The right answer is " + str((randomNumber)))
    print()

print("Your score is " + str(score) + "." + " We are collecting your scores... " + myName)
print()

if player1 == player2:
    print("It's a tie!")
    
if player1 > player2:
    print(myName1 + " wins! Congratulations!")
elif player1 == player2:
    print("TIE!")
else:
    print(myName2 + " wins! Congratulations!")
