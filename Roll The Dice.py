# A die which can be thrown by the user

import random

print("_____________________ROLL THE DICE_____________________")
print("                  Programmed by Neeraj\n\n")

choice = "y"
while choice.lower() == "y":                    # Upper while loop for the play again command
    roll_dice = 'r'                             # 'r' is the variable for the roll command that would be given by the user
    while roll_dice.lower() == 'r':
        n = random.randint(1, 6)                # 'n' is the random number on the dice
        roll_dice = input("Press 'r' to roll the dice: ")
        if roll_dice.lower() == 'r':
            print("number on the dice: :", n, "\n")

        else:
            print("Please press 'r' !\n")
    choice = input("PLAY AGAIN? press y/n: ")   # choice: The input by the user to play again!
    print(" ")
    if choice.lower() == 'y':
        continue
    else:
        print("Thank You For Playing!\n")
