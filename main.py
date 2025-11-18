from pyfirmata import Arduino, util, INPUT
import time
board=Arduino('COM4')
it = util.Iterator(board)
it.start()

def inputldr():
    #import modules from Pyfirmata

    # import inbuilt time module

    ldr_pin = 0
    button_pin=7
    board.analog[ldr_pin ].mode = INPUT



    board.analog [ldr_pin ].enable_reporting ()

    sw_val=False

    board.digital[button_pin].mode = INPUT
    board.digital[button_pin].enable_reporting()
    decimallist = []
    print('play!!')


    while sw_val==False  or sw_val==None:
        timeperio = []
        sw_val=board.digital[button_pin].read()
        ldr_val = board.analog [ldr_pin].read () # read the value
        decimallist.append(ldr_val)
        time.sleep (0.0001)





        y = decimallist
        y = y[4:]
        a = b = 0
        isin = False
        for i, j in enumerate(y):
            if j <= 0.01 and not isin:
                isin = True
                a = i
            elif j >= 0.01 and isin:
                isin = False
                b = i
                timeperio.append(b - a)

    time.sleep(3)





    return timeperio

def dec_to_morse(timeperio):
    morse_list=[]#xxxxxxxxxxxxxxxxxx
    for i in timeperio:
        if i>=8.33:
            morse_list.append('-')
        else :
            morse_list.append('.')

    return morse_list


def morse_to_letter(text):#xxxxxxxxxxxxxxxxx

    encrypt= {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
              '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
              '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
              '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
              '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3',
              '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
              '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?',
              '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'}

    return encrypt[''.join(text)]#xxxxxxxxxxxxxxxxxxxxxx



import random

# Define a list of words to use as the secret word
word_list = ["python","arduino","java"]


# Define a function to select a random word from the list
def get_secret_word():
    return random.choice(word_list)


# Define a function to initialize the game state
def initialize_game():
    secret_word = get_secret_word()
    guessed_letters = set()
    incorrect_guesses = 0
    game_over = False
    return secret_word, guessed_letters, incorrect_guesses, game_over


# Define a function to display the current state of the game
def display_game_state(secret_word, guessed_letters, incorrect_guesses):
    # Convert the secret word to a set of characters
    secret_word_set = set(secret_word)

    # Create a list of underscores, with the same length as the secret word
    word_display = ["_" if letter not in guessed_letters else letter for letter in secret_word]

    # Print the word display
    print(" ".join(word_display))

    # Print the number of incorrect guesses
    print(f"Incorrect guesses: {incorrect_guesses}")

    # Print the guessed letters
    guessed_letters_list = sorted(list(guessed_letters))
    print(f"Guessed letters: {' '.join(guessed_letters_list)}")


# Define the main game loop
def game_loop():
    # Initialize the game state
    secret_word, guessed_letters, incorrect_guesses, game_over = initialize_game()

    # Loop until the game is over
    while not game_over:
        # Display the current state of the game
        display_game_state(secret_word, guessed_letters, incorrect_guesses)

        # Get the user's guess
        print('input the morse code of the letter')
        guess=morse_to_letter(dec_to_morse(inputldr()))



        # Check if the guess is correct
        if guess in secret_word:
            guessed_letters.add(guess)

            # Check if the player has won
            if set(secret_word) <= guessed_letters:
                print("Congratulations, you win!")
                game_over = True
        else:
            incorrect_guesses += 1

            # Check if the player has lost
            if incorrect_guesses == 6:
                print("Sorry, you lose!")
                game_over = True


# Start the game


game_loop()