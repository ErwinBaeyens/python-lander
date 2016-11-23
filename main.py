#!/usr/bin/env python

import sys
from time import sleep

from lander import Lander


# Lunar lander
# rework of the original basic version


def main():    
    print "You are aboard the lunar Lander and you are about to leave for the" 
    print "lunar surface"
    play = True

    while play:
        print "You have left the spacecraft"
        print "try to land with less than 5 m/sec velociy"

        # rest of the program goes here

        # temporary test code
        lem = Lander()
        lem.print_reading()
        lem.height = 800
        lem.print_reading()
        lem.velocity=7
        lem.height=0
        lem.print_reading()
        sleep(5)

        print "Do you want to play again (y/n)?"
        y = str(raw_input()).lower()
        if y == 'n' or y == "no":
            play = False
            del lem
            print "Have a nice day"
            sys.exit(0)


if __name__ == "__main__":
    main()
