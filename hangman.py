import random
print('Hello, in order to play, please enter your name.')
username = input()
if username != 'Cookie':
  hangmanPics = ['''
+---+
    |
    |
    |
   ===''','''
+---+
O   |
    |
    |
   ===''','''
+---+
O   |
|   |
    |
   ===''','''
 +---+
 O   |
/|   |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
 +---+
 O   |
/|\  |
/    |
    ===''','''
 +---+
 O   |
/|\  |
/ \  |
    ===''']
  words = 'pneumonoultramicroscopicsilicovolcanoconiosis supercalifragilisticexpialidocious pseudopseudohypoparathyroidism floccinaucinihilipilification antidisestablishmentarianism honorificabilitudinitatibus hippopotomonstrosesquippedaliophobia sesquipedalophobia thisisaverylongwordthatismeantomakeyoulosediditsucceedihopesobutifyouarereadingthisyouprobablylost hhegoehgoijrejpwojoejfiorneoieoinvrnreoinvoinboenboeinre soeireowimmnvnvmnowierhwgwhwoiehiwoej thyroparathyroidectomized dichlorodifluoromethane incomprehensibilities methionylthreonylthreonylglutaminylarginyltyrosylglutamylserylleucylphenylalanylalanylglutaminylleuc yllysylglutamylarginyllysylglutamylglycylalanylphenylalanylvalylprolylphenylalanylvalylthreonylleucylgl ycylaspartylprolylglycylisoleucylglutamylglutaminOkIShallStop'.split()
  def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList [wordIndex]
  def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
      print(letter, end=' ')
      print()
    blanks = '_ ' * len(secretWord)
    for i in range(len(secretWord)):
      if secretWord[i] in correctLetters:
        blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
      print(letter, end= ' ')
    print()
  def getGuess(alreadyGuessed):
    while True:
      print('Guess a letter.')
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
        print('Please type a single letter.')
      elif guess in alreadyGuessed:
        print('You already entered that number once.')
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('JUST. ONE. LETTER. Come on dude.')
      else:
        return guess
  def playAgain():
    print('Do you want to play again? Enter yes or no.')
    return input().lower().startswith('y')

  print('H A N G M A N')
  missedLetters = ''
  correctLetters = ''
  secretWord = getRandomWord(words)
  gameIsDone = False
  while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
      correctLetters = correctLetters + guess
      foundAllLetters = True
      for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
          foundAllLetters = False
          break
      if foundAllLetters:
        print('Congrats. You have guessed my secret word, ' + secretWord + '. I guess you win.')
        gameIsDone = True
    else:
      missedLetters = missedLetters + guess
      if len(missedLetters) == len(hangmanPics) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed letters and ' + str(len(correctLetters)) + ' correct guesses, the word was \"' + secretWord + '\"')
        gameIsDone = True
    if gameIsDone:
      if playAgain():
        missedLetters = ''
        correctLetters = ''
        gameIsDone = False
        secretWord = getRandomWord(words)
      else:
        break
if username == 'Cookie':
  hangmanPics = ['''
+---+
    |
    |
    |
   ===''','''
+---+
O   |
    |
    |
   ===''','''
+---+
O   |
|   |
    |
   ===''','''
 +---+
 O   |
/|   |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
 +---+
 O   |
/|\  |
/    |
    ===''','''
 +---+
 O   |
/|\  |
/ \  |
    ===''']
  words = 'short lol abc cookie minecraft subscribe'.split()
  def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList [wordIndex]
  def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
      print(letter, end=' ')
      print()
    blanks = '_ ' * len(secretWord)
    for i in range(len(secretWord)):
      if secretWord[i] in correctLetters:
        blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
      print(letter, end= ' ')
    print()
  def getGuess(alreadyGuessed):
    while True:
      print('Guess a letter.')
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
        print('Please type a single letter.')
      elif guess in alreadyGuessed:
        print('You already entered that number once.')
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('JUST. ONE. LETTER.')
      else:
        return guess
  def playAgain():
    print('Do you want to play again? Enter yes or no.')
    return input().lower().startswith('y')

  print('H A N G M A N')
  missedLetters = ''
  correctLetters = ''
  secretWord = getRandomWord(words)
  gameIsDone = False
  while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
      correctLetters = correctLetters + guess
      foundAllLetters = True
      for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
          foundAllLetters = False
          break
      if foundAllLetters:
        print('Congrats. You have guessed my secret word, ' + secretWord + '. I guess you win.')
        gameIsDone = True
    else:
      missedLetters = missedLetters + guess
      if len(missedLetters) == len(hangmanPics) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed letters and ' + str(len(correctLetters)) + ' correct guesses, the word was \"' + secretWord + '\"')
        gameIsDone = True
    if gameIsDone:
      if playAgain():
        missedLetters = ''
        correctLetters = ''
        gameIsDone = False
        secretWord = getRandomWord(words)
      else:
        break