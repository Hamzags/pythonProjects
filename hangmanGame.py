#importing random words module in order to generate a random word for user to guess
from random_word import RandomWords

#generate word and split letters into list
generateRandomWord = RandomWords()
hangmanValue = generateRandomWord.get_random_word()
hangmanWordListed = list(hangmanValue)
wordLength = len(hangmanWordListed)
hangmanGuessList = []
for i in range(0, wordLength):
    hangmanGuessList.append('_')

#initializing the guessCount variable as user has 10 chances before game is over.
guessCount=0

#start guessing
print("The hangman game has begun! The word to guess contains", wordLength, "letters!")
#print(hangmanWordListed)
print(hangmanGuessList)


#Main while loop that runs the game while the variable below is equals to true.
isGameActive = True
while isGameActive == True or hangmanGuessList != hangmanWordListed:
    isInHangmanAtLeastOnce = 1

    userGuess = input("Start Guessing: ").lower()
    while len(userGuess) > 1:
        print("You can only guess one letter at time!")
        userGuess = input("Start Guessing: ").lower()
    while userGuess.isalpha() == False:
        print("Only letters are accepted!")
        userGuess = input("Start Guessing: ").lower()

    incorrectGuessIndex = None
    incorrectGuess = 0
    guessesLeft = 10 - guessCount

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

    #User guessed word correctly
    if hangmanWordListed == hangmanGuessList:
        print("Congratulations! You beat the impossible hangman game!")
        isGameActive = False
        startNewGame = input("Start a new game? Y/N").lower()

        if startNewGame != "y":
            isGameActive = False
            print("Thanks for playing!")
        else:
            generateRandomWord = RandomWords()
            hangmanValue = generateRandomWord.get_random_word()
            hangmanWordListed = list(hangmanValue)
            wordLength = len(hangmanWordListed)
            hangmanGuessList = []

            for i in range(0, wordLength):
                hangmanGuessList.append('_')

            print("The hangman game has begun! The word to guess contains", wordLength, "letters!")
            print(hangmanWordListed)
            print(hangmanGuessList)
            isGameActive = True
