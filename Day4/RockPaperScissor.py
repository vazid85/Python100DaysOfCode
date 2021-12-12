import random as rd

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _________
---'    ______)________
           ____________)
          ______________)
         ______________)
---.________________)
"""

Scissors = """
    _______
---'   ____)__________
          ____________)
       ________________)
      (____)
---.__(___)
"""

# Game Rules
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

#Rock win on Scissor but lose on paper
#scissor wins on paper but lose on rock
#paper wins on rock butt lose on scissor
#Rock<paper<scissor
#0<1<2
#2
# 0>2

# Two players needed -- User and Computer
Art = [Rock, Paper, Scissors]

user_choice = int(input("Please enter your choice 0 for Rock, 1 for Scissor, 2 for Paper \n"))

if user_choice>2:
    print("You entered invalid number. You loss the game")
else:
    print("User Choice:")
    print(Art[user_choice])

    computer_choice = rd.randint(0, 2)
    print("computer_choice:")
    print(Art[computer_choice])

    if user_choice==0 and computer_choice==2:
        print("User wins!")
    elif computer_choice==0 and user_choice==2:
        print("Computer wins!")
    elif user_choice > computer_choice:
        print("User wins!")
    elif computer_choice > user_choice:
        print("Computer wins")
    else:
        print("its draw")

