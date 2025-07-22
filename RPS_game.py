import random

def play_rps(score, high_score):
    moves = { '1': 'Rock', '2': 'Paper', '3': 'Scissors' }

    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit to Main Menu")
        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '4':
            print("Exiting to main menu...\n")
            break

        if user_choice not in ['1', '2', '3']:
            print("Invalid choice! Please enter a number between 1 and 4.")
            continue

        user_move = moves[user_choice]
        computer_move = random.choice(['Rock', 'Paper', 'Scissors'])

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == 'Rock' and computer_move == 'Scissors') or \
             (user_move == 'Paper' and computer_move == 'Rock') or \
             (user_move == 'Scissors' and computer_move == 'Paper'):
            print("You win!")
            score += 1
            if score >= high_score:
                high_score = score
                print("New Highest Score!")
        else:
            print("You lose!")
            score = 0

        print(f"Current Score: {score}")
        print(f"Highest Score: {high_score}")

    return score, high_score

def game():
    score = 0
    high_score = 0

    while True:
        print("\n" + "*" * 80)
        print(f"Current Score: {score}")
        print(f"Highest Score: {high_score}")
        print("*" * 80)
        print("1. Play Rock-Paper-Scissors")
        print("2. Reset High Score")
        print("3. Exit Game")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            score, high_score = play_rps(score, high_score)

        elif choice == '2':
            score = 0
            high_score = 0
            print("Scores have been reset!")

        elif choice == '3':
            print("Game Over!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

game()
