# This file will contain 2 dictionaries, one for the list of paths and the second one for the list of possible extensions for each platform. This will allow the user to add or remove games from the list
# All of this are temporary paths
PS1_GAMES_PATH =  "C:\\Users\\jizos\\Documents\\Emulators\\Roms\\PS1" 
PS1_GAMES_EXTENSION = (".bin", ".cue", ".iso", ".chd") # The extensions of the PS1 games

ARCADE_GAMES_PATH = "C:\\Users\\jizos\\Documents\\Emulators\\Roms\\MAME"
ARCADE_GAMES_EXTENSION = (".zip", ".7z", ".rar") # The extensions of the arcade games

NES_GAMES_PATH = "C:\\Users\\jizos\\Documents\\Emulators\\Roms\\NES"
NES_GAMES_EXTENSION = (".nes") # The extensions of the NES games

GAMES_PATH = {
    'PS1': PS1_GAMES_PATH,
    'NES': NES_GAMES_PATH,
    'Arcade': ARCADE_GAMES_PATH
}

GAMES_EXTENSION = {
    'PS1': PS1_GAMES_EXTENSION,
    'NES': NES_GAMES_EXTENSION,
    'Arcade': ARCADE_GAMES_EXTENSION
}

GAME_COMMANDS = {
    'PS1': 'duckstation',
    'NES': 'nestopia',
    'Arcade': 'mame'
}
