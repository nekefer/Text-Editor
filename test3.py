import curses




def main(stdscr):
   stdscr.clear()
   stdscr.addstr('Click on the screen...')


   curses.mousemask(curses.ALL_MOUSE_EVENTS)


   while True:
       key = stdscr.getch()


       if key == ord('q'):
           break


       elif key == curses.KEY_MOUSE:
           _, mx, my, _, _ = curses.getmouse()


           stdscr.clear()
           stdscr.addstr(f'You clicked at {my}, {mx}')




curses.wrapper(main)