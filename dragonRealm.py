import random
import time

def displayIntro():
  print('You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.')
  print()

def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':
    print('Which cave will you go into? Type either 1 or 2 down below.')
    cave = input()

    return cave

def checkCave (chosenCave):
  print('You approach the cave...')
  time.sleep(2)
  print('It\'s dark, with water dripping from the ceiling. Suddenly you get the feeling that you aren\'t alone.')
  time.sleep(2)
  print('A LARGE DRAGON JUPS IN FRONT OF YOU! He opens his jaws and...')
  print()
  time.sleep(2)

  friendlyCave = random.randint(1, 2)

  if chosenCave == str(friendlyCave):
    print('Gives you his treasure! That\'s some good luck!')
  else:
    print('Decides that he wants you for lunch. Tough luck!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  displayIntro()
  caveNumber = chooseCave()
  checkCave(caveNumber)

  print('Do you want to play again? Type yes or no.')
  playAgain = input()