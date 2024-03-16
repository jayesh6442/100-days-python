# rock papaer scissors game

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
game_image = [rock, paper, scissors]
human_choise = random.randint(0, 2)
computer_choise = random.randint(0, 2)

print("human chose")
print(game_image[human_choise])
print("computer chose")
print(game_image[computer_choise])

if human_choise == computer_choise:
    print("It is a tie!")

elif (human_choise == 0 and computer_choise == 2) or (human_choise == 1 and computer_choise == 0) or (human_choise == 2 and computer_choise == 1):
    print("human wins")
else:
    print("computer wins")
