import random

game_stats = {"wins": 0, "losses": 0, "ties": 0}


def view_stats():
    print("\nCurrent Statistics:")
    print(f"Games Won: {game_stats['wins']}")
    print(f"Games Lost: {game_stats['losses']}")
    print(f"Games Tied: {game_stats['ties']}")
    total = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]
    print(f"Total Games: {total}")


def game_round():
    while True:
        user = input("Choose Rock, Paper or Scissor? ").strip().lower()
        options = ["rock", "paper", "scissor"]
        if user not in options:
            print("Invalid Choice. Try Again")
            continue
        computer = random.choice(options).lower()
        if user == computer:
            print(f"You picked {user}, the computer picked {computer}")
            print("It's a tie")
            game_stats["ties"] += 1
            break
        elif (
            user == "rock"
            and computer == "scissor"
            or user == "scissor"
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
