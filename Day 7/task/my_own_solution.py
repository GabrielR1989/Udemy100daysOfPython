import random
import hangman_art
import hangman_words

under_lines_str = ""
wrdTo_guessLetters_list = []
user_letter_guess = ""
ini_lives = len(hangman_art.stages)
left_lives = ini_lives - 1
letter_guessed = False
hang_stage = left_lives

print(hangman_art.logo)

word_to_guess = random.choice(hangman_words.word_list)

for letter in word_to_guess:
    wrdTo_guessLetters_list.append("_")
    under_lines_str += "_"

# print(word_to_guess)
# print(wrdTo_guessLetters_list)
# print(len(word_to_guess))
# print(f"Lives: {left_lives}")

while left_lives >= 0:
    print(f"Word to guess {under_lines_str}")
    user_letter_guess = input("Guess a letter: ").lower()

    for letter in range(len(word_to_guess)):
        if word_to_guess[letter] == user_letter_guess:
            wrdTo_guessLetters_list[letter] = user_letter_guess
            letter_guessed = True

    if letter_guessed:
        under_lines_str = ""
        letter_guessed = False
        for item in wrdTo_guessLetters_list:
            under_lines_str += item
        # print(under_lines_str)
    else:
        if left_lives > 0:
            print(f"You guessed the letter {user_letter_guess}, that\'s not in the word. You lose a life")
            #Print the image
            print(hangman_art.stages[left_lives])
            left_lives -= 1
            print(f"********************{left_lives}/{ini_lives - 1}! LIVES LEFT*******************************************")
        else:
            print(f"You guessed the letter {user_letter_guess}, that\'s not in the word. You don\'t have more lives")
            print(hangman_art.stages[0])
            print(f"********************IT WAS {word_to_guess}! YOU LOSE*******************************************")
            exit()

    if "_" not in wrdTo_guessLetters_list:
        print(f"Correct the word was: \"{word_to_guess}\", YOU WIN")
        exit()
