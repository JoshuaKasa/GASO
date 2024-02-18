import os
from game_path import GAMES_PATH, GAMES_EXTENSION

# Recursively search for all files in the games directories and all the subdirectories
def get_game_list() -> dict:
    console_games = {}
    for platform, path in GAMES_PATH.items():
        # Check if the path exists, if not, print a warning and add N/A to the list
        if not os.path.exists(path):
            print(f'Watch out! The path for {platform} does not exist.')
            console_games[platform] = ['N/A'] # Add N/A to the list

            continue # Skip to the next iteration

        # Get all the files in the directory and subdirectories
        games = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(GAMES_EXTENSION[platform]):
                    games.append(file.split('.')[0]) # Remove the extension from the file name
        console_games[platform] = games

    # Right here we could also turn this into a set and then back into a list to remove duplicates
    # console_games = {platform: list(set(games)) for platform, games in console_games.items()}
    return console_games

# List of all the games
games = get_game_list() 

if __name__ == "__main__":
    print(games)
