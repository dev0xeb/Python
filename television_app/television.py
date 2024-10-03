class Television:
    def __init__(self):
        self.is_on:bool = False
        self.channel:int = 1
        self.volume_level = 1
        self.mute:bool = False

    def television_is_off(self):
        self.is_on = False

    def television_is_on(self):
        self.is_on = True

    def turn_on(self):
        self.television_is_on()
        return self.is_on

    def turn_off(self):
        self.television_is_off()
        return self.is_on

    def get_channel(self):
        return self.channel

    def channel_up(self):
        if self.is_on:
            if self.channel > 100:
                raise ValueError('Channel cannot be greater than 100')
        else:
            self.channel += 1


    def channel_down(self):
        if self.is_on:
            if self.channel > 1:
                self.channel -= 1
            else :
                raise ValueError('Channel cannot go below 1')

    def set_channel(self, channel):
        if channel < 1 or channel > 100:
            raise ValueError('Channel must be in the range of 1 and 100')
        elif not self.is_on:
            raise ValueError('Television not on')
        else:
            self.channel = channel
            return self.channel

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume):
        if volume < 0 or volume > 100:
            raise ValueError('Volume must be in the range of 1 and 100')
        elif not self.is_on:
            raise ValueError('Television not on')
        else:
            self.volume_level = volume
            return self.volume_level

    def volume_up(self):
        if self.is_on:
            if self.volume_level > 100:
                 raise ValueError('Volume cannot be greater than 100')
            else:
                self.volume_level += 1

    def volume_down(self):
        if self.is_on:
            if self.volume_level > 1:
                self.volume_level -= 1
            else:
                raise ValueError('Volume cannot go below 0')

    def is_mute(self):
        self.mute = True

    def unmute(self):
        self.mute = False
