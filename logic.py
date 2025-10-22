import curses
import random
from curses import wrapper
import time

def start(stdscr):
    #includes commands for displaying the text in the terminal window
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing test where your typing skill will be judged! \n")      #Adds the string to the screen window
    stdscr.addstr("Press any key to begin: ")
    stdscr.refresh()
    stdscr.getkey()  #waits for the user input to execute the program
    
def display_text(stdscr,sentence,user_text,wpm = 0):    #Used to overlap the existing text with the user input
    stdscr.addstr(sentence)
    wpm_text = f"wpm : {wpm}"
    for i, char in enumerate(user_text):
        correct_char = sentence[i]
        if (char == correct_char):
            stdscr.addstr(0,i,char,curses.color_pair(1))
        else:
            stdscr.addstr(0,i,char,curses.color_pair(2))
    stdscr.addstr(1,0,wpm_text)
def test(stdscr):

    # Open and read the file
    with open("sentence.txt", "r", encoding="utf-8") as file:
        sentence = [line.strip() for line in file if line.strip()]
    stdscr.clear()
    # Pick a random sentence for typing test
    sentence = random.choice(sentence)
    stdscr.addstr(sentence)
    user_text = []
    

    """for  char in sentence:   #runs loop up until the length of the sentence
        user_text = []
        user_input = stdscr.getkey()
        if user_input == char:
            stdscr.addstr( 0,0,user_input,curses.color_pair(1))
        else:
            stdscr.addstr(0,0,user_input,curses.color_pair(2))
        stdscr.refresh()
        """
       



    start_time = time.time()
    wpm = 0


    while True:
       
        stdscr.clear()
        display_text(stdscr,sentence,user_text,wpm)
        stdscr.refresh()
        key = stdscr.getkey()

        time_elapsed = max(time.time()-start_time,1) #calculate the time passed and returns 1 if zero
        wpm = ((len(user_text)/time_elapsed/60)/5)   #calculates the word per minute 
                                                    #considering word consist of 5 letter per word

        if ord(key)== 27:
            break

        if key in("KEY_BACKSPACE",'\b',"\x7f"):
            if len(user_text)>0:
                user_text.pop()
        elif(len(user_text) < len(sentence)):
            user_text.append(key)
        
            


    

def main(stdscr):
    #for text color
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    start(stdscr)
    test(stdscr)
   

wrapper(main)
