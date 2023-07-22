import random
word_list = ["mami","babi","shkolla","rruga","qeni","macja"]
win = False

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
word = random.choice(word_list)
display = []
game_over = False
for i in range(0,len(word)):
    display.append('_')
while not game_over:
    letter = str.lower(input("Vendos nje shkronje: "))
    correct = False
    for i in range(0,len(word)):
        if word[i] == letter:
            display[i] = letter
            correct = True
    print(display)
    if correct == False:
        lives = lives - 1 
    print(correct)
    print(stages[lives])

    if '_' not in display:
        win = True
        game_over = True
    if lives == 0:
        win = False
        game_over = True 
else:
    if win:
        print("You won")
    else:
        print("You lost")



