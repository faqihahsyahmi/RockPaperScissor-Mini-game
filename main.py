# This is a simple rock paper scissors mini game that applies randomisation to the computer's choice.
# Date: 29 Oct 2023
# Course: Python 100 Days [Day 04]
# Basic Game Rules:
#   1. Rock wins against scissors.  [/]
#   2. Scissors win against paper.  [/]
#   3. Paper wins against rock.     [/]

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

trophy = '''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
'''

# save the above ascii art in a list
game_image = [rock, paper, scissors]

try:
    # user choice convert to int
    user_choice = int(input("What is your choice? Type:\n0 for Rock\n1 for Paper\n2 for Scissors\n"))
    #print(f"User choose:\n {game_image[user_choice]}")
    

    if user_choice < 0 or user_choice > 3:
        print("Invalid Choice! You Lose!")
    else:
        print("\nYou choose:")
        print(game_image[user_choice])

        # computer choose randomly - 0:rock, 1:paper, 2:scissors
        comp_choice = random.randint(0, 2)
        print("\nComputer choose:")
        print(game_image[comp_choice])

        # condition
        if user_choice >= 3 or user_choice < 0:
            print("You choose an invalid number! Hence, you lose!")
        elif user_choice == 0 and comp_choice == 2:
            print("You Win!")
            print(trophy)
        elif comp_choice == 0 and user_choice == 2:
            print("You Lose!")
        elif comp_choice > user_choice:
            print("You Lose!")
        elif user_choice > comp_choice:
            print("You Win!")
            print(trophy)
        elif comp_choice == user_choice:
            print("It is a draw")
        #else:
            #print("You input an invalid choice!")
except ValueError:
    print("\nInvalid Choice!")

print("Thank you for playing the mini game. Click 'run' to play again!")
