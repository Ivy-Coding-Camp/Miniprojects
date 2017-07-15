import random #importing the random library from python
answers = ["It is certain", "Without a doubt", "Yes, definitely",
           "You may rely on it", "As I see it, yes", "Most likely",
           "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again",
           "Ask again later", "Better not tell you now", "Cannot predict now",
           "Concentrate and ask again", "Don't count on it", "My reply is no",
           "My sources say no", "Outlook not so good", "Very doubtful"] #here, we declare a list of strings. 
ans = '!' #we give ans a value so that the while loop will execute. 
while ans: #This will keep on looping as long as ans is not blank. If a variable stores nothing, it returns false when checked
    ans = input("Ask the magic 8 ball a question. (Press enter to leave): \n") 
    #The reason we store the input is so the user can exit the program by passing in nothing for ans
    print(random.choice(answers)) #the random library lets us draw a random string from a list. We then print it
