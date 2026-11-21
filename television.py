
class Television:
    # Constant variables
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):    # Initial values
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel

    def power(self):    # Turns the tv on and off
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self):    # Mutes and unmutes the tv
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.min_volume = self.__volume
                self.__volume = 0
            elif self.__muted == True:
                self.__muted = False
                self.__volume = self.min_volume
                self.min_volume = 0

    def channel_up(self):    # Moves up a channel
        if self.__status == True:
            if self.__channel == self.max_channel:
                self.__channel = self.min_channel
            else:
                self.__channel += 1

    def channel_down(self):    # Moves down a channel
        if self.__status == True:
            if self.__channel == self.min_channel:
                self.__channel = self.max_channel
            else:
                self.__channel -= 1

    def volume_up(self):    # Moves up one volume
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.min_volume
                self.min_volume = 0
            if self.__volume == self.max_volume:
                pass
            else:
                self.__volume += 1

    def volume_down(self):    # Moves down one volume
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.min_volume
                self.min_volume = 0
            if self.__volume == self.min_volume:
                pass
            else:
                self.__volume -= 1

    def __str__(self):    # Shows current values when object is printed
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"