import random
ART = ['''

 +---+
 |   |
     |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
\|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
\|/  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
\|/  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
\|/  |
/ \  |
     |
=========''']
def getRandomWord():
 with open('wordlist.txt') as words:
     wordlist = words.read().split()
 return random.choice(wordlist)

def displayBoard(ART, missedLetters, correctLetters, secretWord):
 print(ART[len(missedLetters)])
 print()

 blanks = '_' * len(secretWord)

 for i in range(len(secretWord)): # replace blanks with correctly guessed letters
     if secretWord[i] in correctLetters:
         blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

 for letter in blanks: # show the secret word with spaces for readability
     print(letter, end=' ')
 print()

 print('Missed letters:', end=' ')
 for letter in missedLetters:
     print(letter, end=' ')
 print()


def getGuess(alreadyGuessed):
 while True:
     print('Guess a letter.')
     guess = input()
     guess = guess.lower()
     if len(guess) != 1:
         print('Please enter a single letter.')
     elif guess in alreadyGuessed:
         print('You have already guessed that letter. Choose again.')
     elif guess not in 'abcdefghijklmnopqrstuvwxyz':
         print('Please enter a letter.')
     else:
         return guess

def playAgain():
 print('Play again? (y/n)')
 return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False

while True:
 displayBoard(ART, missedLetters, correctLetters, secretWord)

 # Let the player type in a letter.
 guess = getGuess(missedLetters + correctLetters)

 if guess in secretWord:
     correctLetters += guess

     # Check if player has won
     foundAllLetters = True
     for i in range(len(secretWord)):
         if secretWord[i] not in correctLetters:
             foundAllLetters = False
             break
     if foundAllLetters:
         print('Correct! The secret word is "' + secretWord + '". You win!')
         gameIsDone = True
 else:
     missedLetters += guess
     if len(missedLetters) >= len(ART) - 1:
         displayBoard(ART, missedLetters, correctLetters, secretWord)
         print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
         gameIsDone = True
 if gameIsDone:
     if playAgain():
         missedLetters = ''
         correctLetters = ''
         gameIsDone = False
         secretWord = getRandomWord()
     else:
         break
