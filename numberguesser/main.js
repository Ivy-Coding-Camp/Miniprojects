/*
The point of this program is to have the user input a number, and compare that to a number that the computer has already generated. 
If the number differs from the computer selected number, tell them how it differs.
Once they guess the right number, tell them, and stop the program
*/
number =  Math.floor(Math.random() * 100) + 1 //guessing for a number between 1 and 100
guess = parseInt(prompt('I have thought of a number between 1 and 100. Guess it!')) //we take in the first guess
while(guess != number){ //while the guess isn't correct. This is the main loop
  if (guess < number) //if the guess is too low, tell them it is too low
    guess = parseInt(prompt('Too low'))
  else //if it isn't too low, and if it isn't equal, it must be too high. That is why we use the else statement
    guess = parseInt(prompt('Too high'))
//In both cases, we want the user to guess again. Once they type in the guess, the program goes back to the start of the while loop
}//if they get the number, this loop will not run. So, we tell the user that they got the number.
alert("You got it! The number was " +  guess)
