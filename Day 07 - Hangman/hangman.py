import random

word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

display = ["_" for i in range(len(chosen_word))]

while "_"  in display:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            print(display)
    if guess not in chosen_word:
        lives -= 1
        print(display)
        print(stages[lives])
        if lives == 0:
            print("You lost!")


