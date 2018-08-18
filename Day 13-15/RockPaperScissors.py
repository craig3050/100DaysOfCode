import random

def main():
    print('------------------------------')
    print('     -ROCK-PAPER-SCISSORS-')
    print('------------------------------')

    player_name = input('Please Enter Your Name:  ')
    print(f'\n\n Welcome {player_name}')
    print('\n\n')
    game_loop()

def game_loop():
    choice = input('Please choose [R]ock, [P]aper or [S]cissors\n')
    possible_choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(possible_choices)
    print(f'Computer chooses {computer_choice}')
    choice = assign_name(choice)
    if choice == 'unknown':
        print('I have no idea what is going on')
    elif choice == computer_choice:
        print(f'It\'s a draw, you both choose {computer_choice}')
    else:
        winner = who_wins(choice, computer_choice)
        print(f'You {winner}')



# restart loop if yes.
    if input('Do you want to play again?? Y/N') == 'Y' or 'y':
        game_loop()
    else:
        print('OK, good bye!!!')

def assign_name(name):
    if name == ('r' or 'R' or 'Rock' or 'rock'):
        return 'Rock'
    if name == ('s' or 'S' or 'Scissors' or 'scissors'):
        return 'Scissors'
    if name == ('p' or 'P' or 'Paper' or 'paper'):
        return 'Paper'
    else:
        return 'unknown'

def who_wins(choice, computer_choice):
    if choice == 'Rock' and computer_choice == "Paper":
        return 'lose'
    elif choice == 'Paper' and computer_choice == 'Scissors':
        return 'lose'
    elif choice == 'Scissors' and computer_choice == 'Rock':
        return 'lose'
    elif choice == 'Rock' and computer_choice == 'Scissors':
        return 'win'
    elif choice == 'Paper' and computer_choice == 'Rock':
        return 'win'
    elif choice == 'Scissors' and computer_choice == 'Paper':
        return 'win'

if __name__ == '__main__':
    main()

