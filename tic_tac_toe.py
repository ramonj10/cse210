'''
File: tic_tac_toe.py
Author: Jesús Ramón

W02: Prove. 
    Code the tic_tac_toe game for two players
'''

from itertools import count
from pickle import FALSE

# List to keep board positions values
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
intent = 0

def main():
    displaygame()
    intent = 0
        
    while board.count('O') < 5:
        play1()
        displaygame()
        if test_win(board, intent):
            break
        intent += 1
        play2()
        displaygame()
        if test_win(board, intent):
            break
        intent += 1

def displaygame():
    '''Display the board game with the actual game positions
    '''
    
    print()
    print(f'\t{board[0]}\t{board[1]}\t{board[2]}')
    print()
    print(f'\t{board[3]}\t{board[4]}\t{board[5]}')
    print()
    print(f'\t{board[6]}\t{board[7]}\t{board[8]}')

def play1():
    '''Invite player one to choose an option
    ''' 
    
    i = True
    while i == True:
        option = input('\nPlayer1 X -Choose a position with any of the available numbers: ')

        if board.count(option) == 1:
            board.remove(option)
            board.insert(int(option) -1, 'X')
            i = False
        else:
            print(f'\nYour option {option} is invalid. \
            \nPlease choose one of the numbers display in the board.')
            displaygame()

def play2():
    '''Invite player two to choose an option
    ''' 
    
    i = True
    while i == True:
        option = input('\nPlayer2 O -Choose a position with any of the available numbers: ')

        if board.count(option) == 1:
            board.remove(option)
            board.insert(int(option) -1, 'O')
            i = False
        else:
            print(f'\nYour option {option} is invalid. \
            \nPlease choose one of the numbers display in the board.')
            displaygame()

def win(board):
    '''Display the win screen
    '''
   
    if board[0] == board[1] and board[1] == board[2]:
        win = board[0]
    elif board[3] == board[4] and board[4] == board[5]:
        win = board[3]   
    elif board[6] == board[7] and board[7] == board[8]:
        win = board[6]   
    elif board[0] == board[4] and board[4] == board[8]:
        win = board[0]   
    elif board[2] == board[4] and board[4] == board[6]:
        win = board[2]   
    elif board[0] == board[3] and board[3] == board[6]:
        win = board[0]   
    elif board[1] == board[4] and board[4] == board[7]:
        win = board[1]   
    elif board[2] == board[5] and board[5] == board[8]:
        win = board[2]   
    else:
        win =''
    
    return win

def test_win(board, intent):
    end = False

    if intent == 8 and win(board) == '':
        print(f'\nTHE GAME ENDS IN A DRAW\n\n')
        end = True

    if intent >= 2:
        if win(board) != '':
            if win(board) == 'X':
                winner = 'PLAYER 1'
                    
            elif win(board) == 'O':
                winner = 'PLAYER 2'
                
            print(f'\nTHE WINNNER IS {winner}\n\n')
            end = True
    
    return end

if __name__ == "__main__":
    main()   