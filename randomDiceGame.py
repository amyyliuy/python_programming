from random import seed
from random import randint

dice_1_win_count = 0
dice_2_win_count = 0
tie_count = 0

for i in range(0,1000):
    dice_number_1 = randint(1,6)
    dice_number_2 = randint(1,6)

    if dice_number_1 == dice_number_2:
        print("They are similar!")
        tie_count = tie_count + 1
    elif dice_number_1 > dice_number_2:
        print("Dice number 1 wins!")
        dice_1_win_count = dice_1_win_count + 1
    else:
        print("Dice number 2 wins!")
        dice_2_win_count = dice_2_win_count + 1

percent_1_win = (dice_1_win_count / 1000)*100
percent_2_win = (dice_2_win_count / 1000)*100
percent_tie = (tie_count / 1000)*100


print("The number of times dice 1 wins is: " + str(dice_1_win_count) + " with the percentage of " + str(percent_1_win))
print("The number of times dice 2 wins is: " + str(dice_2_win_count) + " with the percentage of " + str(percent_2_win))
print("The number of times when there is a tie is: " + str(tie_count) + " with the percentage of " + str(percent_tie)) 
print()

if dice_2_win_count > dice_1_win_count:
    print("Overall dice 2 wins!")
elif dice_2_win_count < dice_1_win_count:
    print("Overall dice 1 wins!")
else:
    print("Tie!")

print()
