def print_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        print("|")
        print("---------")


def get_player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            column = int(input("Enter the column (0-2): "))

            if 0 <= row <= 2 and 0 <= column <= 2 and board[row][column] == "-":
                return row, column

            print("Invalid move. Try again.")

        except ValueError:
            print("Invalid input. Try again.")


def is_game_over(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True

    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True

    # Check if the board is full
    for row in board:
        if "-" in row:
            return False

    # If no winner and board is full, it's a tie
    return True


def play_game():
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        row, col = get_player_move(board)
        board[row][col] = current_player

        if is_game_over(board):
            print_board(board)
            if current_player == "X":
                print("Player X wins!")
            elif current_player == "O":
                print("Player O wins!")
            else:
                print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


play_game()
