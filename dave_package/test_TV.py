from unittest import TestCase

from dave_package.TV import TV


class TestTV(TestCase):

    def setUp(self) -> None:
        self.tv = TV()

    def test_turn_off(self):
        self.tv.turn_on()
        self.tv.turn_off()
        self.assertEqual(self.tv.on, False)

    def test_get_channel(self):
        self.tv.turn_on()
        self.assertEqual(self.tv.channel, 1)

    def test_set_channel(self):
        self.tv.turn_on()
        self.tv.set_channel(2)

    def test_get_volume(self):
        self.tv.turn_on()
        self.assertEqual(self.tv.volume, 1)

    def test_set_volume(self):
        self.tv.turn_on()
        self.tv.set_volume(2)

    def test_channel_up(self):
        self.tv.turn_on()
        self.tv.channel_up()

    def test_channel_down(self):
        self.tv.turn_on()
        self.tv.channel_down()

    def test_volume_up(self):
        self.tv.turn_on()
        self.tv.volume_up()

    def test_volume_down(self):
        self.tv.turn_on()
        self.tv.volume_down()


print(TestTV)
