import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
listedLetters = list(letters)
possibleCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '-', ':', ';', '/', '.', ',', '?', '0',
                      '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

allChars = possibleCharacters + listedLetters
listedPassword = []


for x in range(0, 12):
    randomIndex = random.randint(0, 80)
    listedPassword.append(allChars[randomIndex])

password = ''.join(listedPassword)
print(password)
