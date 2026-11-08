import random

game_stats = {"wins": 0, "losses": 0, "ties": 0, "total": 0}


def game_round():
    while True:
        user = input("Choose Rock, Paper or Scissors? ").strip().lower()
        options = ["rock", "paper", "scissors"]
        if user not in options:
            print("Invalid Choice. Try Again")
            continue
        computer = random.choice(options)
        game_stats["total"] += 1
        if user == computer:
            print(f"You picked {user}, the computer picked {computer}")
            print("It's a Tie")
            game_stats["ties"] += 1
            break
        elif (
            user == "rock"
            and computer == "scissors"
            or user == "scissors"
            and computer == "paper"
            or user == "paper"
            and computer == "rock"
        ):
            print(f"You picked {user}, the computer picked {computer}")
            print("You Win!!!")
            game_stats["wins"] += 1
            break
        else:
            print(f"You picked {user}, the computer picked {computer}")
            print("You Lose!!!")
            game_stats["losses"] += 1
            break


def view_stats():
    try:
        print("\nCurrent Statistics:")
        print(f"Games Won: {game_stats['wins']}")
        print(f"Games Lost: {game_stats['losses']}")
        print(f"Games Tied: {game_stats['ties']}")
        print(f"Games Played: {game_stats['total']}")
        win_percentage = (game_stats["wins"] / game_stats["total"]) * 100
        print(f"Win Percentage: {win_percentage:.2f}%")
    except ZeroDivisionError:
        print("You did not play a round yet!!")


def final_stats():
    try:
        print("\nFinal Statistics:")
        print(f"Games Won: {game_stats['wins']}")
        print(f"Games Lost: {game_stats['losses']}")
        print(f"Games Tied: {game_stats['ties']}")
        print(f"Games Played: {game_stats['total']}")
        win_percentage = (game_stats["wins"] / game_stats["total"]) * 100
        print(f"Win Percentage: {win_percentage:.2f}%")
    except ZeroDivisionError:
        print("You did not play a round!!")
