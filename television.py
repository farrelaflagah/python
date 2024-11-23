class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
   
    def __init__(self) -> None:
        """
        Initializes the Televison object with default values:
        status is off
        muted is False
        volume is MIN_VOLUME
        channel is MIN_CHANNEL
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
       
    def power(self) -> None:
        """
        Turns the TV on and off
        """
        self.__status = not self.__status
   
    def mute(self) -> None:
        """
        If the TV is on, this method mutes and/or unmutes it.
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        If the TV is on, it increases the channel number by one, and when the maximum is reached, it wraps back around to the original channel (the first one).
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
   
    def channel_down(self) -> None:
        """
        If the TV is on, it decreases the channel number by one, and when the minimum is reached, it wraps back around to the final channel (the last one).
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
               
    def volume_up(self) -> None:
        """
        If the TV is on, it increases the volume number by one, and when the maximum is reached, it stops.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        If the TV is on, it decreases the volume number by one, and when the minimum is reached, it stops.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
   
    def __str__(self) -> str:
        """
        Returns a string represnetation of the television's current status:
        power, channel, and volume (the volume will be a 0 if it is muted).
        """
        if self.__status:
            status = "True"
            if self.__muted:
                volume = 0
            else:
                volume = self.__volume
            return f'Power = {status}, Channel = {self.__channel}, Volume = {volume}'
        else:
            status = "False"
            if self.__muted:
                volume = 0
            else:
                volume = self.__volume
            return f'Power = {status}, Channel = {self.__channel}, Volume = {volume}'