import unittest
from unittest.mock import patch, Mock, call

from app import MasterMind
from app.colors.colors_list import ColorsList


class TestMarterMind(unittest.TestCase):

    # game
    @patch('app.mastermind.mastermind.choice')
    @patch('app.mastermind.mastermind.input')
    @patch('app.mastermind.mastermind.print')
    def test_if_mastermind_is_playing(self, mock_print, mock_input, mock_choice):
        mock_input.side_effect = ['Red', 'Blue', 'Purple', 'Yellow']

        red = Mock()
        red.get_name.return_value = 'Red'
        blue = Mock()
        blue.get_name.return_value = 'Blue'
        purple = Mock()
        purple.get_name.return_value = 'Purple'
        yellow = Mock()
        yellow.get_name.return_value = 'Yellow'

        mock_choice.side_effect = [red, blue, purple, yellow]
        color_list = Mock()

        color_list.get_list.return_value = [red, blue, purple, yellow]
        master = MasterMind(color_list)

        master.game()

    # title
    @patch('app.mastermind.mastermind.print')
    def test_if_function_return_with_title(self, mock_print):
        master = MasterMind(Mock)
        method = master.title()
        assert mock_print(method)

    # raffle
    @patch('app.mastermind.mastermind.choice')
    def test_if_function_really_is_raffling_a_four_color_list(self, mock_choice):
        color_list = Mock()
        MasterMind(color_list)
        master = MasterMind(ColorsList([]))
        master.raffle_colors()
        self.assertEqual(4, mock_choice.call_count)
        self.assertListEqual(
            [call([]), call([]), call([]), call([])],
            mock_choice.mock_calls
        )

    # four_color_password
    @patch('app.mastermind.mastermind.input')
    def test_if_its_really_asking_for_four_colors(self, mock_input):
        mock_input.side_effect = ['Red', 'Blue', 'Purple', 'Green']
        master = MasterMind(Mock())
        master.converted_random_colors = [1, 2, 3, 4]
        master.four_color_password()
        self.assertEqual(len(master.four_color), 4)
        self.assertNotEqual(len(master.four_color), 5)

    # converted_random_colors_to_string
    @patch.object(ColorsList, 'get_list')
    def test_if_it_is_actually_converting_from_object_to_string(self, mock_get_list):
        mock_get_list.return_value = []
        master = MasterMind(ColorsList([]))
        master.converted_random_colors_to_string()

    # round black
    @patch('app.mastermind.mastermind.print')
    def test_contains_color_entered_at_the_same_position_in_the_password_list(self, mock_print):
        color_list = Mock()
        master = MasterMind(color_list)
        master.converted_random_colors = ["Blue", "Red", "Purple", "Yellow"]
        master.four_color = ["Blue", "Red", "Purple", "Yellow"]
        master.round()
        assert mock_print.call_args_list == [call('Black'), call('Black'), call('Black'), call('Black')]

    # round white
    @patch('app.mastermind.mastermind.print')
    def test_contains_color_entered_in_the_drawn_password(self, mock_print):
        color_list = Mock()
        master = MasterMind(color_list)
        master.converted_random_colors = ["Red", "Blue", "Yellow", "Red"]
        master.four_color = ["Red", "Yellow", "Red", "Yellow"]
        master.round()
        assert mock_print.call_args_list == [call('Black'), call('White'), call('White'), call('White')]

    # attemps_game
    @patch('app.mastermind.mastermind.print')
    def test_if_really_the_color_is_invalid(self, mock_print):
        color_list = Mock()
        master = MasterMind(color_list)
        master.converted_random_colors = ["Red", "Blue", "Yellow", "Red"]
        master.four_color = ["Red", "Yellow", "Red", "Pink"]
        master.attemps_game()
        # print(mock_print.call_args_list)
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_args_list, [call('Error: invalid color')])

    ## you_won
    @patch('app.mastermind.mastermind.print')
    def test_if_it_really_won(self, mock_print):
        master = MasterMind(Mock())
        master.four_color = ["Red", "Blue", "Yellow", "Red"]
        master.converted_random_colors = ["Red", "Blue", "Yellow", "Red"]
        master.you_won()
        mock_print.assert_called_once_with(('YOU WON!!! :)'))

    # you_lost
    @patch('app.mastermind.mastermind.print')
    def test_if_really_missed(self, mock_print):
        master = MasterMind(Mock())
        master.error = 4
        master.you_lost()
        mock_print.assert_called_once_with('YOU LOST!!! :(')





