import random
def main():
  max=6
  min=1
  dice_rolls = 2
  dice_sum = 0
  for _ in range(0,dice_rolls):
    roll = random.randint(min,max)
    dice_sum += roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()