import random

MIN_NUM = 1
MAX_NUM = 20
CHANCES = 5

LEVELS = {
    'easy': 3,
    'medium': 2,
    'difficult': 1
}


def play_again():
    user_option = input('Do you want to play again? (yes/no)').lower()
    while user_option not in ['yes', 'no']:
        user_option = input(
            'Please enter "yes" to play again or "no" to quit: ').lower()
    return user_option == 'yes'


def choose_level():
    level_input = input(f"Choose a level: {' '.join(LEVELS.keys())}").lower()
    while level_input not in LEVELS:
        level_input = input('Please enter a valid level: ').lower()
    return LEVELS[level_input]


def display_remaining_chances(chance):
    remaining_chances = chance - 1
    print(
        f"You have {remaining_chances} chance{'s' if remaining_chances != 1 else ''} remaining.")


def main():
    print('''Welcome to the Number Guessing Game!
You need to choose a number between 1 and 20.
We have 3 difficulty levels: easy, medium, and difficult.''')

    random_num = random.randint(MIN_NUM, MAX_NUM)
    chances = CHANCES * choose_level()
    print(
        f'Guess the number between {MIN_NUM} and {MAX_NUM}. You have {chances} chances to get it right.')

    while chances > 0:
        try:
            user_guess = int(input('Enter a number: '))

            if user_guess == random_num:
                print('Congratulations! You made it 🎉🎉')
                if play_again():
                    random_num = random.randint(MIN_NUM, MAX_NUM)
                    chances = CHANCES * choose_level()
                    print(
                        f'Guess the number between {MIN_NUM} and {MAX_NUM}. You have {chances} chances to get it right.')
                else:
                    break
            elif user_guess < random_num:
                print('Too low!')
            else:
                print('Too high!')

            display_remaining_chances(chances)
            chances -= 1

        except ValueError:
            print(f'Enter a valid number between {MIN_NUM} and {MAX_NUM}')

    print(f'Game over! Thanks for playing. The number was {random_num}')
    if play_again():
        return main()
    else:
        print('See you soon 🙏')


if __name__ == '__main__':
    main()
