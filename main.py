from random import randint, choice
from os import system


SYMBOLS = ['O', 'X'] 


def clear_screen():
    system("cls")


def pause_screen():
    input("Press any key... ")


def print_screen(user_symbol: str, board: list):
    clear_screen()
    print(f"[~] You are:{user_symbol}")
    for i in range(0, 7, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i != 6:
            print("-" * 11)
  

def is_valid_input(user_move: str, board: list) -> bool:
    if user_move.isdigit() and 0 < int(user_move) < 10:
            user_move = int(user_move) - 1
            if board[user_move] == ' ':
                return True
    return False


def make_move(user_move: int, p1_symbol: str, p2_symbol: str, board: list):
    board[user_move] = p1_symbol
    computer_choice = randint(0, 8)
    if ' ' in board and not check_winner(board):
        while board[computer_choice] != ' ':
            computer_choice = randint(0, 8)
        board[computer_choice] = p2_symbol


def check_vertical_win(board):
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ' ':
            return board[i]


def Check_horizontal_win(board):
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != ' ':
            return board[i]


def Check_diagonal_win(board):
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    elif board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]


def check_winner(board: list): 
    winner = None
    vertical_win = check_vertical_win(board)
    horizontal_Win = Check_horizontal_win(board)
    diagnoal_win = Check_diagonal_win(board)

    if vertical_win in SYMBOLS:
        winner = vertical_win
    elif horizontal_Win in SYMBOLS:
        winner = horizontal_Win
    elif diagnoal_win in SYMBOLS:
        winner = diagnoal_win
    elif not ' ' in board and not winner:
        winner = 'Draw'
    return winner
    

def main():
    # game configuration
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    user_symbol = choice(SYMBOLS)
    computer_symbol = 'O' if user_symbol == 'X' else 'X'

    for move in range(9):
        print_screen(user_symbol, board=board)
        
        # game
        user_move = input("[?] Pick a move: ") 
        if is_valid_input(user_move, board):
            user_move = int(user_move) - 1
        else:
            print("[!] invalid input or this place already taken!")
            pause_screen()
            continue

        make_move(user_move, p1_symbol=user_symbol, p2_symbol=computer_symbol, board=board)
        winner = check_winner(board=board)
        if winner:
            break
        
        

    print_screen(user_symbol, board=board)
    print(f"[~] Game result: {winner}")
    pause_screen()

if __name__ == '__main__':
    main()
