import random
import os

SCORE_FILE = "high_scores.txt"


# ---------- LOAD HIGH SCORES ----------
def load_scores():
    scores = {"Easy": 0, "Medium": 0, "Hard": 0}

    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                # Skip invalid or empty lines
                if len(parts) == 2:
                    level, score = parts

                    if level in scores:
                        scores[level] = int(score)

    return scores


# ---------- SAVE HIGH SCORE ----------
def save_score(level, score):
    scores = load_scores()

    if score > scores[level]:
        scores[level] = score

        with open(SCORE_FILE, "w") as file:
            for lvl, sc in scores.items():
                file.write(f"{lvl},{sc}\n")


# ---------- GAME LOGIC ----------
def play_game():

    print("\n=== NUMBER GUESSING GAME ===")
    print("1. Easy (1-50) - 10 attempts")
    print("2. Medium (1-100) - 7 attempts")
    print("3. Hard (1-200) - 5 attempts")

    # Input validation for difficulty choice
    try:
        choice = int(input("Choose level: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    # Difficulty settings
    if choice == 1:
        level = "Easy"
        jackpot = random.randint(1, 50)
        max_range = 50
        attempts = 10
        base_score = 100

    elif choice == 2:
        level = "Medium"
        jackpot = random.randint(1, 100)
        max_range = 100
        attempts = 7
        base_score = 200

    elif choice == 3:
        level = "Hard"
        jackpot = random.randint(1, 200)
        max_range = 200
        attempts = 5
        base_score = 300

    else:
        print("❌ Invalid choice!")
        return

    score = base_score

    print(f"\nGuess a number between 1 and {max_range}")
    print(f"You have {attempts} attempts\n")

    # ---------- GUESS LOOP ----------
    while attempts > 0:

        # Input validation for guesses
        try:
            guess = int(input("Enter guess: "))
        except ValueError:
            print("❌ Please enter numbers only!\n")
            continue

        # Range validation
        if guess < 1 or guess > max_range:
            print(f"❌ Enter a number between 1 and {max_range}\n")
            continue

        # Correct guess
        if guess == jackpot:
            print("\n🎉 Correct! You won!")
            print(f"🏆 Score: {score}")

            save_score(level, score)
            return

        # Hint system
        elif guess < jackpot:
            print("⬆ Wrong! Go higher")

        else:
            print("⬇ Wrong! Go lower")

        # Very close hint
        difference = abs(jackpot - guess)

        if difference <= 5:
            print("🔥 Very close!")

        attempts -= 1
        score -= 10

        print(f"Attempts left: {attempts}\n")

    # ---------- GAME OVER ----------
    print("\n💀 Game Over!")
    print(f"The correct number was {jackpot}")
    print("Score: 0")


# ---------- MAIN LOOP ----------
def main():

    while True:

        play_game()

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            break

    # Show high scores
    print("\nThanks for playing!")

    scores = load_scores()

    print("\n🏆 HIGH SCORES:")

    for level, score in scores.items():
        print(f"{level}: {score}")


# ---------- RUN PROGRAM ----------
if __name__ == "__main__":
    main()
