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
    curses.echo()  # Enable echo mode to see typing
    height, width = stdscr.getmaxyx()
    text = []
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Create a new file")

        # Display existing text
        for idx, line in enumerate(text):
            if idx < height - 2:  # Leave space for header and current line
                stdscr.addstr(idx + 1, 0, f"{idx + 1} {line}")  # Show line number

        # Display line number for new input
        line_number = len(text) + 1  # Next line number
        stdscr.addstr(current_row + 1, 0, f"{line_number} ")  # Display line number followed by a space
        stdscr.move(current_row + 1, len(str(line_number)) + 1)  # Move cursor to the right of the number

        # Get user input
        curses.curs_set(1)  # Show cursor
        new_line = stdscr.getstr(current_row + 1, len(str(line_number)) + 1, width - 1).decode('utf-8')  # Start input after the line number
        curses.curs_set(0)  # Hide cursor

        if new_line == '\x07':  # Ctrl+G to exit
            break

        text.append(new_line)  # Append the new line to text
        current_row += 1  # Move to the next row for the next input

    curses.noecho()  # Disable echo mode
    return text



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
                text = createNewFile(stdscr)
                # Here you can do something with the text, like saving it to a file
                stdscr.clear()
                stdscr.addstr(1, 1, "File created. Content:")
                for idx, line in enumerate(text):
                    stdscr.addstr(idx + 2, 1, line)
                stdscr.addstr(len(text) + 3, 1, "Press any key to continue...")
                stdscr.refresh()
                stdscr.getch()
            elif current_row == 2:
                exitApp(stdscr)
                break  # Exit after the "Exit" option is selected
        showMenu(stdscr, current_row)  # Update the menu on the screen


# Call the wrapper function, which handles terminal setup and cleanup
wrapper(main)