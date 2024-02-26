import os

# r stands for raw string, which is used to avoid escape characters
DUCKSTATION_PATH = r'C:\Users\jizos\Documents\Emulators\Duckstation' # Duckstation = PS1 emulator
MAME_PATH = r'C:\Users\jizos\Documents\Emulators\MAME' # MAME = Arcade emulator
NES_PATH = r'C:\Users\jizos\Documents\Emulators\NES' # NES = NES emulator

# We will use all of this path 
EMULATORS_COMMANDS = {
    'PS1': 'duckstation -fullscreen --  ',
    'Arcade': 'mame64 ',
    'NES': 'nestopia '
}
EMULATORS_PATH = {
    DUCKSTATION_PATH: EMULATORS_COMMANDS['PS1'],
    MAME_PATH: EMULATORS_COMMANDS['Arcade'],
    NES_PATH: EMULATORS_COMMANDS['NES']
}
