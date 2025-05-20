import random 

def game():
    score = 0
    high_score = 0

    while True:
        print("********************************************************************************************************************************")
        print(f"Current Score: {score}")
        print(f"Highest Score: {high_score}")
        print("********************************************************************************************************************************")
        print("1. Play Rock-Paper-Scissors")
        print("2. Reset High Score")
        print("3. Exit Game")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nChoose your move:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            user_choice = input("Enter your choice (1-3): ")

            if user_choice not in ['1', '2', '3']:
                print("Invalid choice! Please enter a number between 1 and 3.")
                continue

            moves = { '1': 'Rock', '2': 'Paper', '3': 'Scissors' }
            user_move = moves[user_choice]
            computer_move = random.choice(['Rock', 'Paper', 'Scissors'])

            print(f"\nYou chose: {user_move}")
            print(f"Computer chose: {computer_move}")

            # Determine the winner
            if user_move == computer_move:
                print("It's a tie!")
            elif (user_move == 'Rock' and computer_move == 'Scissors') or \
                 (user_move == 'Paper' and computer_move == 'Rock') or \
                 (user_move == 'Scissors' and computer_move == 'Paper'):
                print("You win!")
                score += 1
                if score >= high_score:  # Changed operator to >=
                    high_score = score
                    print("New Highest Score!")
            else:
                print("You lose!")
                score = 0  # Reset current score on loss

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
