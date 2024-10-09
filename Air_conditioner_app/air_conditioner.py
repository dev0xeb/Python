class AirConditioner:
    def __init__(self):
        self.is_on = False
        self.temperature = 16

    def is_ac_on(self):
        self.is_on = True

    def is_ac_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_ac_on()
        return self.is_on

    def turn_off(self):
        self.is_ac_off()
        return self.is_on

    def get_temperature(self):
        return self.temperature

    def increase_temperature(self):
        if self.is_on:
            if self.temperature < 30:
                self.temperature += 1
        return self.temperature

    def decrease_temperature(self):
        if self.is_on:
            if self.temperature > 16:
                self.temperature -= 1
        return self.temperature