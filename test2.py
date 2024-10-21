import curses

def createNewFile(stdscr):
    stdscr.clear()
    curses.echo()  # Enable echo mode to see typing
    height, width = stdscr.getmaxyx()
    text = []
    current_row = 0
    top_line = 0  # The first line displayed in the viewport

    # Enable mouse support
    curses.mousemask(curses.ALL_MOUSE_EVENTS)

    while True:
        stdscr.clear()

        # Draw the header and instructions
        stdscr.addstr(0, 1, "Create a new file (Ctrl+G: save, ↑/↓: navigate, Mouse scroll: scroll, Ctrl+C: exit)")

        # Display existing text within the viewport
        for idx, line in enumerate(text[top_line:top_line + height - 3]):  # Subtract extra space for header and scroll timeline
            display_line = idx + top_line
            stdscr.addstr(idx + 1, 1, f"{display_line + 1:<4}{line}")

        # Determine where to place the cursor for new input
        cursor_row = min(current_row - top_line + 1, height - 3)

        # Display line number for new input if at the end of the text
        if current_row == len(text):
            stdscr.addstr(cursor_row, 1, f"{current_row + 1:<4}")

        stdscr.move(cursor_row, 5)  # Move cursor to the right of the line number

        # Draw the scroll timeline on the far right
        if len(text) > height - 2:  # If content is larger than the screen height
            timeline_height = height - 3  # Space for the scroll timeline
            scroll_indicator_height = max(1, int(timeline_height * (timeline_height / len(text))))
            scroll_position = int((timeline_height * top_line) / len(text))

            # Render the scroll timeline
            for i in range(timeline_height):
                if i == scroll_position:
                    stdscr.addstr(i + 1, width - 1, '█')  # Scrollbar position
                else:
                    stdscr.addstr(i + 1, width - 1, '|')  # Background of the timeline

        # Get user input or mouse event
        curses.curs_set(1)  # Show cursor
        try:
            key = stdscr.getch()

            # Handle mouse events
            if key == curses.KEY_MOUSE:
                _, mx, my, _, bstate = curses.getmouse()
                if bstate & curses.BUTTON4_PRESSED:  # Scroll up (mouse wheel up)
                    if top_line > 0:
                        top_line -= 1
                elif bstate & curses.BUTTON5_PRESSED:  # Scroll down (mouse wheel down)
                    if top_line + height - 3 < len(text):
                        top_line += 1

            elif key == ord('\n'):  # Enter key
                if current_row < len(text):
                    text[current_row] += '\n'
                else:
                    text.append('')
                current_row += 1
            elif key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(text):
                current_row += 1
            elif key == 7:  # Ctrl+G to save and exit
                break
            elif key == 3:  # Ctrl+C to exit without saving
                text = []
                break
            elif key in (curses.KEY_BACKSPACE, 127):  # Backspace
                if current_row < len(text) and text[current_row]:
                    text[current_row] = text[current_row][:-1]
                elif current_row > 0:
                    current_row -= 1
                    text[current_row] = text[current_row][:-1]
            elif 32 <= key <= 126:  # Printable ASCII characters
                if current_row < len(text):
                    text[current_row] += chr(key)
                else:
                    text.append(chr(key))

        except curses.error:
            pass  # Ignore errors from getch() (e.g., interrupted system call)

        # Adjust the viewport if necessary
        if current_row < top_line:
            top_line = current_row
        elif current_row >= top_line + height - 3:
            top_line = current_row - height + 4

        curses.curs_set(0)  # Hide cursor

    curses.noecho()  # Disable echo mode
    return text

# Initialize the curses application
curses.wrapper(createNewFile)



def createNewFile(stdscr):
    stdscr.clear()
    curses.echo()  # Enable echo mode to see typing
    height, width = stdscr.getmaxyx()
    text = []
    current_row = 0
    top_line = 0  # The first line displayed in the viewport

    # Enable mouse support
    curses.mousemask(curses.ALL_MOUSE_EVENTS)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Create a new file (Ctrl+G: save, ↑/↓: navigate, Mouse scroll: scroll, Ctrl+C: exit)")

        # Display existing text within the viewport
        for idx, line in enumerate(text[top_line:top_line + height - 2]):
            display_line = idx + top_line
            if idx < height - 2:  # Leave space for header and current line
                stdscr.addstr(idx + 1, 0, f"{display_line + 1:<4}{line}")

        # Determine where to place the cursor for new input
        cursor_row = min(current_row - top_line + 1, height - 2)

        # Display line number for new input if at the end of the text
        if current_row == len(text):
            stdscr.addstr(cursor_row, 0, f"{current_row + 1:<4}")

        stdscr.move(cursor_row, 4)  # Move cursor to the right of the line number

        # Get user input or mouse event
        curses.curs_set(1)  # Show cursor
        try:
            key = stdscr.getch()

            # Handle mouse events
            if key == curses.KEY_MOUSE:
                _, mx, my, _, bstate = curses.getmouse()
                if bstate & curses.BUTTON4_PRESSED:  # Scroll up (mouse wheel up)
                    if top_line > 0:
                        top_line -= 1
                elif bstate & curses.BUTTON5_PRESSED:  # Scroll down (mouse wheel down)
                    if top_line + height - 2 < len(text):
                        top_line += 1

            elif key == ord('\n'):  # Enter key
                if current_row < len(text):
                    text[current_row] += '\n'
                else:
                    text.append('')
                current_row += 1
            elif key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(text):
                current_row += 1
            elif key == 7:  # Ctrl+G to save and exit
                break
            elif key == 3:  # Ctrl+C to exit without saving
                text = []
                break
            elif key in (curses.KEY_BACKSPACE, 127):  # Backspace
                if current_row < len(text) and text[current_row]:
                    text[current_row] = text[current_row][:-1]
                elif current_row > 0:
                    current_row -= 1
                    text[current_row] = text[current_row][:-1]
            elif 32 <= key <= 126:  # Printable ASCII characters
                if current_row < len(text):
                    text[current_row] += chr(key)
                else:
                    text.append(chr(key))

        except curses.error:
            pass  # Ignore errors from getch() (e.g., interrupted system call)

        # Adjust the viewport if necessary
        if current_row < top_line:
            top_line = current_row
        elif current_row >= top_line + height - 2:
            top_line = current_row - height + 3

        curses.curs_set(0)  # Hide cursor

    curses.noecho()  # Disable echo mode
    return text


# Initialize the curses application
curses.wrapper(createNewFile)
