import curses
from game_list import games

# Initial state
platforms = list(games.keys())
current_platform_index = 0
current_platform = platforms[current_platform_index]
current_selection = 0

def wrap(min_index, max_index):
    '''
    This function will wrap the index of the selected game so it doesn't go out of bounds

    Example:
    wrap(0, 3)(4) # 0
    wrap(0, 3)(-1) # 3

    Args:
    min_index (int): The minimum index of the list
    max_index (int): The maximum index of the list

    Returns:
    wrapper (function): The function that will wrap the index
    '''
    def wrapper(index):
        if index < min_index:
            return max_index
        elif index > max_index:
            return min_index
        return index
    return wrapper

def draw_menu(stdscr):
    global current_platform, current_selection, platforms, current_platform_index
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(0)  # Make getkey() wait for the user's input
    stdscr.keypad(True)  # Enable keypad mode
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Selected item

    max_visible_games = 10  # Adjust based on your screen size or dynamically calculate

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Adjust the number of visible games based on screen size
        max_visible_games = min(len(games[current_platform]), (height - 3) // 2)

        title = "Game Selector - {0}".format(current_platform)[:width-1]
        subtitle = "Arrow keys navigate games, 'n'/'p' switch platform, 'Enter' to select, 'q' to exit."[:width-1]
        statusbarstr = "Press 'q' to exit | PLATFORM: {0}".format(current_platform)

        start_x_title = (width // 2) - (len(title) // 2)
        start_x_subtitle = (width // 2) - (len(subtitle) // 2)
        start_y = 3  # Start below the title and subtitle (one line down from the subtitle)

        stdscr.addstr(0, start_x_title, title)
        stdscr.addstr(1, start_x_subtitle, subtitle)

        # Calculate the range of games to display
        start_index = max(0, current_selection - max_visible_games // 2)
        end_index = min(len(games[current_platform]), start_index + max_visible_games)
        start_index = max(0, end_index - max_visible_games)  # Adjust start_index if near the end of the list

        for idx, game in enumerate(games[current_platform][start_index:end_index], start=start_index):
            x = (width // 2) - (len(game) // 2)
            y = start_y + (idx - start_index) * 2  # Adjust based on the start_index
            if idx == current_selection:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, game)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, game)

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(height-1, 0, statusbarstr, curses.A_STANDOUT)
        stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()

        k = stdscr.getch()

        if k == ord('q'):
            break
        elif k == curses.KEY_UP:
            current_selection -= 1
            current_selection = wrap(0, len(games[current_platform]) - 1)(current_selection)
        elif k == curses.KEY_DOWN:
            current_selection += 1
            current_selection = wrap(0, len(games[current_platform]) - 1)(current_selection)
        elif k == curses.KEY_ENTER or k in [10, 13]:  # Enter key
            # Placeholder for launching the selected game
            game = games[current_platform][current_selection]
            # TODO: Launch the game
            break  # Or keep the menu open
        elif k == ord('n'):
            current_platform_index = (current_platform_index + 1) % len(platforms)
            current_platform = platforms[current_platform_index]
            current_selection = 0
        elif k == ord('p'):
            current_platform_index = (current_platform_index - 1) % len(platforms)
            current_platform = platforms[current_platform_index]
            current_selection = 0

def init_curses():
    curses.wrapper(draw_menu)
