/*
The goal is to display a random number between 1 and 6.
*/
roll = Math.floor(Math.random()*6) + 1 
//We get a number between 0 and 1 (but not including 1!). We then multiply that by 6, so it goes from 0 and 5.999... 
//We then truncate the number past the decimal (0 to 5) and add 1 (1 to 6)
alert("The result of the die roll was " + roll) //we combine the string and the number we had generated
// We call the javascript alert function to display the result
