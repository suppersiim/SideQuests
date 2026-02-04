
def win_check(board):
    game_over = False
    
    # rows check
    if board[0].count('X') == 3 or board[1].count('X') == 3 or board[2].count('X') == 3:
        game_over = True
    elif board[0].count('O') == 3 or board[1].count('O') == 3 or board[2].count('O') == 3:
        game_over = True
        
    # columns check
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        game_over = True
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        game_over = True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        game_over = True
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        game_over = True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        game_over = True
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        game_over = True
        
    # diagonals check
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        game_over = True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        game_over = True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        game_over = True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        game_over = True
        
    return game_over
    
        
        
        
is_over = False
game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

whos_move = 'X'
print("Welcome to Tic Tac Toe.")
print("For a correct move you must write letter (A, B or C) followed by a number (1, 2 or 3). For example A1 or B2 or C3 would be all correct moves :)")
print("Here is the game board:")

while not is_over:
    display_board =f"""
        1   2   3
    ---------------
    A | {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]} |
    ---------------
    B | {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]} |
    ---------------
    C | {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]} |
    ---------------
    """
    print(display_board)
    
    move = input("What is your next move: ")
    
    if move[0] == 'A':
        game_board[0][int(move[1])-1] = whos_move
    elif move[0] == 'B':
        game_board[1][int(move[1])-1] = whos_move
    elif move[0] == 'C':
        game_board[2][int(move[1])-1] = whos_move
    
    is_over = win_check(game_board)
    if is_over:
        break
    
    if whos_move == 'X':
        whos_move = 'O'
    else:
        whos_move = 'X'
    
print("Game over!")
print(f"The winner is {whos_move}!")
