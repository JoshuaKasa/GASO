import ctypes
import win32gui
import win32con
import time

from game_launcher import init_curses

# Constants
VK_F11 = 0x7A
METRICS_WIDTH = 0
METRICS_HEIGHT = 1
STD_OUTPUT_HANDLE = -11

def press_key(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)

def release_key(key):
    ctypes.windll.user32.keybd_event(key, 0, 2, 0)

def press_and_release_key(key, duration):
    press_key(key)
    time.sleep(duration)
    release_key(key)

def move_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

def is_truly_fullscreen(hwnd):
    # Get the screen size
    screen_width = ctypes.windll.user32.GetSystemMetrics(METRICS_WIDTH) # 0 for width
    screen_height = ctypes.windll.user32.GetSystemMetrics(METRICS_HEIGHT) # 1 for height

    # Get the window size and position
    window_rect = win32gui.GetWindowRect(hwnd)
    window_width = window_rect[2] - window_rect[0] # 2 - 0 for width
    window_height = window_rect[3] - window_rect[1] # 3 - 1 for height

    # Check if the window is at the top-left corner and covers the entire screen
    is_fullscreen = (window_rect[0] == 0 and
                     window_rect[1] == 0 and
                     window_width == screen_width and
                     window_height == screen_height)
    return is_fullscreen

def hide_terminal_scrollbar():
    # Get handle to the console
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    # Define required structures
    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class SMALL_RECT(ctypes.Structure):
        _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short),
                    ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]

    class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
        _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD),
                    ("wAttributes", ctypes.c_ushort), ("srWindow", SMALL_RECT),
                    ("dwMaximumWindowSize", COORD)]

    # Get current console screen buffer info
    csbi = CONSOLE_SCREEN_BUFFER_INFO()
    ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, ctypes.byref(csbi))

    # Adjust buffer size to match window size
    window_height = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
    window_width = csbi.srWindow.Right - csbi.srWindow.Left + 1
    buffer_size = COORD(window_width, window_height)
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(handle, buffer_size)

def main() -> None:
    # Checking if the terminal is fullscreen
    # If not, then we need to press F11 to make it fullscreen
    key = 0x7A  # F11
    duration = 0.1

    hwnd = win32gui.GetForegroundWindow()
    if not is_truly_fullscreen(hwnd): # If the terminal is not fullscreen
        press_and_release_key(key, duration) # Pressing F11 to make it fullscreen

    # Hiding the terminal scrollbar
    hide_terminal_scrollbar()

    # Putting the mouse out of the way (down right)
    move_mouse(
        ctypes.windll.user32.GetSystemMetrics(METRICS_WIDTH) - 1,
        ctypes.windll.user32.GetSystemMetrics(METRICS_HEIGHT) - 1
    )

    # Starting the game launcher
    init_curses()

if __name__ == "__main__":
    main()
