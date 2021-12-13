import sys
import os
if os.name == "nt":
    import msvcrt as getch
else:
    import getch

"""
brainfsck.py -- a featureless python brainfuck interpreter.
Follows all conventional rules of brainfuck, as far as I know. Has been tested with a suite of random programs found on the internet.
Input is done using getch (msvcrt.getch on windows) and does not work with stdin as far as I can tell. This seems to be the de facto standard from what I can tell.
The array used for memory is started at size 30,000 out of tradition, but I have written in the ability for it to increase in size to prevent crashing.
I have done similarly by forcing the pointer position not to go below 0.
"""


# interpreter
class Interpreter:
    def __init__(self):
        self.__interp_array = [0]*30000 # traditional size
        self.__ptr = 0

    def interpret(self, str):
        idx = 0
        while idx < len(str):
            ch = str[idx]

            # dynamically increase array if necessary
            if ch == '>':
                self.__ptr += 1
                if self.__ptr == len(self.__interp_array):
                    self.__interp_array += [0]
            elif ch == '<':
                self.__ptr = 0 if self.__ptr == 0 else self.__ptr - 1

            # include overflow for bytes
            elif ch == '+':
                self.__interp_array[self.__ptr] = self.__interp_array[self.__ptr] + 1 if self.__interp_array[self.__ptr] < 255 else 0
            elif ch == '-':
                self.__interp_array[self.__ptr] = self.__interp_array[self.__ptr] - 1 if self.__interp_array[self.__ptr] > 0 else 255
            
            # user input and output
            elif ch == '.':
                sys.stdout.write(chr(self.__interp_array[self.__ptr]))
            elif ch == ',':
                self.__interp_array[self.__ptr] = ord(getch.getch())

            # loop controls. Use a counter as a stack for brackets
            # loop start only triggers if pointer is 0, loop end always triggers
            elif ch == '[':
                counter = 0
                if self.__interp_array[self.__ptr] == 0:
                    while True:
                        idx += 1
                        if str[idx] == "]":
                            if counter == 0:
                                break
                            else:
                                counter -= 1
                        elif str[idx] == '[':
                            counter += 1
            elif ch == ']':
                counter = 0
                while True:
                    idx -= 1
                    if str[idx] == "[":
                        if counter == 0:
                            break
                        else:
                            counter -= 1
                    elif str[idx] == "]":
                        counter += 1
                idx -= 1
            
            # not strictly part of language, but ignore all other chars
            # move forward in array
            idx += 1

def main():
    # instantiate interpreter
    main_interp = Interpreter()

    # read from file
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as filetext:
            main_interp.interpret(filetext.read())
    else: print("Syntax: python3 brainfsck.py [FILENAME]")
            
if __name__ == '__main__':
    main()