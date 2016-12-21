import random

#Found variable to check the word has been completely guessed or not
found_word="false"#Found word initially set to false
file =open("keywords.txt",'r')
words=file.readlines()#store all words from file 
list_length=len(words)-1
chosen_word_position = random.randint(0,list_length)#choose any random any position of list

chosen_word =(words[chosen_word_position][:-1]).lower()#randomly choosed word

dashes=""#string to keep dashes in place of letters
for i in chosen_word:
    dashes=dashes+"_ "
#function to get the guess(input) from the player
def get_guess():
    #create a variable to store player's guess
    guess=""
    #Ask the player for their guess(input) and store it in a variable
    guess= input("Guess a letter or whole word: ")
    return guess

#function to check the guess
def check_guess(dashes):
    global false_guesses
    global incorrect_guesses
    if not guess.isalpha(): # check the input is a letter. Also checks an input has been made.
        print("That is not a letter. Please try again.")
        return dashes
    elif guess in incorrect_guesses: # check it letter hasn't been guessed already
        print("You have already guessed that letter. Please try again.")
        return dashes
    if len(guess)>1: #check to see if the guess is a word or one character
        if guess == chosen_word:#check if guess word is correct
            return guess
        else:
            false_guesses=false_guesses+1#increase the number of false gue
            incorrect_guesses.append(guess)#append to wrong guesses list
            return dashes
    else:#if a charcter is guessed
        if guess in chosen_word:#Is the guess in word
            print("Good guess!!...The word contains",guess)
            dashes_temp=""#temporary dashes string to add the the matches
            count =0
            for i in chosen_word:#Loop through the word and check for matches
                if i==guess:# compare word with guess to replace dashes
                    dashes_temp=dashes_temp + i + " "#replace the dash with the guessed letter
                else:
                    dashes_temp = dashes_temp + dashes[count*2]+" "#if letter not matched temporary dashes variable will be same as dashes
                count=count+1
            return dashes_temp#return the new matched string 
        else:#if guess is not in word
            print("Bad guess!!The word doesn't contains ",guess)
            false_guesses=false_guesses+1#increase the number of false guesses
            incorrect_guesses.append(guess)#append to wrong guesses list
            return dashes#no changes in the dashes return as it is

        
false_guesses=0#variable to count number of wrong guesses
incorrect_guesses=[]#a list to keep all the wrong guesses
print("Welcome to Hangman! A word will be chosen at random and\nyou must try to guess the word correctly \nletter by letter or the whole word before you run out of attempts.\nYou can at max have 10 wrong guesses. Good luck!!!!\n\n")
print("Here's your word: ",dashes,"\n")
#Game starts
while found_word == "false" and false_guesses<10:#loop to take guesses(input) from player    
    guess = get_guess()
    dashes=check_guess(dashes)
    print("\n",dashes,"\n")
    print("You have",10-false_guesses,"incorrect guesses remaining!")
    print("Incorrect guess tried so far: ",incorrect_guesses)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    if not "_" in dashes:#check if word is completely guessed or not
        found_word ="true"
        print("Congratulation! Well Done")
if false_guesses==10:#keep a check on number of wrong guesses
    print("Unlucky! Game Over - Hang the Man!")
    print("The word was",chosen_word)
