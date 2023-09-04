class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False

    def turn_on(self):
        return self.turn_on

    def turn_off(self):
        return self.turn_off

    def get_channel(self):
        self.channel = 1

    def set_channel(self, channel=1):
        self.channel = channel

    def get_volume(self):
        return self.volume

    def set_volume(self, volume=1):
        self.volume = volume

    def channel_up(self):
        self.channel += 1

    def channel_down(self):
        self.channel -= 1

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        self.volume -= 1
