# Write your code here :-)
import time, sys
indent = 0 #How many spaces to indent
indentIncreasing = True #whether indentation is increasing or not

try:
    while True: #main program loop
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.1) #Pause for 0.1 secs

        if indentIncreasing:c
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False

        else:
            #decrease number of spaces
            indent = indent - 1
            if indent == 0:
                #change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
