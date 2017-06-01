import random
number =  random.randint(1, 100)
guess = int(input('I have thought of a number between 1 and 100. Guess it! \n'))
while(guess != number):
  if guess < number:
    guess = int(input('Too low!\n'))
  else: guess = int(input('Too high!\n'))
print("You got it! The number was", guess)