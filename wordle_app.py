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


def find_all_char_positions(word: str, char: str):
    positions = []
    pos = word.find(char)
    while pos != -1:
        positions.append(pos)
        pos = word.find(char, pos + 1)
    return positions


def compare(expected: str, guess: str):
    output = ["_"] * len(expected)
    counted_pos = set()

    if (expected == guess):
        return True

    for index, (expected_char, guess_char) in enumerate(zip(expected, guess)):
        if (expected_char == guess_char):
            output[index] = "*"
            counted_pos.add(index)

    for index, guess_char in enumerate(guess):
        if guess_char in expected and output[index] != "*":
            positions = find_all_char_positions(word=expected, char=guess_char)
            for pos in positions:
                if pos not in counted_pos:
                    output[index] = "-"
                    counted_pos.add(pos)
                    break

    coloured = ""
    for idx, i in enumerate(output):
        if i == '*':
            coloured += white_on_green(guess[idx])
        elif i == "-":
            coloured += white_on_yellow(guess[idx])
        else:
            coloured += white_on_black(guess[idx])
    print(coloured)
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

        if compare(init_word, guess) == True:
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
