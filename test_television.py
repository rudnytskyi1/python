import pytest
from television import Television


class Test:
    def test_init(self):
        television = Television()
        assert str(television) == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        television = Television()
        television.power()
        assert str(television) == 'Power = True, Channel = 0, Volume = 0'
        television.power()
        assert str(television) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        television = Television()
        television.power()
        television.volume_up()
        television.mute()
        assert str(television) == 'Power = True, Channel = 0, Volume = 0'
        television.mute()
        assert str(television) == 'Power = True, Channel = 0, Volume = 1'
        television.power()
        assert str(television) == 'Power = False, Channel = 0, Volume = 1'
        television.mute()
        assert str(television) == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        television = Television()
        television.channel_up()
        assert str(television) == 'Power = False, Channel = 0, Volume = 0'
        television.power()
        television.channel_up()
        assert str(television) == 'Power = True, Channel = 1, Volume = 0'
        television.channel_up()
        television.channel_up()
        television.channel_up()
        assert str(television) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        television = Television()
        television.channel_down()
        assert str(television) == 'Power = False, Channel = 0, Volume = 0'
        television.power()
        television.channel_down()
        assert str(television) == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        television = Television()
        television.volume_up()
        assert str(television) == 'Power = False, Channel = 0, Volume = 0'
        television.power()
        television.volume_up()
        assert str(television) == 'Power = True, Channel = 0, Volume = 1'
        television.mute()
        television.volume_up()
        assert str(television) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        television = Television()
        television.volume_down()
        assert str(television) == 'Power = False, Channel = 0, Volume = 0'
        television.power()
        television.volume_up()
        television.volume_up()
        television.volume_down()
        assert str(television) == 'Power = True, Channel = 0, Volume = 1'
        television.mute()
        television.volume_down()
        assert str(television) == 'Power = True, Channel = 0, Volume = 0'
