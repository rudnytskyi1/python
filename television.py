class Television:
    """Simple Television simulation class with power, mute, volume, channels"""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initializes the Television with power off, unmuted status, 0 volume and 0 channel"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power state of the tv"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute state if the tv is on"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase channel if tv is on, increasing the max channel will change it to min channel"""
        if self.__status:
            self.__channel = Television.MIN_CHANNEL if self.__channel == Television.MAX_CHANNEL else self.__channel + 1

    def channel_down(self) -> None:
        """Decrease channel if tv is on, decrease the min channel will change it to max channel"""
        if self.__status:
            self.__channel = Television.MAX_CHANNEL if self.__channel == Television.MIN_CHANNEL else self.__channel - 1

    def volume_up(self) -> None:
        """Increase volume and unmute tv"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease volume and unmute tv"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return formatted string with tv state"""
        volume = 0 if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
