import random
from handman_word import word_list
from hangman_art import stages, logo

#Counter to keep track of lives
lives = 6

#Print hangman logo
print(logo)

# Randomly choose a word from the word_list 
#chosen_word = random.choice(handman_word.word_list)
chosen_word = random.choice(word_list)
print(chosen_word)

#Create a placeholder with same no of blansk as the chosen_word eg. _ _ _ _ _ _
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder +="_"
print(placeholder)

#While loop to let user guess again
game_over = False
correct_letters = [] # to store the result after guess

while not game_over:

    #Display how namy lives left
    print(f"********************{lives}/6 LIVES LEFT********************")

    # Ask the user to guess a letter & make it lowercase.
    guess = input("Guess a letter: ").lower()

    #Print the letters users have already used
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    #Display the letter in right position eg. _ a _ _ _ _
    display = ""

    # Check if the letter the user guessed is one of the letters in the chosen_word.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) #letter get's added to the list
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    #If chosen word wrong reduce counter (lives) by 1 and inform user they have lost a life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You loose a life.")
        if lives == 0:
            game_over = True
            print(f"********************IT WAS {chosen_word}! YOU LOSE********************")


    if "_" not in display:
        game_over = True
        print ("********************YOU WIN********************")

    #print ascii art for stages corresponding to current no of lives
    print(stages[lives])