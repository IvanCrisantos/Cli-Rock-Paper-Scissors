from game_data import view_stats
from game_data import game_round


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. Start a Round")
        print("2. View Stats")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("You chose to start a round")
            game_round()
        elif choice == "2":
            print("You chose to view stats")
            view_stats()
        elif choice == "3":
            print("You chose to exit")
            is_running = False
        else:
            print("Invalid choice. Please try again.")
