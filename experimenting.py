import time

EXAMPLE_TO_RUN = 8

if EXAMPLE_TO_RUN == 8:
    try:
        f = open('myfile.txt')
    except OSError as error_message:
        print( 
            error_message.args[:]) 