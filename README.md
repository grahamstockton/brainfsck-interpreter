# brainfsck-interpreter
elementary python brainf*ck interpreter


"""
brainfsck.py -- a featureless python brainf*ck interpreter.
Follows all conventional rules of brainf*ck, as far as I know. Has been tested with a suite of random programs found on the internet.
Input is done using getch (msvcrt.getch on windows) and does not work with stdin as far as I can tell. This seems to be the de facto standard from what I can tell.
The array used for memory is started at size 30,000 out of tradition, but I have written in the ability for it to increase in size to prevent crashing.
I have done similarly by forcing the pointer position not to go below 0.
"""
