#importing random words module in order to generate a random word for player to guess
from random_words import RandomWords

#generate word and split letters into list in order to compare player guesses with the word and gradually show correctly guessed letters.
generateRandomWord = RandomWords()
hangmanValue = generateRandomWord.random_word()
hangmanWordListed = list(hangmanValue)
wordLength = len(hangmanWordListed)
hangmanGuessList = []
for i in range(0, wordLength):
    hangmanGuessList.append('_')

#initializing the guessCount variable as player has 10 chances before game is over.
guessCount=0

#displaying message letting player know the game has started as well as the number of letters in the word to guess
print("Starting the impossible Hangman! The word to guess contains", wordLength, "letters!")
print(hangmanGuessList)


#Main while loop that runs the game while the variable isGameActive is True or as long as the list of letters guessed by player is not equals to the list of letters in the generated word
isGameActive = True
while isGameActive == True or hangmanGuessList != hangmanWordListed:


#adding constraints to user input : letters only & only one letter can be guessed at a time. Also using the lower() method to prevent any errors related to case sensitivity
    userGuess = input("Start Guessing: ").lower()
    while len(userGuess) > 1:
        print("You can only guess one letter at time!")
        userGuess = input("Start Guessing: ").lower()
    while userGuess.isalpha() == False:
        print("Only letters are accepted!")
        userGuess = input("Start Guessing: ").lower()

    # managing occurences of player guessed letters in the list of letters in the generated word and initializing variables for occurence of guessed
    # letter in the generated word and inserting the letter if guessed  correctly in our created list at the same index it is in the list of letters for the generated word
    isInHangmanAtLeastOnce = 1
    guessesLeft = 9 - guessCount

    if isInHangmanAtLeastOnce == hangmanWordListed.count(userGuess):
        correctGuessIndex = hangmanWordListed.index(userGuess)
        hangmanGuessList[correctGuessIndex] = userGuess
        print(hangmanGuessList)

    elif isInHangmanAtLeastOnce < hangmanWordListed.count(userGuess):
        duplicateGuess = [i for i in range(len(hangmanWordListed)) if hangmanWordListed[i] == userGuess]
        for i in duplicateGuess:
            hangmanGuessList[i] = userGuess
            print(hangmanGuessList)

    else:
        guessCount += 1
        print("Wrong guess! You have", guessesLeft, "tries left.")
        print(hangmanGuessList)

    #managing the message displayed to the player in case of a player win and offering choice to start a new game.
    if hangmanWordListed == hangmanGuessList:
        print("Congratulations! You beat the impossible hangman game!")
        print("The word was ", hangmanWordListed)
        isGameActive = False
        startNewGame = input("Start a new game? Y/N").lower()

    # managing the message displayed to the player in case of a player loss and offering choice to start a new game.
    elif guessesLeft == 0:
        print("Game Over. Better luck next time!")
        print("The word to guess was ", hangmanWordListed)
        isGameActive = False
        startNewGame = input("Start a new game? Y/N").lower()

    #managing events that happen if user chooses to either a start a new game or not and displaying messages accordingly.
        if startNewGame != "y":
            isGameActive = False
            print("Thanks for playing!")


        else:
            generateRandomWord = RandomWords()
            #hangmanValue = generateRandomWord.get_random_word()
            hangmanWordListed = list(hangmanValue)
            wordLength = len(hangmanWordListed)
            hangmanGuessList = []
            for i in range(0, wordLength):
                hangmanGuessList.append('_')
            print("Starting the impossible Hangman! The word to guess contains", wordLength, "letters!")
            print(hangmanGuessList)
            isGameActive = True
