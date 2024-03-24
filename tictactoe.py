def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Enter row for " + current_player + " (1-3): "))
            col = int(input("Enter col for " + current_player + " (1-3): "))
            row -= 1
            col -= 1
        except ValueError:
            print("Invalid input, please enter a number between 1 and 3.")
            continue
        except KeyboardInterrupt:
            print("Exiting...")
            return

        if board[row][col] != " ":
            print("That space is already occupied, try again.")
            continue

        board[row][col] = current_player
        if check_win(board):
            print(f"Player {current_player} wins!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

main()