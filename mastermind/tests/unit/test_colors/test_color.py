import unittest

from app import Color


class TestColor(unittest.TestCase):
    def test_color_retorna_color(self):
        c = Color('Red')
        self.assertEqual(c.get_name(), 'Red')


