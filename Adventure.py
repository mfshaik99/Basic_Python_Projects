def intro():
    print("You are in a dark forest. There are two paths ahead.")
    print("Do you go left or right?")
    choice = input("> ").lower()
    
    if choice == "left":
        bear_cave()
    elif choice == "right":
        river_crossing()
    else:
        print("Not a valid choice. Try again.")
        intro()

def bear_cave():
    print("\nYou enter a cave and see a sleeping bear.")
    print("Do you sneak past it or go back?")
    choice = input("> ").lower()

    if choice == "sneak":
        print("\nYou quietly pass the bear and find treasure. You win!")
    elif choice == "back":
        intro()
    else:
        print("Not a valid choice. Try again.")
        bear_cave()

def river_crossing():
    print("\nYou reach a river. There's a boat and a bridge.")
    print("Do you take the boat or the bridge?")
    choice = input("> ").lower()

    if choice == "boat":
        print("\nThe boat leaks and sinks. Game over.")
    elif choice == "bridge":
        print("\nThe bridge leads you safely across. You win!")
    else:
        print("Not a valid choice. Try again.")
        river_crossing()

# Start the game
intro()
