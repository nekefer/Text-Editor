import curses
from curses import wrapper

mainMenu = ["Open a file", "Create new file", "Exit"]

class GapBuffer:
    def __init__(self, init_size=100):
        self.buffer = [' '] * init_size
        self.gap_start = 0
        self.gap_end = init_size

    def insert(self, char):
        if self.gap_end == self.gap_start:
            self.grow()
        self.buffer[self.gap_start] = char
        self.gap_start += 1

    def delete(self):
        if self.gap_start > 0:
            self.gap_start -= 1

    def move_gap(self, new_pos):
        if new_pos < self.gap_start:
            while new_pos < self.gap_start:
                self.gap_start -= 1
                self.gap_end -= 1
                self.buffer[self.gap_end] = self.buffer[self.gap_start]
        else:
            while new_pos > self.gap_start:
                self.buffer[self.gap_start] = self.buffer[self.gap_end]
                self.gap_start += 1
                self.gap_end += 1

    def grow(self):
        new_size = len(self.buffer) * 2
        new_buffer = self.buffer[:self.gap_start] + [' '] * (new_size - len(self.buffer)) + self.buffer[self.gap_end:]
        self.buffer = new_buffer
        self.gap_end = new_size - (len(self.buffer) - self.gap_end)

    def get_text(self):
        return ''.join(self.buffer[:self.gap_start] + self.buffer[self.gap_end:])

def openfolder(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Open a file")
    stdscr.refresh()
    stdscr.getch()  # Wait for user to press a key to go back

def createNewFile(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    text = [GapBuffer()]
    current_row, current_col = 0, 0
    top_line = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Create a new file (Ctrl+G: save, Ctrl+C: exit)")
        #col row
        curses.mousemask(curses.ALL_MOUSE_EVENTS)

        # Display text
        for idx, line in enumerate(text[top_line:top_line+height-2]):
            display_line = idx + top_line
            if idx < height - 2:  # Leave space for header and current line
                stdscr.addstr(idx + 1, 0, f"{display_line + 1:<4}{line.get_text()}")

        # Move cursor
        cursor_row = current_row - top_line + 1
        stdscr.move(cursor_row, current_col + 4)  # +4 for line number

        stdscr.refresh()
        key = stdscr.getch()




        if key == ord('\n'):  # Enter
            new_line = GapBuffer()
            if current_col < len(text[current_row].get_text()):
                text.insert(current_col+1, new_line)
            else:
                text.insert(current_row + 1, new_line)
            current_row += 1
            current_col = 0
        elif key == curses.KEY_UP and current_row > 0:
            current_row -= 1
            current_col = min(current_col, len(text[current_row].get_text()))
        elif key == curses.KEY_DOWN and current_row < len(text) - 1:
            current_row += 1
            current_col = min(current_col, len(text[current_row].get_text()))
        elif key == curses.KEY_LEFT and current_col > 0:
            current_col -= 1
        elif key == curses.KEY_RIGHT and current_col < len(text[current_row].get_text()):
            current_col += 1
        elif key == 7:  # Ctrl+G to save and exit
            break
        elif key == 3:  # Ctrl+C to exit without saving
            text = [GapBuffer()]
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8): # Backspace
            if current_col > 0:
                text[current_row].move_gap(current_col)
                text[current_row].delete()
                current_col -= 1
            elif current_row > 0:
                current_row -= 1
                current_col = len(text[current_row].get_text())
                text[current_row].move_gap(current_col)
                text[current_row].insert('\n')
                text.pop(current_row + 1)
        elif 32 <= key <= 126:  # Printable ASCII characters
            text[current_row].move_gap(current_col)
            text[current_row].insert(chr(key))
            current_col += 1
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()

            my -= 1  # Subtract 1 for the header
            mx -= 3  # Subtract 3 for the line number (3 characters for line numbering)

            # Determine the row based on the mouse click position
            if 0 <= my < len(text):
                current_row = my  # Set current_row based on the clicked line

                # Set current_col based on the clicked position in the line
                if mx >= 0:
                    current_col = min(mx, len(text[current_row].get_text()))  # Ensure current_col does not exceed line length
                else:
                    current_col = 0  # If clicked before the line, set to the start of the line



        # Adjust top_line if cursor is out of view
        if current_row < top_line:
            top_line = current_row
        elif current_row >= top_line + height - 2:
            top_line = current_row - height + 3

    return [line.get_text() for line in text]

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
    curses.curs_set(1)  # Show cursor
    current_row = 0
    showMenu(stdscr, current_row)  # Display the initial menu
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(mainMenu) - 1:
            current_row += 1
        elif key in [10, 13]:  # Enter key (10 is for Linux, 13 for Windows)
            if current_row == 0:
                openfolder(stdscr)
            elif current_row == 1:
                text = createNewFile(stdscr)
                stdscr.clear()
                stdscr.addstr(1, 1, "File created. Content:")
                for idx, line in enumerate(text):
                    stdscr.addstr(idx + 2, 0, line)
                stdscr.addstr(len(text) + 3, 1, "Press any key to continue...")
                stdscr.refresh()
                stdscr.getch()
            elif current_row == 2:
                exitApp(stdscr)
                break  # Exit after the "Exit" option is selected
        showMenu(stdscr, current_row)  # Update the menu on the screen

# Call the wrapper function, which handles terminal setup and cleanup
wrapper(main)