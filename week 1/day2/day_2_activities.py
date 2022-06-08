# ------ ACTIVITY 1 ------ #
from random import randint as r


def number():
    choice = False
    while choice == False:
        num = input('Choose A Number:   \n')
        if num.isnumeric():
            print(f'You Chose The Number: {num}')
            num = int(num)
            print(type(num))
            choice = True
        else:
            print(f'{num} is not a number!')


number()


# ------ ACTIVITY 2 ------ #
# not mine #


ghost_chars = [
    'Peter Venkman', 'Raymond Stantz', 'Egon Spengler',
    'Winston Zeddemore', 'Dana Barrett', 'Lenny Clotch',
    'Janine Melnitz', 'Louis Tully', 'Walter Peck',
    'Joanne Phillips', 'Sammy Kipper', 'George Washington',
    'Frank Joslin', 'Meryl Campbell', 'John Plisken',
    'John Conner', 'Kyle Reece', 'Sarah Connor'
]
hscore = 0


def ghost_game(char_list):
    p_lives = 3
    p_score = 0
    print('You have 3 lives, would you like to begin? Press enter to continue')
    input()
    while p_lives > 0:
        question = r(0, 17)
        pressed_question = char_list[question]
        print(f'is {pressed_question} in the Ghostbusters film? [Y/N]\n')
        user_answer = input()
        if question <= 8:
            match user_answer.capitalize():
                case 'Y' | "YES":
                    print(f'{pressed_question} is indeed a charater in the movie!')
                    p_score += 1
                case 'N' | "NO":
                    print(f'{pressed_question} is not a charater in the movie!')
                    p_lives -= 1
        else:
            match user_answer.capitalize():
                case 'Y' | "YES":
                    print(f'{pressed_question} is not a charater in the movie!')
                    p_lives -= 1
                case 'N' | "NO":
                    print(f'{pressed_question} is indeed a charater in the movie!')
                    p_score += 1
    print('You have run out of lives! GAME OVER!!!!')
    return p_score


while True:
    score = ghost_game(ghost_chars)
    if score > hscore:
        print(f'New High Score!! {score} Points!')
        hscore = score
    else:
        print(f'High Score remains at  Points!')
    p_continue = input('Play again? Y | N')
    match p_continue.capitalize():
        case 'Y' | 'N':
            print('Starting a new game')
        case 'N' | 'NO':
            print('Have a good day!')
            break
