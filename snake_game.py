import random


def roll_dice():
    return random.randint(1, 6)


def play(players):
    scores = [0] * players
    completed_players = 0

    while completed_players < players - 1:
        for i in range(players):
            if scores[i] >= 100:
                continue

            input(f"\nPlayer {i + 1}'s turn. Press Enter to roll the dice...")
            roll = roll_dice()
            scores[i] += roll
            print(f"Player {i + 1} rolled a {roll}. Total score: {scores[i]}")

            # Implement specific score points where the score changes
            if scores[i] == 10:
                print(f"\nPlayer {i + 1} hits a penalty! Score decreases by 5 points.")
                scores[i] -= 5
            elif scores[i] == 25:
                print(f"\nPlayer {i + 1} gets a bonus! Score increases by 10 points.")
                scores[i] += 10
            elif scores[i] == 50:
                print(f"\nPlayer {i + 1} hits a penalty! Score decreases by 10 points.")
                scores[i] -= 10
            elif scores[i] == 75:
                print(f"\nPlayer {i + 1} gets a bonus! Score increases by 20 points.")
                scores[i] += 20

            # Ensure scores do not drop below 0
            if scores[i] < 0:
                scores[i] = 0

            if scores[i] >= 100:
                completed_players += 1
                print(
                    f"\nPlayer {i + 1} reached or exceeded 100 points with a score of {scores[i]}!"
                )

    ranked_players = sorted(
        enumerate(scores, start=1), key=lambda x: x[1], reverse=True
    )

    print("\nFinal Rankings:")
    for position, (player, score) in enumerate(ranked_players, start=1):
        suffix = "th"
        if position == 1:
            suffix = "st"
        elif position == 2:
            suffix = "nd"
        elif position == 3:
            suffix = "rd"
        print(f"{position}{suffix} place: Player {player} with a score of {score}")


def playDice():
    while True:
        try:
            players = int(input("Choose the number of players (2/3/4): "))
            if players >= 2 and players <= 4:
                play(players)
                break
            else:
                print("Invalid input. Please enter 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    query = input("Do you want to play Dice (y/n)? : ").strip().lower()

    if query == "y":
        print("\n\n\t\t__Welcome__\n\t\t")
        playDice()
    else:
        print("Thanks for stopping by!")
        exit()


if __name__ == "__main__":
    main()