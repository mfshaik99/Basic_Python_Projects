# Board shows numbers to help players pick their move
board = [str(i+1) for i in range(9)]

def show_positions():
    print("Here’s the board layout. Use these numbers to pick your move:\n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

def display_board():
    print()
    for i in range(3):
        print(f" {board[3*i]} | {board[3*i+1]} | {board[3*i+2]} ")
        if i < 2:
            print("---+---+---")
    print()

def check_if_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def board_is_full():
    return all(space in ['X', 'O'] for space in board)

def start_game():
    current_player = "X"
    
    while True:
        display_board()
        move = input(f"Player {current_player}, pick a number (1-9) to place your mark: ")

        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Oops! Please enter a number from 1 to 9.\n")
            continue

        move = int(move) - 1

        if board[move] in ['X', 'O']:
            print("That spot is already taken. Try a different number.\n")
            continue

        board[move] = current_player

        if check_if_winner(current_player):
            display_board()
            print(f"Congratulations! Player {current_player} wins! 🎉\n")
            break
        elif board_is_full():
            display_board()
            print("It's a tie! Great game! 🤝\n")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Show how the board looks before starting
show_positions()
start_game()
