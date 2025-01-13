import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(size):
    return [["O"] * size for _ in range(size)]

def place_ships(board, num_ships):
    ships = 0
    while ships < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if board[row][col] == "O":
            board[row][col] = "S"
            ships += 1

def get_guess():
    row = int(input("Guess Row: "))
    col = int(input("Guess Col: "))
    return row, col

def main():
    size = 5
    num_ships = 3
    board = create_board(size)
    place_ships(board, num_ships)
    print("Let's play Battleship!")
    print_board(board)

    turns = 5
    while turns > 0:
        guess_row, guess_col = get_guess()
        if board[guess_row][guess_col] == "S":
            print("Congratulations! You sunk my battleship!")
            board[guess_row][guess_col] = "X"
            num_ships -= 1
            if num_ships == 0:
                print("You win!")
                break
        else:
            if board[guess_row][guess_col] == "X":
                print("You already guessed that.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
                turns -= 1
        print_board(board)
        print(f"Turns remaining: {turns}")

    if num_ships > 0:
        print("Game Over. You ran out of turns.")

if __name__ == "__main__":
    main()
    