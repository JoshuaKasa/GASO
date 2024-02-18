import os

# r stands for raw string, which is used to avoid escape characters
DUCKSTATION_PATH = r'C:\Users\jizos\Documents\Emulators\Duckstation' # Duckstation = PS1 emulator
MAME_PATH = r'C:\Users\jizos\Documents\Emulators\MAME' # MAME = Arcade emulator
NES_PATH = r'C:\Users\jizos\Documents\Emulators\NES' # NES = NES emulator

# We will use all of this path 
EMULATORS_COMMANDS = {
    DUCKSTATION_PATH: 'duckstation -fullscreen --  ',
    MAME_PATH: 'mame',
    NES_PATH: 'nes'
}
EMULATORS_PATH = {
    'PS1': EMULATORS_COMMANDS[DUCKSTATION_PATH], 
    'Arcade': EMULATORS_COMMANDS[MAME_PATH],
    'NES': EMULATORS_COMMANDS[NES_PATH]
}
