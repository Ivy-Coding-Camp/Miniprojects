'''
The point of this program is to have the user input a number, and compare that to a number that the computer has already generated. 
If the number differs from the computer selected number, tell them how it differs.
Once they guess the right number, tell them, and stop the program
'''
import random #importing the random number library from Python
number =  random.randint(1, 100) #Generating the random number
guess = int(input('I have thought of a number between 1 and 100. Guess it! \n')) 
#taking in the guess. When the user types in something, it is a string in python. So, we must convert it to a number, using the 'int' cast function
while(guess != number): #while the guess isn't correct. This is the main loop
  if guess < number: #if the guess is too low, tell them it is too low
    guess = int(input('Too low!\n'))
  else: guess = int(input('Too high!\n')) #if it isn't too low, and if it isn't equal, it must be too high. That is why we use the else statement
#In both cases, we want the user to guess again. Once they type in the guess, the program goes back to the start of the while loop
 #if the get the number, this loop will not run. So, we tell the user that they got the number.
print("You got it! The number was", guess)