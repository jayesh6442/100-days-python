import random
stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list =  ["jayesh","savan","viral"]
word= random.choice(word_list)
print(word)
    
word_len = len(word)   
display=[]    
for _ in range(word_len):
    display+="_"
print(display)
lives = 6

game_is_over  = False
while not game_is_over:
    guess = input("Enter the guess: ")
    
    for i in range(word_len):
        if word[i]==guess:
            display[i]=guess
    print(display)
    
    if guess not in word:
        lives-=1
        if lives ==0 :
            game_is_over=True
            print("game over you lose")
    
    if "_" not in display:
        game_is_over= True
        print("you win")
    print(stages[lives])