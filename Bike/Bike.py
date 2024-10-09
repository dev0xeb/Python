class Bike:
    def __init__(self):
        self.is_on:bool = False
        self.gear:int = 1
        self.speed:int = 0

    def bike_is_on(self):
        self.is_on = True

    def bike_is_off(self):
        self.is_on = False

    def turn_on(self):
        self.bike_is_on()
        return self.is_on

    def turn_off(self):
        self.bike_is_off()
        return self.is_on

    def get_speed(self):
        return self.speed

    def get_gear(self):
        return self.gear

    def accelerate(self):
        self.change_speed(increment = True)

    def decelerate(self):
        self.change_speed(increment = False)

    def change_speed(self, increment):
        if self.is_on:
            if increment:
                if self.gear == 1:
                    self.speed += 1
                elif self.gear == 2:
                    self.speed += 2
                elif self.gear == 3:
                    self.speed += 3
                elif self.gear == 4:
                    self.speed += 4
            else:
                if self.gear == 1:
                    self.speed -= 1
                elif self.gear == 2:
                    self.speed -= 2
                elif self.gear == 3:
                    self.speed -= 3
                elif self.gear == 4:
                    self.speed -= 4
            self.change_gear()

    def change_gear(self):
        if self.is_on:
            if self.speed <= 20:
                self.gear = 1
            elif self.speed <= 30:
                self.gear = 2
            elif self.speed <= 40:
                self.gear = 3
            elif self.speed > 40:
                self.gear = 4
