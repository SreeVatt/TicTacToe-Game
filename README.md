# TicTacToe
This Python code implements a simple text-based Tic-Tac-Toe game. Tic-Tac-Toe, also known as Noughts and Crosses, is a two-player game where the objective is to be the first to place three of your marks (either "X" or "O") in a row, column, or diagonal on a 3x3 grid.

Description:

Setting up the Game:

The game begins by initializing an empty 3x3 game board represented by a list named board. Initially, all cells are filled with spaces to represent empty spaces.

![image](https://github.com/SreeVatt/TicTacToe-Game/assets/91870603/70687ae8-43e5-473c-99ef-7a1b3fba895a)



The print_board() function is used to display the current state of the game board. It prints the grid layout and shows the positions of the "X" and "O" markers.

![image](https://github.com/SreeVatt/TicTacToe-Game/assets/91870603/5fd25b04-a060-433e-a42c-7e51bdf5b20a)


Checking for a Win:

The check_win(player) function checks if the player has won by examining rows, columns, and diagonals. If a player has three markers in a row, the function returns True, indicating a win for that player.

![image](https://github.com/SreeVatt/TicTacToe-Game/assets/91870603/5177ebae-f399-482b-9937-3c954561b2f6)

Checking for a Draw:

The is_board_full() function checks if the game board is full of markers, indicating a draw. It returns True if there are no more empty spaces.

![image](https://github.com/SreeVatt/TicTacToe-Game/assets/91870603/a293b525-4621-4ab4-963d-3a695919f3be)


Playing the Game:

The game starts with current_player set to "X." Players take turns entering their moves by specifying a position on the board (1-9). The position input is subtracted by 1 to convert it to the correct list index.

The game then checks if the chosen position is empty. If it is, the player's marker is placed in that position. If not, the player is asked to try again.

After each move, the game checks for a win. If a player wins, the game announces the winner and ends. If there's a draw, the game declares it and ends.

The code alternates between players ("X" and "O") after each valid move, making it a two-player game.

Ending the Game:

The game ends when there is a winner or a draw. Players are informed of the outcome, and the program exits.
How to Play:

Run the Python script in a terminal or IDE that supports input.

![image](https://github.com/SreeVatt/TicTacToe-Game/assets/91870603/889571c0-2959-448a-b1fb-382dfe7908b8)


Players take turns entering their moves by specifying a position on the board (1-9). For example, entering "5" will place the current player's marker in the middle of the board.

The game continues until a player wins or the board is full (draw). The winner is announced, or the game ends in a draw. 
