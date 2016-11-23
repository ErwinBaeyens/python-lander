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

	
