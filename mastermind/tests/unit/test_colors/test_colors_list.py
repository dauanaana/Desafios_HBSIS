import unittest

from app import ColorsList


class TestListColors(unittest.TestCase):
    def test_if_return_colors(self):
        l = ColorsList(['red', 'blue', 'green', 'orange', 'purple', 'yellow'])
        self.assertEqual(l.get_list(), ['red', 'blue', 'green', 'orange', 'purple', 'yellow'])
