import random
from wordle_constants import NUMBER_OF_GUESSES_ALLOWED, WORD_LIST
from color_coverter import white_on_green, black_on_gray, white_on_black, white_on_yellow


def get_word():
    """Return a word randomly chosen from word_list."""
    return random.choice(WORD_LIST).upper()


def get_guess(guess_number):
    return input(f'Enter your #{guess_number} : ').upper().strip()


def validate_guess(guess: str, length: int):
    if len(guess) == length:
        return True

    return False


def process_word(init_word: str, guess: str):
    if init_word == guess:
        print(white_on_green(guess))
        return True

    colored_str = ''
    for idx, letter in enumerate(guess):
        if guess[idx] == init_word[idx]:
            colored_str += white_on_green(guess[idx])
        elif guess[idx] in init_word:
            colored_str += white_on_yellow(guess[idx])
        else:
            colored_str += black_on_gray(guess[idx])

    print(colored_str)
    return False


def play():
    init_word = get_word()
    count = 0
    is_gessed_correctly = False

    print('Welcome to Wordle!')
    print(f'Start guessing a {len(init_word)} letter word')
    while count < NUMBER_OF_GUESSES_ALLOWED:
        guess = get_guess(count + 1)

        # Validating User Guess
        if validate_guess(guess, len(init_word)) == False:
            print('Invalid guess, please try again!')
            continue

        # Increment the count
        print(f'You\'ve entered : {guess}')
        count += 1

        # Process Wordle
        if process_word(init_word, guess) == True:
            is_gessed_correctly = True
            print('Congratulations!!! You\'ve guessed it right... ')
            break
        else:
            print('Oops! Wrong Guess. Please try again... ')

    if is_gessed_correctly == False:
        print('Sorry you haven\'t found the correct guess... ')

    shouldContinue = input(
        'Would you like to continue playing? Press Y to continue. N to Exit : ')
    if shouldContinue.upper() == 'Y':
        play()
    else:
        exit(1)
