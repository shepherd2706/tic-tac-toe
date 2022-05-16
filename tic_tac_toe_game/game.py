from os import system
from random import randint

def ask_for_symbol():
    while True:
        choice = input('Player 1: Do you want to be X or O?' + '\n' + "Player's 1 choice: ")
        if choice.upper() in ('X', 'O'):
            break
        print('Wrong input! Please try again.')
    return choice.upper()

def ask_for_position():
    position = ''

    while not position.isdigit():
        position = input('Choose your next position: (1-9).' + '\n' + 'Your choice: ')
        if position.isdigit():
            if int(position) in range(1, 10):
                return int(position)
            position = ''
            print('Position out of range!')
        else:
            print('That is not a digit!')

def ask_for_more():
    while True:
        choice = input('Do you want to play again? (Y, N)' + '\n' + 'Your choice: ')
        if choice.upper() == 'Y':
            return True
        elif choice.upper() == 'N':
            return False
        else:
            print('Wrong input!')

def print_table(lst):
    for item in [lst[0:3], lst[3:6], lst[6:9]]:
        print('-------------')
        print('|' + '|'.join(('   ', '   ', '   ')) + '|')
        print('|' + '|'.join((' {} ', ' {} ', ' {} ')).format(*item) + '|')
        print('|' + '|'.join(('   ', '   ', '   ')) + '|')
    print('-------------')

def print_order(var):
    if var == 1:
        print('Player 1 will go first.')
    else:
        print('Player 2 will go first.')

def print_layout():
    print('This is the layout of the game. You have to choose positions like so.')
    print_table(list(range(1, 10)))
    print('Now the game begins!')

def can_insert(lst, pos):
    if not lst[pos] in ('X', 'O'):
        return True
    return False

def check_if_won(lst):
    rows = lst[0:3], lst[3:6], lst[6:9]
    cols = lst[0::3], lst[1::3], lst[2::3]
    diagonals = lst[0::4], lst[2:8:2]

    for row in rows:
        if ''.join(row) in ('XXX', 'OOO'):
            return True
    for col in cols:
        if ''.join(col) in ('XXX', 'OOO'):
            return True
    for diagonal in diagonals:
        if ''.join(diagonal) in ('XXX', 'OOO'):
            return True
    return False

def start():
    print('Welcome to tic tac toe game!!!')

    lst = [' '] * 9
    choice = ask_for_symbol()
    next_turn = randint(1, 2)
    go_on = True
    who_won = 0

    print_order(next_turn)
    print_layout()
    input()
    system('cls')

    while go_on:
        print_table(lst)
        position = ask_for_position() - 1
        while not can_insert(lst, position):
            print('This position is occupied!')
            position = ask_for_position() - 1
        if next_turn == 1:
            lst[position] = choice
            if check_if_won(lst):
                go_on = False
                who_won = 1
            next_turn = 2
        else:
            if choice == 'X':
                lst[position] = 'O'
            else:
                lst[position] = 'X'
            if check_if_won(lst):
                go_on = False
                who_won = 2
            next_turn = 1
        if ' ' not in lst:
            go_on = False
        system('cls')
    print_table(lst)

    if who_won == 1:
        print('Player 1 won!')
    elif who_won == 2:
        print('Player 2 won!')
    else:
        print('Tie game!')


more = True
while more:
    start()
    more = ask_for_more()
    system('cls')
