import curses
import random
from curses import wrapper

def start(stdscr):
    #includes commands for displaying the text in the terminal window
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing test where your typing skill will be judged! \n")      #Adds the string to the screen window
    stdscr.addstr("Press any key to begin: ")
    stdscr.refresh()
    stdscr.getkey()  #waits for the user input to execute the program

def test(stdscr):

    # Open and read the file
    with open("sentence.txt", "r", encoding="utf-8") as file:
        sentence = [line.strip() for line in file if line.strip()]

    # Pick a random sentence for typing test
    sentence = random.choice(sentence)
    user_text = []
    stdscr.clear()
    stdscr.addstr(sentence)
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    #for text color
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    start(stdscr)
    test(stdscr)


wrapper(main)
