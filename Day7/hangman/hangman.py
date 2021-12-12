import random
import hangman_art
import word_list
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

print(hangman_art.logo)

#word_list = ['ability','able','about','above']


random_word = random.choice(word_list.word_list)
print(f"random word: {random_word}")
word_length = len(random_word)

guess_list=[]
for _ in range(word_length):
    guess_list.append('_')
print(guess_list)
Total_lives = len(hangman_art.stages)-1
end_game = False
while not end_game:
    user_input = input('Please guess one letter at a time \n').lower()
    if user_input in guess_list:
        print(f"You entered again {user_input} letter and you loss on lives")
        Total_lives -= 1
        if Total_lives == 0:
            print("you lose")
            end_game = True
    for position in range(word_length):
        letter = random_word[position]
        if letter == user_input:
            guess_list[position] = letter

    if user_input not in random_word:
        print(f"You guessed {user_input} letter not in the list and you loss the live ")
        Total_lives -= 1
        if Total_lives == 0:
            print("you lose")
            end_game = True


#    print(Total_lives)
    clear()
    print(hangman_art.stages[Total_lives])
    print(guess_list)

    if "_" not in guess_list:
        end_game = True
        print(f"Random word chosen is {''.join(guess_list)}")
        print("you Win")
print("end game")