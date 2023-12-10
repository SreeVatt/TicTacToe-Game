# Tic-Tac-Toe Game


board = [' ' for _ in range(9)]


def print_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(' _  _  _')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(' _  _  _')
    print(f'{board[6]} | {board[7]} | {board[8]}')
 
        
def check_win(player):
 
    for i in range(3):
        if (board[i] == board[i+3] == board[i+6] == player) or \
           (board[i*3] == board[i*3+1] == board[i*3+2] == player):
            return True
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False


def is_board_full():
    return ' ' not in board


current_player = 'X'
while True:
    print_board()
    position = int(input(f'Player {current_player}, enter your move (1-9): ')) - 1

    if board[position] == ' ':
        board[position] = current_player

        if check_win(current_player):
            print_board()
            print(f'Player {current_player} wins!')
            break
        elif is_board_full():
            print_board()
            print('The game is a draw!')
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print('Invalid move. Try again.')