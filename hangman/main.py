import random
from hangman_words import word_list
from hangman_art import logo, stages

def initialize_display(word_length):
    """Initialize the display list with underscores."""
    return ["_" for _ in range(word_length)]

def update_display(display, chosen_word, guess):
    """Update the display list with the guessed letter."""
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

def main():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = initialize_display(word_length)
    lives = 6
    end_of_game = False

    print(logo)
    # Uncomment the following line to reveal the chosen word (useful for debugging)

    #print(f'Pssst, the solution is {chosen_word}.')

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed '{guess}'.")
            continue

        if guess in chosen_word:
            update_display(display, chosen_word, guess)
        else:
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win!")

        print(stages[lives])

if __name__ == "__main__":
    main()
