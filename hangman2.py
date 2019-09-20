secretWord = input(" Player1 enter a word:  ")
print("\n"*50)

HANGMANPICS = ['''
    ===
      |
      |
      |
      |
      |
=========''', '''
   ====
      |
      |
      |
      |
      |
=========''', '''
  =====
      |
      |
      |
      |
      |
=========''', '''
  =====
  |   |
      |
      |
      |
      |
=========''', '''
  =====
  |   |
  O   |
      |
      |
      |
=========''', '''
  =====
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  =====
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  =====
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  =====
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  =====
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

 
guess_word = []
length_word = len(secretWord)
alphabet = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz "
letter_storage = []

for character in secretWord: # printing blanks for each letter in secret word
     guess_word.append("-")

print("Player2 the word You need to guess has", length_word, "characters")

print(guess_word)


guess_taken = 1
while guess_taken < 11:
    
    guess = input("Player2 pick a letter\n").lower()

    if not guess in alphabet: #checking input
        print("Enter a letter from a-z alphabet")
    elif guess in letter_storage: #checking if letter has been already used
        print("You have already guessed that letter!")
    else: 
        letter_storage.append(guess)
        if guess in secretWord:
          print("You guessed correctly!")
          for x in range(0, length_word): #This Part I just don't get it
              if secretWord[x] == guess:
                guess_word[x] = guess
                print(guess_word)
          if not '-' in guess_word:
            print("You won!")
            break
        else:
          guess_taken += 1
          if guess_taken < 11:
              print("The letter is not in the word. Try Again!")
              print(HANGMANPICS[guess_taken-2])
          else:
              print(HANGMANPICS[-1])
              print("Sorry You lost :<! The secret word was",         secretWord, )


print("Game over!")
