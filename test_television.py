import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    def test_init(self):
        television = Television()
        self.assertEqual(str(television), f'Power = [False], Channel = [0], Volume = [0]')

    def test_power(self):
        television = Television()
        television.power()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [0]')
        television.power()
        self.assertEqual(str(television), f'Power = [False], Channel = [0], Volume = [0]')

    def test_mute(self):
        television = Television()
        television.power()
        television.volume_up()
        television.mute()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [1]')
        television.mute()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [1]')
        television.power()
        television.mute()
        self.assertEqual(str(television), f'Power = [False], Channel = [0], Volume = [1]')
        television.mute()
        self.assertEqual(str(television), f'Power = [False], Channel = [0], Volume = [1]')

    def test_channel_up(self):
        television = Television()
        television.channel_up()
        self.assertEqual(str(television), f'Power = [False], Channel = [1], Volume = [0]')
        television.power()
        television.channel_up()
        self.assertEqual(str(television), f'Power = [True], Channel = [2], Volume = [0]')
        television.channel_up()
        television.channel_up()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [0]')

    def test_channel_down(self):
        television = Television()
        television.channel_down()
        self.assertEqual(str(television), f'Power = [False], Channel = [0], Volume = [0]')
        television.power()
        television.channel_down()
        self.assertEqual(str(television), f'Power = [True], Channel = [3], Volume = [0]')

    def tset_volume_up(self):
        television = Television()
        television.volume_up()
        self.assertEqual(str(television), f'Power = [False], Channel = [0], Volume = [0]')
        television.power()
        television.volume_up()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [2]')
        television.mute()
        television.volume_up()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [2]')

    def test_volume_down(self):
        television = Television()
        television.volume_down()
        self.assertEqual(str(television), f'Power = [False], Channel = [0], Volume = [0]')
        television.power()
        television.volume_up()
        television.volume_up()
        television.volume_down()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [1]')
        television.mute()
        television.volume_down()
        self.assertEqual(str(television), f'Power = [True], Channel = [0], Volume = [0]')


if __name__ == "__main__":
    unittest.main()
