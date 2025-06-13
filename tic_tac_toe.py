def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(space != " " for space in board)

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns to place their marks (X or O) on the board.")
    print("Enter a number from 1 to 9 to place your mark in the corresponding position:")
    print_board([str(i) for i in range(1,10)])

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            if board[move-1] != " ":
                print("That position is already taken. Try again.")
                continue
            board[move-1] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins! Congratulations!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    tic_tac_toe()
