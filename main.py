import curses
from curses import wrapper

mainMenu = ["Open a file", "Create new file", "Exit"]


def openfolder(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Open a file")
    stdscr.refresh()
    stdscr.getch()  # Wait for user to press a key to go back


def createNewFile(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Create a new file")
    stdscr.refresh()
    stdscr.getch()  # Wait for user to press a key to go back


def exitApp(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Exiting... Press any key to quit.")
    stdscr.refresh()
    stdscr.getch()  # Wait for user to press a key to quit


def showMenu(stdscr, rowSelect):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for index, row in enumerate(mainMenu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(mainMenu) // 2 + index
        if index == rowSelect:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Set up initial state
    current_row = 0
    showMenu(stdscr, current_row)  # Display the initial menu

    while True:
        key = stdscr.getch()

        # Handle navigation keys
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(mainMenu) - 1:
            current_row += 1
        elif key in [10, 13]:  # Enter key (10 is for Linux, 13 for Windows)
            if current_row == 0:
                openfolder(stdscr)
            elif current_row == 1:
                createNewFile(stdscr)
            elif current_row == 2:
                exitApp(stdscr)
                break  # Exit after the "Exit" option is selected

        showMenu(stdscr, current_row)  # Update the menu on the screen


# Call the wrapper function, which handles terminal setup and cleanup
wrapper(main)
