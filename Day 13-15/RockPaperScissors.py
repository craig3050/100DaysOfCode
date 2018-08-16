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
    print(f'computer chooses {computer_choice}')
    if choice.lower() == computer_choice.lower():
        print(f'It\'s a draw, you both choose {computer_choice}')
## computer wins
    elif choice.lower() == 'r' and computer_choice.lower() == 'paper':
        print('The computer chose paper, you lose')
    elif choice.lower() == 'p' and computer_choice.lower() == 'scissors':
        print('The computer chose scissors, you lose')
    elif choice.lower() == 's' and computer_choice.lower() == 'rock':
        print('The computer chose rock, you lose')
## player wins
    elif computer_choice.lower() == 'rock' and choice.lower() == 'p':
        print('The computer chose rock, you win')
    elif computer_choice.lower() == 'paper' and choice.lower() == 's':
        print('The computer chose paper, you win')
    elif computer_choice.lower() == 'scissors' and choice.lower() == 'r':
        print('The computer chose scissors, you win')
    else:
        print('Well I don\'t really know what\'s going on then!!!')

    if input('Do you want to play again?? Y/N') == 'Y' or 'y':
        game_loop()
    else:
        print('OK, good bye!!!')





if __name__ == '__main__':
    main()

