import random
def main():
  min=1
  dice_rolls = int(input('How many dice would you like to roll? '))
  max=int(input('How many sides are the dice? '))
  dice_sum = 0
  for _ in range(0,dice_rolls):
    roll = random.randint(min,max)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == max:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()