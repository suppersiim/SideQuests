
def illegal_move_check(board,number,row,column):
    
    # row check
    if number in board[row]:
        return True

    # column check
    if number in [board[r][column] for r in range(9)]:
        return True

    # 3x3 block check
    start_row = (row // 3) * 3
    start_col = (column // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == number:
                return True
                
    return False



game_board = [[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ']]
is_over = False

print("Welcome to Sudoku.")
print("For sellecting a box, you must write letter (A, B, C...) followed by a number (1, 2, 3...). For example A1 or B2 or C3 would be all correct moves :)")
print("After selecting a box you have to place a number in that box from one to nine.")
print("Here is the game board:")

total_moves = 81

while not is_over:
    display_board =f"""
        1   2   3   4   5   6   7   8   9
    -----------------------------------------
    A | {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]} || {game_board[0][3]} | {game_board[0][4]} | {game_board[0][5]} || {game_board[0][6]} | {game_board[0][7]} | {game_board[0][8]} |
    .........................................
    B | {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]} || {game_board[1][3]} | {game_board[1][4]} | {game_board[1][5]} || {game_board[1][6]} | {game_board[1][7]} | {game_board[1][8]} |
    .........................................
    C | {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]} || {game_board[2][3]} | {game_board[2][4]} | {game_board[2][5]} || {game_board[2][6]} | {game_board[2][7]} | {game_board[2][8]} |
    .........................................
    D | {game_board[3][0]} | {game_board[3][1]} | {game_board[3][2]} || {game_board[3][3]} | {game_board[3][4]} | {game_board[3][5]} || {game_board[3][6]} | {game_board[3][7]} | {game_board[3][8]} |
    -----------------------------------------
    E | {game_board[4][0]} | {game_board[4][1]} | {game_board[4][2]} || {game_board[4][3]} | {game_board[4][4]} | {game_board[4][5]} || {game_board[4][6]} | {game_board[4][7]} | {game_board[4][8]} |
    .........................................
    F | {game_board[5][0]} | {game_board[5][1]} | {game_board[5][2]} || {game_board[5][3]} | {game_board[5][4]} | {game_board[5][5]} || {game_board[5][6]} | {game_board[5][7]} | {game_board[5][8]} |
    -----------------------------------------
    G | {game_board[6][0]} | {game_board[6][1]} | {game_board[6][2]} || {game_board[6][3]} | {game_board[6][4]} | {game_board[6][5]} || {game_board[6][6]} | {game_board[6][7]} | {game_board[6][8]} |
    .........................................
    H | {game_board[7][0]} | {game_board[7][1]} | {game_board[7][2]} || {game_board[7][3]} | {game_board[7][4]} | {game_board[7][5]} || {game_board[7][6]} | {game_board[7][7]} | {game_board[7][8]} |
    .........................................
    I | {game_board[8][0]} | {game_board[8][1]} | {game_board[8][2]} || {game_board[8][3]} | {game_board[8][4]} | {game_board[8][5]} || {game_board[8][6]} | {game_board[8][7]} | {game_board[8][8]} |
    -----------------------------------------
    """
    print(display_board)
    
    move = input("Sellect a box to place a number: ")
    nr = int(input("Write a number to place in that box: "))
    
    if move[0] == 'A':
        row_nr = 0
    elif move[0] == 'B':
        row_nr = 1
    elif move[0] == 'C':
        row_nr = 2
    elif move[0] == 'D':
        row_nr = 3
    elif move[0] == 'E':
        row_nr = 4
    elif move[0] == 'F':
        row_nr = 5
    elif move[0] == 'G':
        row_nr = 6
    elif move[0] == 'H':
        row_nr = 7
    elif move[0] == 'I':
        row_nr = 8
        
    column_nr = int(move[1])-1
    
    if game_board[row_nr][column_nr] != ' ':
        print("That box is already filled!")
        continue
    
    number_check = illegal_move_check(game_board,nr,row_nr,column_nr)
    if number_check:
        print(f'This in an illegal move! You cannot place number "{nr}" to box "{move}"')
    else:
        game_board[row_nr][column_nr] = nr
        total_moves -= 1
        
    if total_moves == 0:
        break
        
print("Game over.")
print("Well done! You have completed the Sudoku game board!")