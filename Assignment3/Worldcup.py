# Assignment 3: Real world application of loop control statements
# Simulating a country that will win World Cup 2026

import random

teams = {
    "Brazil": 95,
    "Argentina": 93,
    "France": 92,
    "Spain": 90,
    "Germany": 88,
    "England": 87,
    "Portugal": 86,
    "Netherlands": 84
}

print("Welcome to the World Cup 2026 Winner Predictor!")
print("\nTeams and their strength ratings:")
for team, rating in teams.items():
    print(f"  {team}: {rating}")

print("\nCommands: press Enter to run a prediction, 'redo' to run again,")
print("'stop' to exit, or anything else to skip a round.\n")

while True:
    command = input("Enter command: ").strip().lower()

    if command == "stop":
        print("Exiting predictor. Goodbye!")
        break

    elif command == "redo":
        continue

    elif command == "":
        pass  

    else:
        print("Unknown command, skipping this round.")
        continue

    
    team_names = list(teams.keys())
    weights = list(teams.values())
    predicted_winner = random.choices(team_names, weights=weights, k=1)[0]

    print(f"\nPredicted World Cup 2026 winner: {predicted_winner}")
    print(f"(Rating: {teams[predicted_winner]})\n")

    again = input("Run another prediction? (yes/no): ").strip().lower()

    if again == "yes":
        continue
    elif again == "no":
        print("Exiting predictor. Goodbye!")
        break
    else:
        print("Invalid response. Exiting.")
        break
