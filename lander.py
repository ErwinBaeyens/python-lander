#!/usr/bin/env python

import sys
from time import sleep

class Lander():
    height = 0
    velocity = 0
    gravity = 1.622
    fuel = 0
    burn = 0

    def __init__(self):
        self.height = 1000
        self.velocity = 50
        self.fuel = 500

    def print_reading(self):
        if self.height == 1000:
            print "Meter readings"
            print "=============="
            print "Fuel:{:4d} gal Height: {:6.3f} m speed {:6.3f} m/s".format(
                self.fuel, self.height, self.velocity)
        elif self.height > 0:
            print "Fuel:{:4d} gal Height: {:6.3f} m speed {:6.3f} m/s".format(
                self.fuel, self.height, self.velocity)
        else:
            print "Fuel:{:4d} gal Height: {:6.3f} m landingspeed {:6.3f} m/s".format(
                self.fuel, self.height, self.velocity)

    def update_parameters(self, burn, ):
        pass

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
