number =  Math.floor(Math.random() * 100) + 1  
guess = parseInt(prompt('I have thought of a number between 1 and 100. Guess it!'))
while(guess != number){
  if (guess < number) 
    guess = parseInt(prompt('Too low'))
  else 
    guess = parseInt(prompt('Too high'))
}
alert("You got it! The number was " +  guess)
