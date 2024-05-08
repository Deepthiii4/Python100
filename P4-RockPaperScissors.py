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

value1=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if value1==0:
    print(rock)
elif value1==1:
    print(paper)
else:
    print(scissors)
value2=random.randint(0,2)
if value2==0:
    print("Computer Chose :\n"+rock)
elif value2==1:
    print("Computer chose\n"+paper)
else:
    print("Computer chose\n"+scissors)

if value1==value2:
    print("Its a draw")
elif value1>value2:
    print("You win")
else:
    print("You lose")
