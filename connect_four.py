
def win_check(board, who):
    rows = len(board)
    cols = len(board[0])

    # check rows
    for r in range(rows):
        for c in range(cols - 3):
            if (board[r][c] == who and board[r][c+1] == who and
                board[r][c+2] == who and board[r][c+3] == who):
                return True

    # check columns
    for c in range(cols):
        for r in range(rows - 3):
            if (board[r][c] == who and board[r+1][c] == who and
                board[r+2][c] == who and board[r+3][c] == who):
                return True

    # check diagonal down-right
    for r in range(rows - 3):
        for c in range(cols - 3):
            if (board[r][c] == who and board[r+1][c+1] == who and
                board[r+2][c+2] == who and board[r+3][c+3] == who):
                return True

    # check diagonal down-left
    for r in range(rows - 3):
        for c in range(3, cols):
            if (board[r][c] == who and board[r+1][c-1] == who and
                board[r+2][c-2] == who and board[r+3][c-3] == who):
                return True

    return False


def place_button(board, who, nr):
    col = nr - 1
    rows = len(board)
    cols = len(board[0])

    if not (0 <= col < cols):
        return False

    for r in range(rows - 1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = who
            return True

    return False

            
game_board = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
is_over = False
whos_move = 'X'

print("Welcome to Connect Four!")
print("The aim of the game is to successfully connect 4 buttons in a row (can also be in diagonal).")
print(f'Good luck, the player with "{whos_move}" button starts.')

while not is_over:
    
    display_board =f"""
            1   2   3   4   5   6   7   8   9   10
        -------------------------------------------
        A | {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]} | {game_board[0][3]} | {game_board[0][4]} | {game_board[0][5]} | {game_board[0][6]} | {game_board[0][7]} | {game_board[0][8]} | {game_board[0][9]} |
        -------------------------------------------
        B | {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]} | {game_board[1][3]} | {game_board[1][4]} | {game_board[1][5]} | {game_board[1][6]} | {game_board[1][7]} | {game_board[1][8]} | {game_board[1][9]} |
        -------------------------------------------
        C | {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]} | {game_board[2][3]} | {game_board[2][4]} | {game_board[2][5]} | {game_board[2][6]} | {game_board[2][7]} | {game_board[2][8]} | {game_board[2][9]} |
        -------------------------------------------
        D | {game_board[3][0]} | {game_board[3][1]} | {game_board[3][2]} | {game_board[3][3]} | {game_board[3][4]} | {game_board[3][5]} | {game_board[3][6]} | {game_board[3][7]} | {game_board[3][8]} | {game_board[3][9]} |
        -------------------------------------------
        E | {game_board[4][0]} | {game_board[4][1]} | {game_board[4][2]} | {game_board[4][3]} | {game_board[4][4]} | {game_board[4][5]} | {game_board[4][6]} | {game_board[4][7]} | {game_board[4][8]} | {game_board[4][9]} |
        -------------------------------------------
        F | {game_board[5][0]} | {game_board[5][1]} | {game_board[5][2]} | {game_board[5][3]} | {game_board[5][4]} | {game_board[5][5]} | {game_board[5][6]} | {game_board[5][7]} | {game_board[5][8]} | {game_board[5][9]} |
        -------------------------------------------
        G | {game_board[6][0]} | {game_board[6][1]} | {game_board[6][2]} | {game_board[6][3]} | {game_board[6][4]} | {game_board[6][5]} | {game_board[6][6]} | {game_board[6][7]} | {game_board[6][8]} | {game_board[6][9]} |
        -------------------------------------------
        H | {game_board[7][0]} | {game_board[7][1]} | {game_board[7][2]} | {game_board[7][3]} | {game_board[7][4]} | {game_board[7][5]} | {game_board[7][6]} | {game_board[7][7]} | {game_board[7][8]} | {game_board[7][9]} |
        -------------------------------------------
        I | {game_board[8][0]} | {game_board[8][1]} | {game_board[8][2]} | {game_board[8][3]} | {game_board[8][4]} | {game_board[8][5]} | {game_board[8][6]} | {game_board[8][7]} | {game_board[8][8]} | {game_board[8][9]} |
        -------------------------------------------
        J | {game_board[9][0]} | {game_board[9][1]} | {game_board[9][2]} | {game_board[9][3]} | {game_board[9][4]} | {game_board[9][5]} | {game_board[9][6]} | {game_board[9][7]} | {game_board[9][8]} | {game_board[9][9]} |
        -------------------------------------------
        """
    print(display_board)
    
    move = int(input("What's your next move: "))
    
    placed = place_button(game_board, whos_move, move)
    if not placed:
        print("Invalid move, try again.")
        continue
    
    is_over = win_check(game_board, whos_move)
    
    if is_over:
        break
    
    if whos_move == 'X':
        whos_move = 'O'
    else:
        whos_move = 'X'
        
display_board =f"""
            1   2   3   4   5   6   7   8   9   10
        -------------------------------------------
        A | {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]} | {game_board[0][3]} | {game_board[0][4]} | {game_board[0][5]} | {game_board[0][6]} | {game_board[0][7]} | {game_board[0][8]} | {game_board[0][9]} |
        -------------------------------------------
        B | {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]} | {game_board[1][3]} | {game_board[1][4]} | {game_board[1][5]} | {game_board[1][6]} | {game_board[1][7]} | {game_board[1][8]} | {game_board[1][9]} |
        -------------------------------------------
        C | {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]} | {game_board[2][3]} | {game_board[2][4]} | {game_board[2][5]} | {game_board[2][6]} | {game_board[2][7]} | {game_board[2][8]} | {game_board[2][9]} |
        -------------------------------------------
        D | {game_board[3][0]} | {game_board[3][1]} | {game_board[3][2]} | {game_board[3][3]} | {game_board[3][4]} | {game_board[3][5]} | {game_board[3][6]} | {game_board[3][7]} | {game_board[3][8]} | {game_board[3][9]} |
        -------------------------------------------
        E | {game_board[4][0]} | {game_board[4][1]} | {game_board[4][2]} | {game_board[4][3]} | {game_board[4][4]} | {game_board[4][5]} | {game_board[4][6]} | {game_board[4][7]} | {game_board[4][8]} | {game_board[4][9]} |
        -------------------------------------------
        F | {game_board[5][0]} | {game_board[5][1]} | {game_board[5][2]} | {game_board[5][3]} | {game_board[5][4]} | {game_board[5][5]} | {game_board[5][6]} | {game_board[5][7]} | {game_board[5][8]} | {game_board[5][9]} |
        -------------------------------------------
        G | {game_board[6][0]} | {game_board[6][1]} | {game_board[6][2]} | {game_board[6][3]} | {game_board[6][4]} | {game_board[6][5]} | {game_board[6][6]} | {game_board[6][7]} | {game_board[6][8]} | {game_board[6][9]} |
        -------------------------------------------
        H | {game_board[7][0]} | {game_board[7][1]} | {game_board[7][2]} | {game_board[7][3]} | {game_board[7][4]} | {game_board[7][5]} | {game_board[7][6]} | {game_board[7][7]} | {game_board[7][8]} | {game_board[7][9]} |
        -------------------------------------------
        I | {game_board[8][0]} | {game_board[8][1]} | {game_board[8][2]} | {game_board[8][3]} | {game_board[8][4]} | {game_board[8][5]} | {game_board[8][6]} | {game_board[8][7]} | {game_board[8][8]} | {game_board[8][9]} |
        -------------------------------------------
        J | {game_board[9][0]} | {game_board[9][1]} | {game_board[9][2]} | {game_board[9][3]} | {game_board[9][4]} | {game_board[9][5]} | {game_board[9][6]} | {game_board[9][7]} | {game_board[9][8]} | {game_board[9][9]} |
        -------------------------------------------
        """
print(display_board)

print("Game over.")
print(f'The player with "{whos_move}" buttons won.')
